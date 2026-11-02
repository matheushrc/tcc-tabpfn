const { spawn } = require('node:child_process');
const path = require('node:path');

// Resolve from this helper so the MCP does not depend on the caller's cwd.
const root = path.resolve(__dirname, '..');
// PDFCraft's MCP runs independently of the desktop editor.
const bridge = spawn('flatpak', [
  'run',
  '--command=pdfcraft-cli',
  'ai.storyteller.pdfcraft',
  'mcp',
  '--compact',
  '--root', root,
  '--automation-read-root', root,
  '--automation-write-root', root,
], {
  cwd: root,
  // Keep stdout exclusively for JSON-RPC; diagnostics go to stderr.
  stdio: 'inherit',
  windowsHide: true,
});

bridge.on('error', error => {
  console.error('Failed to start PDFCraft MCP: ' + error.message);
  process.exitCode = 1;
});
bridge.on('exit', (code, signal) => {
  process.exitCode = code ?? (signal === 'SIGINT' ? 130 : 1);
});

for (const signal of ['SIGINT', 'SIGTERM']) {
  process.on(signal, () => bridge.kill(signal));
}
