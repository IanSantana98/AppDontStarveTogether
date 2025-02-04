# Lista de plantas
Plantas = [
    'Cenoura', 'Milho', 'Batata', 'Tomate', 'Berinjela', 'Fruta do Dragão',
    'Pimenta', 'Abóbora', 'Cebola', 'Romã', 'Aspargo', 'Durian',
    'Alho', 'Melancia'
]

# Definição das estações e as plantas que podem ser cultivadas nelas
Estacoes = {
    'Outono': [
        Plantas[i] for i in [0, 1, 2, 3, 4, 6, 7, 8]
    ],
    'Inverno': [
        Plantas[i] for i in [0, 2, 7, 10, 12]
    ],
    'Primavera': [
        Plantas[i] for i in [0, 1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 13]
    ],
    'Verão': [
        Plantas[i] for i in [1, 3, 5, 6, 8, 9, 12, 13]
    ]
}

# Nutrientes utilizados e produzidos por cada planta
uso_nutrientes = {
    'Cenoura': {'Composto': +2, 'Fertilizante': -4, 'Esterco': +2},
    'Milho': {'Composto': -4, 'Fertilizante': +2, 'Esterco': +2},
    'Batata': {'Composto': +2, 'Fertilizante': +2, 'Esterco': -4},
    'Tomate': {'Composto': -2, 'Fertilizante': -2, 'Esterco': +4},
    'Berinjela': {'Composto': +2, 'Fertilizante': +2, 'Esterco': -4},
    'Fruta do Dragão': {'Composto': +4, 'Fertilizante': +4, 'Esterco': -8},
    'Pimenta': {'Composto': +4, 'Fertilizante': +4, 'Esterco': -8},
    'Abóbora': {'Composto': +2, 'Fertilizante': -4, 'Esterco': +2},
    'Cebola': {'Composto': +4, 'Fertilizante': -8, 'Esterco': +4},
    'Romã': {'Composto': +4, 'Fertilizante': -8, 'Esterco': +4},
    'Aspargo': {'Composto': -4, 'Fertilizante': +2, 'Esterco': +2},
    'Durian': {'Composto': -8, 'Fertilizante': +4, 'Esterco': +4},
    'Alho': {'Composto': -8, 'Fertilizante': +4, 'Esterco': +4},
    'Melancia': {'Composto': -2, 'Fertilizante': +4, 'Esterco': -2}
}

# Função para calcular os nutrientes necessários


def calcular_nutrientes(plantas_escolhidas):
    total = {'Composto': 0, 'Fertilizante': 0, 'Esterco': 0}

    for planta in plantas_escolhidas:
        if planta in uso_nutrientes:
            for nutriente, valor in uso_nutrientes[planta].items():
                total[nutriente] += valor

    return total

# Interface de entrada para o usuário


def main():
    while True:
        print("\n🌦️ Escolha a estação atual (ou digite 'sair' para encerrar):")
        print("🍂 Outono  ❄️ Inverno  🌸 Primavera  ☀️ Verão")

        estacao = input("\nDigite a estação: ").strip().capitalize()

        if estacao == "Sair":
            print("\n👋 Obrigado por usar a calculadora de nutrientes! "
                  "Até mais! 🌾")
            break

        if estacao not in Estacoes:
            print(
                "\n⚠️ Estação inválida. Escolha entre: Outono, Inverno, "
                "Primavera ou Verão."
            )
            continue

        plantas_disponiveis = Estacoes[estacao]

        print(f"\n🌱 Plantas disponíveis na estação {estacao}:\n")
        print(f"{'Nº':<3} {'Planta':<20} {'Composto':<10} {
              'Fertilizante':<12} {'Esterco':<8}")
        print("-" * 60)

        indices_validos = []
        for i, planta in enumerate(Plantas):
            if planta in plantas_disponiveis:
                indices_validos.append(i)
                nutrientes = uso_nutrientes[planta]
                print(
                    f"{i+1:<3} {planta:<20} {nutrientes['Composto']:<10} {
                        nutrientes['Fertilizante']:<12} "
                    f"{nutrientes['Esterco']:<8}"
                )

        escolhas = input(
            "\nDigite os números das plantas escolhidas separados por espaço "
            "(ou 'sair' para trocar de estação): "
        ).strip().lower()

        if escolhas == "sair":
            continue

        indices = [int(x) - 1 for x in escolhas.split()
                   if x.isdigit() and int(x) - 1 in indices_validos]

        if len(indices) > 3:
            print("\n⚠️ Você só pode escolher até 3 plantas.")
            continue

        plantas_escolhidas = [Plantas[i] for i in indices]

        if not plantas_escolhidas:
            print("\n⚠️ Nenhuma planta foi selecionada corretamente.")
            continue

        print(f"\n🌿 Plantas escolhidas: {', '.join(plantas_escolhidas)}")

        # Calcula os nutrientes
        resultado = calcular_nutrientes(plantas_escolhidas)

        print("\n🌾 Total de Nutrientes Necessários:")
        print(f"🟢 Composto: {resultado['Composto']}")
        print(f"🔵 Fertilizante: {resultado['Fertilizante']}")
        print(f"🟤 Esterco: {resultado['Esterco']}\n")


if __name__ == "__main__":
    main()
