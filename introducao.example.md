# 1 INTRODUÇÃO

## 1.1 APRESENTAÇÃO

No decorrer dos últimos anos têm se notado um aumento contínuo no uso de aplicações que interagem com APIs web, estas vão desde aplicações web e desktop, até sistemas instalados em dispositivos móveis, que necessitam buscar algum recurso conforme iteração do usuário ou sistema, por exemplo buscar informações atualizadas do clima ou receber e enviar mensagens.

Para tornar possível essa transmissão se faz necessário o uso de tecnologias específicas para tal comunicação (2). Um dos padrões mais utilizados para construção de APIs é o REST (Representational State Transfer), que apesar de seus inúmeros benefícios, possui muitas vezes algumas limitações, como por exemplo a transferência de dados desnecessários para o cliente, assim utilizando recursos da rede e processamento dispensáveis. Com o intuito de otimizar a transferência de dados entre a comunicação dos seus serviços em 2012 o Facebook lançou o GraphQL (Graph Query Language), que é uma linguagem de consulta para comunicação entre cliente e API (3).

O GraphQL tem como grande vantagem que somente o que é solicitado pelo cliente vai ser disponibilizado, e nada mais, assim gerando uma economia no uso de rede e processamento de dados. Apesar de ter sido desenvolvido pelo Facebook, em 2015 o GraphQL se tornou open source e passou a ser administrado pela GraphQL Foundation, o que incentivou sua adesão pela comunidade de desenvolvedores, sendo grande o número de empresas que passou adotá-lo na comunicação de suas APIs, um exemplo disso é o Github(3).

Contudo, por se tratar de uma tecnologia relativamente nova, existem poucas pesquisas para automatização de geração de consultas para APIs GraphQL, o que poderia vir a corroborar na área de testes, e assim contribuir na construção de APIs mais robustas e seguras, com menor suscetibilidade a falhas. Porém, para tornar a geração de testes automáticos viáveis e com maior cobertura de casos uma abordagem é a geração autônoma de consultas GraphQL válidas para a API, assim evitando trabalho humano para criação das consultas de teste. Neste ponto a geração de consultas aleatórias em GraphQL viria a ser um utilitário para possibilitar a execução de testes de forma mais independente e com grande cobertura de casos (8).

Este trabalho propõe-se para a geração de consultas GraphQL de forma aleatória baseados no esquema da API GraphQL, repeitando suas regras e gerando assim consultas válidas, deste modo oferecendo um aparato a mais para facilitar a construção de testes para APIs que envolvem a tecnologia GraphQL.

## 1.2 PROBLEMA DE PESQUISA

É possível criar uma ferramenta para geração de consultas GraphQL que sejam válidas e de forma aleatória, estas baseadas no esquema da API para geração de casos de testes utilizando a linguagem Haskell?

## 1.3 HIPÓTESE DE PESQUISA

A geração de consultas válidas de forma aleatória para APIs GraphQL é útil para efetuar testes de API com maior cobertura de casos, sem necessidade de esforço humano para gerar as consultas.

## 1.4 OBJETIVOS

## 1.4.1 Objetivos gerais

O objetivo geral deste trabalho é criar uma ferramenta para realizar a geração de consultas GraphQL de forma aleatória baseados no esquema da API GraphQL.

## 1.4.2 Objetivos específicos

- Revisar na literatura os trabalhos propostos para geração de consultas GraphQL de forma aleatória;
- Estudar o formato e a especificação da linguagem GraphQL;
- Criar ferramenta para geração de consultas GraphQL de forma aleatória utilizando a linguagem de programação Haskell;
- Implementar testes baseados em propriedades utilizando os casos de teste gerados como entrada.
- Testar as consultas geradas automaticamente em uma API GraphQL de teste.

## 1.5 JUSTIFICATIVA

Desenvolver software robusto e confiável é de extrema importância em um mundo onde cada vez mais a tecnologia está presente no cotidiano das pessoas e empresas. Desde a área de saúde e transporte e até mesmo nas atividades de lazer e entretenimento existe o uso de softwares pra aprimorar e auxiliar. Algo muito importante no desenvolvimento de software é a parte de testes, onde se objetiva simular possíveis cenários de uso, visando antecipar o encontro de erros antes que chegue ao usuário final. Portanto ter maneiras fáceis de criar testes vem auxiliar essa área tão importante para a qualidade de software. Uma tecnologia presente atualmente no segmento de software é o GraphQL que é uma ferramenta para comunicação entre cliente e API (Interface de Programação de Aplicação). O presente trabalho tem como proposta auxiliar na produção de testes para o GraphQL gerando consultas válidas de forma automática, assim facilitando a criação de testes evitando trabalho humano que pode ser dispensável, assim deixando livre para outras atividades.
