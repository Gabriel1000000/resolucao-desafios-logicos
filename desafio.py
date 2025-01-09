import json

# 1. Cálculo do valor da variável SOMA
def calcular_soma():
    indice = 13
    soma = 0
    k = 0

    while k < indice:
        k += 1
        soma += k

    print(f"1. Valor de SOMA = {soma}")

# 2. Verifica se um número pertence à sequência de Fibonacci
def is_fibonacci(num):
    a, b = 0, 1
    while b <= num:
        if b == num:
            return True
        a, b = b, a + b
    return False

def verificar_fibonacci():
    numero = int(input("\n2. Informe um número para verificar se pertence à sequência de Fibonacci: "))
    if is_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

# 3. Análise de faturamento diário
def analisar_faturamento_diario():
    faturamento_json = '''
    [
        {"dia": 1, "valor": 200.0},
        {"dia": 2, "valor": 0.0},
        {"dia": 3, "valor": 300.0},
        {"dia": 4, "valor": 0.0},
        {"dia": 5, "valor": 100.0}
    ]
    '''
    dados = json.loads(faturamento_json)
    valores = [item['valor'] for item in dados if item['valor'] > 0]

    menor = min(valores)
    maior = max(valores)
    media = sum(valores) / len(valores)
    dias_acima_media = sum(1 for v in valores if v > media)

    print("\n3. Análise de Faturamento Diário:")
    print(f"Menor valor: {menor}")
    print(f"Maior valor: {maior}")
    print(f"Dias acima da média: {dias_acima_media}")

# 4. Cálculo do percentual de faturamento por estado
def calcular_percentual_faturamento():
    faturamento = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }

    total = sum(faturamento.values())
    percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento.items()}

    print("\n4. Percentual de Faturamento por Estado:")
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")

# 5. Inversão de string
def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

def inverter_texto():
    texto = input("\n5. Digite uma string para inverter: ")
    print(f"String invertida: {inverter_string(texto)}")

# Executando as funções
if __name__ == "__main__":
    calcular_soma()
    verificar_fibonacci()
    analisar_faturamento_diario()
    calcular_percentual_faturamento()
    inverter_texto()
