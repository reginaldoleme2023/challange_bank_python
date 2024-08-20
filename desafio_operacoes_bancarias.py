menu = """
    [d] = Depositar
    [s] = Sacar
    [e] = Extrato
    [q] = Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

def option_choice(value): 
   global saldo 
   global extrato 
   global numero_saques 
   global limite
   match value: 

        case "d": 

             valor = float(input("Informe o valor do depósito: "))
             if valor > 0:
             
                saldo += valor
              
                extrato += f"Depósito: R$ {valor:.2f}\n"
                return extrato

             else:
                return "Operação falhou! O valor informado é inválido."

        case "s": 
          
            if(numero_saques >= LIMITE_SAQUE):
                return "Operação falhou! Número máximo de saques excedido." 
            
            valor = float(input("Informe o valor do saque: "))

            if(valor > saldo):
                return "Operação falhou! Você não tem saldo suficiente."
            if (valor > limite):
                return "Operação falhou! O valor do saque excede o limite."
            if(valor>0):
              saldo -= valor
              numero_saques += 1
              extrato += f"Saque: R$ {valor:.2f}\n"
              return f"Saque: R$ {valor:.2f}\n"

        case "e": 

             print("\n================ EXTRATO ================")
             print("Não foram realizadas movimentações." if not extrato else extrato)
             print(f"\nSaldo: R$ {saldo:.2f}")
             return "=========================================="

        case _: 

            return "Opção Inválida!" 

while True:
    option = input(menu)
    if(option == "q"):
        break
    result = option_choice(option)
    print(result)

        