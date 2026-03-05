# Sistema de Gerenciamento de Portfólio de Investimentos

Sistema interativo desenvolvido em Python para registrar ativos financeiros, simular variações de mercado e acompanhar o desempenho do seu portfólio de investimentos.


# Funcionalidades

| Opção 

| 1 | Adicionar ativo 
| 2 | Simular variação de mercado 
| 3 | Mostrar desempenho dos ativos 
| 4 | Mostrar ranking 
| 5 | Mostrar resumo geral 
| 6 | Sair 

| Funcionalidade

| 1 | Registra um novo ativo informando nome e valor investido 
| 2 | Aplica uma variação percentual ao valor atual de um ativo 
| 3 | Exibe lucro/prejuízo e variação percentual de cada ativo 
| 4 | Classifica os ativos em ganhadores e perdedores 
| 5 | Apresenta visão consolidada de todo o portfólio 
| 6 | Encerra o programa 


# Tecnologias Utilizadas

- Python 3


# Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/saemiuyeda/Portfolio-Investimentos.git

2. Acesse a pasta do projeto:
```bash
cd portfolio-investimentos
```

3. Execute o programa:
```bash
python main.py
```


# Estrutura do Projeto

```
portfolio-investimentos/
│
├── main.py            # Arquivo principal com a lógica do sistema
├── portfolio_art.py   # Arte ASCII exibida na inicialização
└── README.md          # Documentação do projeto
```


# Exemplo de Uso

```
1- Adicionar ativo
2- Simular variação de mercado
3- Mostrar desempenho dos ativos
4- Mostrar ranking
5- Mostrar resumo geral
6- Sair

Escolha uma das opções digitando o número correspondente:
 1

'Adicionar ativo' selecionado.
Digite o nome do ativo: PETR4
Digite o valor investido: R$ 1500
PETR4 adicionado com sucesso.
```


# Conceitos Python Aplicados

- Dicionários aninhados
- Funções reutilizáveis
- Laço `while` com flag de controle
- Estruturas condicionais `if/elif/else`
- Tratamento de exceções com `try/except`
- Ordenação com `sorted` e `lambda`
- Formatação com f-strings