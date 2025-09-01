def calcular_area_retangulo(largura, altura):
    """Calcula a área de um retângulo."""
    return largura * altura


def main():
    # Variáveis
    largura = 10
    altura = 5

    # Lista de números
    numeros = [1, 2, 3, 4, 5]

    # Dicionário
    dados = {"nome": "Python", "versao": 3.12, "ativo": True}

    # Cálculo da área
    area = calcular_area_retangulo(largura, altura)

    # Output
    print(f"Largura: {largura}")
    print(f"Altura: {altura}")
    print(f"Área do retângulo: {area}")
    print(f"Números: {numeros}")
    print(f"Dados: {dados}")

    # Loop simples
    for i, numero in enumerate(numeros):
        if numero % 2 == 0:
            print(f"Número {numero} é par (posição {i})")
        else:
            print(f"Número {numero} é ímpar (posição {i})")


if __name__ == "__main__":
    main()
