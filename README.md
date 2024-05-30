## Descrição
Este é um projeto simples de uma aplicação com uma configuração básica de CI/CD utilizando GitHub Actions.

## Configuração do Projeto

### Estrutura do Projeto
devops/
├── .github/
│ └── workflows/
│ └── ci.yml
├── src/
│ └── my_module.py
├── tests/
│ ├── test_unit.py
│ └── test_integration.py
├── requirements.txt
├── .gitignore
└── README.md

### Dependências
As dependências do projeto estão listadas no arquivo `requirements.txt`:

## Configuração do GitHub Actions
O workflow de CI/CD está definido no arquivo `.github/workflows/ci.yml` e é executado a cada push no branch principal. Ele inclui as seguintes etapas:
1. Check out do repositório.
2. Configuração do Python.
3. Instalação das dependências.
4. Execução dos testes unitários e de integração.

## Testes Automatizados
Os testes automatizados estão localizados no diretório `tests`. O arquivo `test_unit.py` contém testes unitários para a função `my_function` e o arquivo `test_integration.py` contém testes de integração para `my_function` e `another_function`.
