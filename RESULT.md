# Resultado - Desafio CoorLab

## Implementação
O frontend foi desenvolvido utilizando Vue.js (v3) com o auxílio do Vite para a inicialização rápida do projeto e uma experiência de desenvolvimento ágil. O backend foi construído em Python utilizando o framework Flask para a criação de uma API REST.


## Backend (Python)

- **Tecnologias Utilizadas**: Python, Flask
  - *Python*: Uma linguagem de programação de alto nível conhecida por sua simplicidade e legibilidade de código. Utilizada principalmente para desenvolvimento web e científico.
  - *Flask*: Um microframework web em Python que permite construir aplicativos web de forma rápida e simples.
- **Estrutura do Projeto**: 
  - Criei um arquivo `app.py` para definir as rotas da API REST.
  - Utilizei o arquivo `data.json` como base de dados para as viagens.
- **Funcionalidades Implementadas**:
  - Criei uma rota `/travels` que retorna os dados das viagens de acordo com os parâmetros de destino e data.
  - Criei uma rota `/fecth` que retorna os a lista de cidades presente no json para ser usado na lista do selector no frontend.
  - Implementei a lógica para buscar as viagens mais confortáveis e rápidas, assim como as mais econômicas
- **Testes Realizados**:
  - Testei as rotas utilizando o Postman para garantir que os dados estavam sendo retornados corretamente.
- **Observações**:
  - Adicionei uma verificação em que quando a passagem mais barata for igual à mais rápida e confortável, o backend retorna apenas 1 única passagem.

## Frontend (Vue.js)

- **Tecnologias Utilizadas**: Vue.js, HTML, CSS, Vite, Vuetify
  - *Vue.js*: Um framework progressivo para a construção de interfaces de usuário. Possui uma curva de aprendizado suave e é altamente adaptável.
  - *Vite*: Um construtor de aplicações web extremamente rápido e leve que utiliza o moderno ESM (ECMAScript Modules) para uma inicialização rápida do projeto.
  - *Vuetify*: Uma biblioteca de componentes Vue.js baseada no Material Design que oferece uma ampla gama de componentes prontos para uso.
- **Estrutura do Projeto**:
  - Inicializei o projeto Vue através do Vite e adicionei a biblioteca Vuetify.
  - 
- **Funcionalidades Implementadas**:
  - Criei a página de busca por viagens com campos de destino e data.
  - Implementei a lógica para buscar os dados das viagens no backend e exibi-los na tela.
  - Exibi os dados das viagens mais confortáveis e rápidas, assim como as mais econômicas.
  - Implementei o modal que informa ao usuário que todas os campos devem ser preenchidos para poder realizar a busca.
- **Testes Realizados**:
  - Testei a interação com a página e a exibição dos dados para garantir que tudo funcionava corretamente.
- **Observações**:
  - Utilizei classes CSS para estilizar os componentes e deixar a interface amigável e responsiva para desktop.
  - Quando a passagem mais barata for igual à mais rápida e confortável, será exibida apenas um 1 opção, contendo um texto logo abaixo informando ao usuário que aquela é a passagem com menor custo e menor tempo de viagem.
  - Utilizei o Vuetify para acessar uma ampla variedade de componentes prontos para uso, empregando a biblioteca para criar o seletor usado na escolha das cidades e também para aproveitar a biblioteca de ícones do Material Design.

## Considerações Finais

Durante o desenvolvimento deste projeto, enfrentei desafios ao dominar um novo framework, Vue.js, resultando em erros e bugs devido à inexperiência inicial. No entanto, minha familiaridade com outros frameworks me permitiu buscar soluções com sucesso, aprimorando minhas habilidades de pesquisa.

Apesar de implementar apenas responsividade para desktop devido ao prazo, reconheço a importância de tornar a aplicação acessível em dispositivos móveis, e desejo explorar essa possibilidade futuramente. Além disso, considero a adição de um guia de protótipo para melhorias no design e uma página detalhada para visualização de passagens.

Apesar dos desafios e das áreas que gostaria de explorar mais a fundo, estou satisfeito com o resultado alcançado neste projeto. Foi uma vivência gratificante criar algo novo utilizando tecnologias que estavam fora da minha zona de conforto. Estou ansioso para continuar aprendendo e crescendo como desenvolvedor, buscando sempre expandir meu conhecimento e habilidades em novas áreas.
