def calc(n1, n2, op):
    try:
        match op:
            case 1:
                return n1 + n2
            case 2:
                return n1 - n2
            case 3:
                return n1 * n2
            case 4:
                if n2 == 0:
                    return "Erro! Divisão por zero não é permitida."
                return n1 / n2
            case 5:
                return n1 ** n2
            case 6:
                if n2 == 0:
                    return "Erro! Não é possível calcular a raiz n-ésima com n sendo zero."
                return n1 ** (1 / n2)
            case _:
                return "Erro! Opção desconhecida."
    except Exception as e:
        return f"Erro! {e}"

def getNum():
    try:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        op = int(input("""--- Bem-vindo à Calculadora ---
Escolha a operação que deseja realizar entre os dois números escolhidos:\n
1. Soma
2. Subtração
3. Multiplicação
4. Divisão
5. Potenciação
6. Radiciação
0. Sair\n
Digite o número da opção: """))
        if op == 0:
            print("Saindo da calculadora...")
            return None, None, None
        return n1, n2, op
    except ValueError:
        print("Por favor, digite um número válido.")
        return None, None, None

while True:
    n1, n2, op = getNum()
    if n1 is None or n2 is None or op is None:
        break
    resultado = calc(n1, n2, op)
    print(f"Resultado: {resultado}")


