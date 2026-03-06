from portfolio_art import logo

def calcular_variacao(percentual, v_atual):
    novo_valor = (1 + percentual / 100) * v_atual
    return novo_valor

def calcular_desempenho(v_investido, v_atual):
    desempenho = ((v_atual - v_investido) / v_investido) * 100
    return desempenho

print(logo)

portfolio = {}

sair = False

while not sair:
    print("1- Adicionar ativo \n2- Simular variação de mercado \n3- Mostrar desempenho dos ativos \n4- Mostrar ranking"
          "\n5- Mostrar resumo geral \n6- Sair")
    opcao = input("Escolha uma das opções digitando o número correspondente:\n ")

    if opcao == "1":
        print("'Adicionar ativo' selecionado.")

        nome = input("Digite o nome do ativo: ").strip().upper()

        if nome in portfolio:
            print("⚠️ Este ativo já está cadastrado. ⚠️")
            print("\n" * 10)
        else:
            try:
                valor_inv = float(input("Digite o valor investido: R$ "))
                valor_atual = valor_inv
                if valor_inv < 0:
                    print("Valor negativo. Bloqueado.")
                else:
                    portfolio[nome] = {
                        "valor investido": valor_inv,
                        "valor atual": valor_atual
                    }
                    print(f"Ativo. \n{nome} adicionado com sucesso.")
                print("\n" * 10)

            except ValueError:
                print("Valor inválido. \nOperação cancelada.")
                print("\n" * 10)

    elif opcao == "2":
        print("'Simular variação de mercado' selecionado.")
        aplicar_var = input("Qual ativo deseja aplicar a variação?: ").strip().upper()

        if aplicar_var not in portfolio:
            print("Este ativo não foi encontrado.")
            print("\n" * 10)

        else:
            try:
                var_percentual = float(input("Qual a variação percentual do mercado?: "))

                valor_atual = portfolio[aplicar_var]["valor atual"]
                novo_valor = calcular_variacao(var_percentual, valor_atual)
                portfolio[aplicar_var]["valor atual"] = novo_valor
                print(f"Variação aplicada. \nNovo valor do ativo {aplicar_var}: R${novo_valor:.2f}")
                print("\n" * 10)
            except ValueError:
                print("Valor inválido. Operação cancelada.")
                print("\n" * 10)

    elif opcao == "3":
        print("'Mostrar desempenho dos ativos' selecionado.")
        if not portfolio:
            print("Não há nenhum ativo adicionado.")
        else:
            for nome, dados in portfolio.items():
                valor_investido = dados["valor investido"]
                valor_atual = dados["valor atual"]

                lucro = valor_atual - valor_investido
                desempenho = calcular_desempenho(valor_investido, valor_atual)

                print(f"Ativo: {nome}\nInvestido: R$ {valor_investido:.2f}\nAtual: R$ {valor_atual:.2f}\n"
                      f"Lucro: R$ {lucro:.2f}\nVariação: {desempenho:+.2f}%")
                print("\n")
            print("\n" * 10)

    elif opcao == "4":
        print("'Mostrar ranking' selecionado.")

        if not portfolio:
            print("Não há ativos cadastrados.")
        else:
            ganhos = []
            perdas = []

            for nome,dados in portfolio.items():
                valor_investido = dados["valor investido"]
                valor_atual = dados["valor atual"]

                percentual = calcular_desempenho(valor_investido, valor_atual)

                if percentual > 0:
                    ganhos.append((nome, percentual))
                elif percentual < 0:
                    perdas.append((nome, percentual))
                elif percentual == 0:
                    print("Este ativo não apresentou variação percentual.")

            ganhos = sorted(ganhos, key=lambda x: x[1], reverse=True)
            perdas = sorted(perdas, key=lambda x: x[1])

            print("===== GANHADORES =====")

            if ganhos:
                for posicao, (nome, percentual) in enumerate(ganhos, start=1):
                    print(f"{posicao}° {nome} -> {percentual:+.2f}%")
                print("\n")
            else:
                print("Nenhum ativo com desempenho positivo.")

            print("\n===== PERDEDORES =====")

            if perdas:
                for posicao, (nome, percentual) in enumerate(perdas, start=1):
                    print(f"{posicao}° {nome} -> {percentual:+.2f}%")
                print("\n" * 10)
            else:
                print("Nenhum ativo com desempenho negativo.")
                print("\n" * 10)

    elif opcao == "5":
        print("'Mostrar resumo geral' selecionado.")

        if not portfolio:
            print("Não há ativos cadastrados.")
        else:
            total_ativos = len(portfolio)
            total_investido = 0
            total_atual = 0
            total_lucro_prejuizo = 0

            for nome, dados in portfolio.items():
                valor_investido = dados["valor investido"]
                total_investido += valor_investido

                valor_atual = dados["valor atual"]
                total_atual += valor_atual

                lucro = valor_atual - valor_investido
                total_lucro_prejuizo += lucro

            variacao_percentual = calcular_desempenho(total_investido, total_atual)

            print(f"Número de ativos: {total_ativos}\nValor investido total: {total_investido:.2f}\n"
                  f"Valor atual total: {total_atual:.2f}\nLucro/prejuízo total: {total_lucro_prejuizo:.2f}\n"
                  f"Variação percentual: {variacao_percentual:.2f}%")
            print("\n" * 10)

    elif opcao == "6":
        print("'Sair' selecionado")
        sair = True
    else:
        print("Este número é invalido.\nTente novamente.")
        print("\n" * 10)