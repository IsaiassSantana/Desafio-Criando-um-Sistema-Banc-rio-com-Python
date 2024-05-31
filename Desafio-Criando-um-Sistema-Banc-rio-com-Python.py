menu = """
=========== MENU ESCOLHA UM DAS OPÇÕES ===========
  [1] DEPOSITAR 
  [2] SACAR
  [3] EXTRATO
  [4] SAIR

"""
saldo = 0
limite = 500
extrato = " "
numero_saques = 0
LIMITE_SAQUES  = 3

while True:
  opcao = int(input(menu))

  if opcao == 1:
    print ("Só sera permitido depósito de cedula:")
    valor = int(input ("valor depósito \n"))
    if valor > 0:
      saldo+= valor
      extrato += f"Depósito: R${valor} \n"
      ver_saldo = int (input('''Gostaria de ver seu saldo ou seguir para o menu anterior
      [1] SIM
      [2] NÂO'''))
      print(f"o Seu saldo é R$ {salfo}" if ver_saldo == 1  else "")
    elif valor == 0:
      print ("o valor informado não é válido")

  elif opcao == 2:
    valor = int(input ("Valor de saque"))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    exedeu_saques = LIMITE_SAQUES == 0
    if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

    elif exedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor} \n"
        LIMITE_SAQUES -= 1
    else:
            print("Operação falhou! O valor informado é inválido.")
  elif opcao == 3:
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movizadas."if not extrato else extrato)
    print("==========================================")

  else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


