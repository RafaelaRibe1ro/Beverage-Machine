# Nome: RAFAELA OLIVEIRA RIBEIRO
# Matrícula: 2020100719

from os import system , name

def limpaTela():
    """ Esta função limpa a tela"""

    if name == 'nt':
        system('cls')
    else:
        system('clear')

def valorTotal(faturamento):
    """ Esta função mostra o valor
    total do pedido"""

    print(f"Valor total: R${faturamento:.2f}")

def troco1(valorMax,troco):
    """ Esta função devolve o troco para
    o cliente"""

    # Esta função irá continuar chamando a função
    # Ftroco() até que todo o troco seja fornecido
    # ao cliente
    nota = valorMax

    if nota > 1:
        n = int(troco/nota)
        r = troco - (nota*n)
        print(f"1 nota de R${nota:.2f}")
        troco2 = r + (n-1)*nota
        fTroco(troco2)

    elif nota <= 1:
        n = int(troco/nota)
        r = troco - (nota*n)
        print(f"1 moeda de R${nota:.2f}")
        troco2 = r + (n-1)*nota
        fTroco(troco2)

def fTroco(troco):
    """ Esta função indica qual a maior
    nota de troco que será usada na função
    troco1"""

    if troco >= 100:
        valorMax = 100
        troco1(valorMax,troco)

    elif troco >= 50:
        valorMax = 100
        troco1(valorMax,troco)

    elif troco >= 20:
        valorMax = 20
        troco1(valorMax,troco)

    elif troco >= 10:
        valorMax = 10
        troco1(valorMax,troco)

    elif troco >= 5:
        valorMax = 5
        troco1(valorMax,troco)

    elif troco >= 1:
        valorMax = 1
        troco1(valorMax,troco)

    elif troco >= 0.5:
        valorMax = 0.5
        troco1(valorMax,troco)

    elif troco >= 0.25:
        valorMax = 0.25
        troco1(valorMax,troco)

    elif troco >= 0.1:
        valorMax = 0.1
        troco1(valorMax,troco)

    elif troco >= 0.05:
        valorMax = 0.05
        troco1(valorMax,troco)

    elif troco >= 0.01:
        valorMax = 0.01
        troco1(valorMax,troco)

def detalhesInternos(cafeSoluvel,copos, agua, adocante, acucar, abacate, morango, leite, laranja, faturamento):
    """ Esta função exibe os detalhes internos
    (opção 8 da máquina)"""
    
    limpaTela()
    print("--> Detalhes internos\n")
    print(f"Café solúvel: {cafeSoluvel}g")
    print(f"Copos: {copos} unidades")
    print(f"Água: {agua}ml")
    print(f"Adoçante: {adocante}ml")
    print(f"Açúcar: {acucar}g")
    print(f"Abacate: {abacate} unidades")
    print(f"Morango: {morango} unidades")
    print(f"Leite: {leite}ml")
    print(f"Laranja: {laranja} unidades")
    print(f"Faturamento: R${faturamento:.2f}\n")

def desejaVer(cafeSoluvel,copos, agua, adocante, acucar, abacate, morango, leite, laranja, faturamento):
    """ Esta função permite a visualização dos detalhes
    internos após a compra, caso seja solicitado"""

    ver = input("\nDeseja ver os detalhes internos?: ")

    if ver == "s" or ver == "S":
        detalhesInternos(cafeSoluvel,copos, agua, adocante, acucar, abacate, morango, leite, laranja, faturamento)
        print("\n----------------Obrigado, volte sempre!-------------------\n")

    elif ver == "n" or ver == "N":
        print("\n----------------Obrigado, volte sempre!-------------------\n")

    else:
        print("\nATENÇÃO!!!")
        print("Você deve digitar S para sim e N para não")
        desejaVer(cafeSoluvel,copos, agua, adocante, acucar, abacate, morango, leite, laranja, faturamento)

def novoPedido(cafeSoluvel,copos, agua, adocante, acucar, abacate, morango, leite, laranja, faturamento):
    """ Esta função volta para o menu quando
    o cliente quiser realizar um novo pedido
    ou escolher uma nova opção"""

    novosPedidos = input("Deseja escolher um novo pedido ou opção? (S/N): ")

    # Se o cliente digitar S/s, a máquina retorna ao menu. Se digitar N/n irá para a fase de pagamento
    # ou para o final do programa caso não tenha comprado itens anteriormente,
    # e se não for digitado nenhum desses termos, uma mensagem de atenção será introduzida.
    if novosPedidos == "S" or novosPedidos == "s":
        limpaTela()
        menu(cafeSoluvel,copos, agua, adocante, acucar, abacate, morango, leite, laranja, faturamento)

    elif (novosPedidos == "N" or novosPedidos == "n" )and faturamento > 0:
        limpaTela()
        valorTotal(faturamento)
        dinheiro = float(input("\nColoque o valor em dinheiro: "))

        if dinheiro > faturamento:
            troco = dinheiro - faturamento
            print(f"Seu troco será de R${troco:.2f}")
            print("\nRetire o seu troco:")
            fTroco(troco)
            desejaVer(cafeSoluvel,copos, agua, adocante, acucar, abacate, morango, leite, laranja, faturamento)

        elif dinheiro == faturamento:
            desejaVer(cafeSoluvel,copos, agua, adocante, acucar, abacate, morango, leite, laranja, faturamento)

        elif dinheiro < faturamento:
            print("O valor inserido não é suficiente para o pagamento, tente novamente")
            novoPedido(cafeSoluvel,copos, agua, adocante, acucar, abacate, morango, leite, laranja, faturamento)


    elif novosPedidos == "N" or novosPedidos == "n":
        print("\n----------------Obrigado, volte sempre!-------------------\n")

    else:
        print("\nATENÇÃO!!!")
        print("Você deve digitar S para sim e N para não")
        novoPedido(cafeSoluvel,copos, agua, adocante, acucar, abacate, morango, leite, laranja, faturamento)

def menu(cafeSoluvel, copos, agua, adocante, acucar, abacate, morango, leite, laranja, faturamento):
    """ Esta função exibe o menu, contabiliza e
    exibe todas as ações realizadas pelos clientes"""

    # Exibindo o menu
    print("----------------------MENU----------------------")
    print("Produtos:")
    print("1) Café com açúcar -> \t\tR$ 3,00\n2) Café com adoçante -> \tR$ 2,50\n3) Café amargo -> \t\tR$ 1,50\n4) Vitamina de abacate -> \tR$ 9,00\n5) Vitamina de morango -> \tR$ 9,00\n6) Suco de laranja -> \t\tR$ 6,00\n")
    print("Opções:")
    print("7) Detalhes dos produtos")
    print("8) Detalhes internos")
    print("9) Finalizar compra")
    print("------------------------------------------------\n")

    try:
        escolha = int(input("----> Digite o número do seu pedido ou da opção escolhida: "))
    except:
        limpaTela()
        print("\nATENÇÃO!!!")
        print("Você deve inserir um valor INTEIRO!\n")
        menu(cafeSoluvel, copos, agua, adocante, acucar, abacate, morango, leite, laranja, faturamento)
    else:
        if escolha > 0 and escolha < 10:
            # Contabilizando os pedidos
            if escolha == 1 and cafeSoluvel >= 12 and agua >= 100 and acucar >= 3:
                copos -= 1
                cafeSoluvel -= 12
                agua -= 100
                acucar -= 3
                faturamento += 3
                valorTotal(faturamento)
                novoPedido(cafeSoluvel,copos, agua, adocante, acucar, abacate, morango, leite, laranja, faturamento)

            elif escolha == 2 and cafeSoluvel >= 12 and agua >= 100 and adocante >= 4:
                copos -= 1
                cafeSoluvel -= 12
                agua -= 100
                adocante -= 4
                faturamento += 2.5
                valorTotal(faturamento)
                novoPedido(cafeSoluvel,copos, agua, adocante, acucar, abacate, morango, leite, laranja, faturamento)

            elif escolha == 3 and cafeSoluvel >= 12 and agua >= 100:
                copos -= 1
                cafeSoluvel -= 12
                agua -= 100
                faturamento += 1.5
                valorTotal(faturamento)
                novoPedido(cafeSoluvel,copos, agua, adocante, acucar, abacate, morango, leite, laranja, faturamento)

            elif escolha == 4 and abacate >= 0.5 and leite >= 300 and acucar >= 4:
                copos -= 1
                abacate -= 0.5
                leite -= 300
                acucar -= 4
                faturamento += 9
                valorTotal(faturamento)
                novoPedido(cafeSoluvel,copos, agua, adocante, acucar, abacate, morango, leite, laranja, faturamento)

            elif escolha == 5 and morango >= 4 and leite >= 300 and acucar >= 4:
                copos -= 1
                morango -= 4
                leite -= 300
                acucar -= 4
                faturamento += 9
                valorTotal(faturamento)
                novoPedido(cafeSoluvel,copos, agua, adocante, acucar, abacate, morango, leite, laranja, faturamento)

            elif escolha == 6 and laranja >= 1 and agua >= 300 and acucar >= 4:
                copos -= 1
                laranja -= 1
                agua -= 300
                acucar -= 4
                faturamento += 6
                valorTotal(faturamento)
                novoPedido(cafeSoluvel,copos, agua, adocante, acucar, abacate, morango, leite, laranja, faturamento)

            # Exibindo os detalhes/finalizando compra
            elif escolha == 7:
                limpaTela()
                print("--> Detalhes dos produtos:")
                print("1) Café com açúcar\tR$ 3,00\n- 12g de café solúvel\n- 100ml de água\n- 3g de açúcar\n")
                print("2) Café com adoçante\tR$ 2,50\n- 12g de café solúvel\n- 100ml de água\n- 4ml de adoçante\n")
                print("3) Café amargo\tR$ 1,50\n- 12g de café solúvel\n- 100ml de água\n")
                print("4) Vitamina de abacate\tR$ 9,00\n- 1/2 abacate\n- 300ml de leite\n- 4g de açúcar\n")
                print("5) Vitamina de morango\tR$ 9,00\n- 4 morangos\n- 300ml de leite\n- 4g de açúcar\n")
                print("6) Suco de laranja\tR$ 6,00\n- 1 laranja\n- 300ml de água\n- 4g de açúcar\n")
                novoPedido(cafeSoluvel,copos, agua, adocante, acucar, abacate, morango, leite, laranja, faturamento)

            elif escolha == 8:
                detalhesInternos(cafeSoluvel,copos, agua, adocante, acucar, abacate, morango, leite, laranja, faturamento)
                novoPedido(cafeSoluvel,copos, agua, adocante, acucar, abacate, morango, leite, laranja, faturamento)

            elif escolha == 9 and faturamento == 0:
                limpaTela()
                print("\n----------------Obrigado, volte sempre!-------------------\n")

            elif escolha == 9 and faturamento > 0:
                limpaTela()
                novoPedido(cafeSoluvel,copos, agua, adocante, acucar, abacate, morango, leite, laranja, faturamento)

            # Caso algum dos ingredientes esteja indisponível
            else:
                print("\nDesculpe, um dos ingredientes está indisponível, favor verificar na opção 8 do menu\n")
                novoPedido(cafeSoluvel,copos, agua, adocante, acucar, abacate, morango, leite, laranja, faturamento)

        # Caso seja inserido um valor negativo ou fora das opções:
        else:
            limpaTela()
            print("\nATENÇÃO!!!")
            print("Você deve inserir um valor inteiro positivo de 1 a 9!\n")
            menu(cafeSoluvel, copos, agua, adocante, acucar, abacate, morango, leite, laranja, faturamento)
def main():
    menu(250,50,2000,250,100,30,30,2000,30,0.00)

main()
