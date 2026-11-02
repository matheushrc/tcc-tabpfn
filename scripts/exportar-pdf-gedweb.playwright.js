/** Execute via browser_run_code_unsafe({ filename: caminho absoluto deste arquivo }).
 * Requer uma aba GEDWeb autenticada com a versão correta da norma já aberta.
 * Antes, iniciar scripts/receber-pdf-gedweb.py --output <destino.pdf>.
 * Recarrega apenas essa aba e observa a senha que o próprio leitor recebe.
 * Não usa OCR, capturas de tela, força bruta nem credenciais de terceiros.
 */
async (page) => {
  if (new URL(page.url()).hostname !== 'www.gedweb.com.br' ||
      !new URL(page.url()).pathname.includes('visualizador-docviewer')) {
    throw new Error('Selecione a aba autenticada do visualizador GEDWeb.');
  }
  await page.addInitScript(() => {
    if (!location.hostname.endsWith('gedweb.com.br')) return;
    const original = Worker.prototype.postMessage;
    Worker.prototype.postMessage = function (message, ...args) {
      if (message?.data && typeof message.data.password === 'string') {
        window.__gedwebDocumentPassword = message.data.password;
      }
      if (typeof message?.data?.source?.password === 'string') {
        window.__gedwebDocumentPassword = message.data.source.password;
      }
      return original.call(this, message, ...args);
    };
  });
  await page.reload();
  const iframe = page.locator('iframe[title="webviewer"]');
  await iframe.waitFor();
  const frame = await (await iframe.elementHandle()).contentFrame();
  await frame.waitForFunction(() =>
    typeof window.__gedwebDocumentPassword === 'string' &&
    window.documentViewer?.getDocument()?.getPageCount() > 0,
    undefined, { timeout: 30000 });
  const payload = await frame.evaluate(async () => {
    const doc = window.documentViewer.getDocument();
    const bytes = await doc.ba.pdfDocument.getData();
    let binary = '';
    for (let i = 0; i < bytes.length; i += 32768) {
      binary += String.fromCharCode(...bytes.subarray(i, i + 32768));
    }
    const password = window.__gedwebDocumentPassword;
    delete window.__gedwebDocumentPassword;
    return { pdf: btoa(binary), password, pages: doc.getPageCount() };
  });
  const response = await page.context().request.post('http://127.0.0.1:37660/export', {
    data: payload, timeout: 30000
  });
  payload.password = '';
  payload.pdf = '';
  if (!response.ok()) throw new Error('Receptor local recusou o PDF: HTTP ' + response.status());
  return await response.json();
}
