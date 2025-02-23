def gwei_to_wei(gwei: float) -> int:
    if gwei < 0:
        raise ValueError("O valor em Gwei não pode ser negativo.")
    return int(gwei * 10**9)

def wei_to_gwei(wei: int) -> float:
    if wei < 0:
        raise ValueError("O valor em Wei não pode ser negativo.")
    return wei / 10**9

def eth_to_wei(eth: float) -> int:
    if eth < 0:
        raise ValueError("O valor em ETH não pode ser negativo.")
    return int(eth * 10**18)

def wei_to_eth(wei: int) -> float:
    if wei < 0:
        raise ValueError("O valor em Wei não pode ser negativo.")
    return wei / 10**18

def eth_to_gwei(eth: float) -> float:
    if eth < 0:
        raise ValueError("O valor em ETH não pode ser negativo.")
    return eth * 10**9

def gwei_to_eth(gwei: float) -> float:
    if gwei < 0:
        raise ValueError("O valor em Gwei não pode ser negativo.")
    return gwei / 10**9

def main():
    while True:
        print("=== Conversor de ETH, Gwei e Wei ===")
        print("1 - Gwei para Wei")
        print("2 - Wei para Gwei")
        print("3 - ETH para Wei")
        print("4 - Wei para ETH")
        print("5 - ETH para Gwei")
        print("6 - Gwei para ETH")
        print("7 - Sair")
        
        opcao = input("Digite a opção (1-7): ").strip()
        
        if opcao == '7':
            print("Saindo...")
            break
        
        try:
            if opcao == '1':
                valor = float(input("Digite o valor em Gwei: "))
                resultado = gwei_to_wei(valor)
                print(f"{valor} Gwei = {resultado} Wei")
            elif opcao == '2':
                valor = int(input("Digite o valor em Wei: "))
                resultado = wei_to_gwei(valor)
                print(f"{valor} Wei = {resultado} Gwei")
            elif opcao == '3':
                valor = float(input("Digite o valor em ETH: "))
                resultado = eth_to_wei(valor)
                print(f"{valor} ETH = {resultado} Wei")
            elif opcao == '4':
                valor = int(input("Digite o valor em Wei: "))
                resultado = wei_to_eth(valor)
                print(f"{valor} Wei = {resultado} ETH")
            elif opcao == '5':
                valor = float(input("Digite o valor em ETH: "))
                resultado = eth_to_gwei(valor)
                print(f"{valor} ETH = {resultado} Gwei")
            elif opcao == '6':
                valor = float(input("Digite o valor em Gwei: "))
                resultado = gwei_to_eth(valor)
                print(f"{valor} Gwei = {resultado} ETH")
            else:
                print("Opção inválida! Escolha entre 1 e 7.")
        except ValueError as e:
            if "negativo" in str(e):
                print(str(e))
            else:
                print("Erro: Digite um número válido (ex: 1.5 para Gwei/ETH, 1000 para Wei).")
        print()

if __name__ == "__main__":
    main()
