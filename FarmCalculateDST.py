# List of plants
Plants = ['Carrot', 'Corn', 'Potato', 'Toma Root', 'Eggplant', 'Dragon Fruit',
          'Pepper', 'Pumpkin', 'Onion', 'Pomegranate', 'Aspargus', 'Durian',
          'Garlic', 'Watermelon',]

# Defining the seasons and their respective plants
Seasons = {
    'Autumn': [Plants[i] for i in [0, 1, 2, 3, 4, 6, 7, 8]],
    'Winter': [Plants[i] for i in [0, 2, 7, 10, 12]],
    'Spring': [Plants[i] for i in [0, 1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 13]],
    'Summer': [Plants[i] for i in [1, 3, 5, 6, 8, 9, 12, 13]]
}

# Nutrients per plant (Consumption and Production)
nutrient_usage = {
    'Carrot': {'Compost': +2, 'Formula': -4, 'Manure': +2},
    'Corn': {'Compost': -4, 'Formula': +2, 'Manure': +2},
    'Potato': {'Compost': +2, 'Formula': +2, 'Manure': -4},
    'Toma Root': {'Compost': -2, 'Formula': -2, 'Manure': +4},
    'Eggplant': {'Compost': +2, 'Formula': +2, 'Manure': -4},
    'Dragon Fruit': {'Compost': +4, 'Formula': +4, 'Manure': -8},
    'Pepper': {'Compost': +4, 'Formula': +4, 'Manure': -8},
    'Pumpkin': {'Compost': +2, 'Formula': -4, 'Manure': +2},
    'Onion': {'Compost': +4, 'Formula': -8, 'Manure': +4},
    'Pomegranate': {'Compost': +4, 'Formula': -8, 'Manure': +4},
    'Aspargus': {'Compost': -4, 'Formula': +2, 'Manure': +2},
    'Durian': {'Compost': -8, 'Formula': +4, 'Manure': +4},
    'Garlic': {'Compost': -8, 'Formula': +4, 'Manure': +4},
    'Watermelon': {'Compost': -2, 'Formula': +4, 'Manure': -2}
}

# Function to calculate required nutrients


def calculate_nutrients(selected_plants):
    total = {'Compost': 0, 'Formula': 0, 'Manure': 0}

    for plant in selected_plants:
        if plant in nutrient_usage:
            for nutrient, value in nutrient_usage[plant].items():
                total[nutrient] += value

    return total

# User interface function


def main():
    while True:
        print("\n🌦️ Select the current season (or type 'exit' to quit):")
        print("🍂 Autumn  ❄️ Winter  🌸 Spring  ☀️ Summer")

        season = input("\nEnter the season: ").strip().capitalize()

        if season == "Exit":
            print("\n👋 Thank you for using the nutrient calculator! "
                  "See you next time! 🌾")
            break

        if season not in Seasons:
            print(
                "\n⚠️ Invalid season. Please choose from: "
                "Autumn, Winter, Spring, or Summer."
            )
            continue

        available_plants = Seasons[season]

        print(f"\n🌱 Available plants in {season}:\n")
        print(f"{'No.':<3} {'Plant':<15} {'Compost':<8} {
              'Formula':<8} {'Manure':<8}")
        print("-" * 50)

        valid_indices = []
        for i, plant in enumerate(Plants):
            if plant in available_plants:
                valid_indices.append(i)
                nutrients = nutrient_usage[plant]
                print(f"{i+1:<3} {plant:<15} {nutrients['Compost']:<8} {
                      nutrients['Formula']:<8} {nutrients['Manure']:<8}")

        choices = input(
            "\nEnter the numbers of the selected plants "
            "(or 'exit' to change the season): "
        ).strip().lower()

        if choices == "exit":
            continue

        indices = [int(x) - 1 for x in choices.split()
                   if x.isdigit() and int(x) - 1 in valid_indices]

        if len(indices) > 3:
            print("\n⚠️ You can only select up to 3 plants.")
            continue

        selected_plants = [Plants[i] for i in indices]

        if not selected_plants:
            print("\n⚠️ No plants were selected correctly.")
            continue

        print(f"\n🌿 Selected plants: {', '.join(selected_plants)}")

        # Calculate the required nutrients
        result = calculate_nutrients(selected_plants)

        print("\n🌾 Total Required Nutrients:")
        print(f"🟢 Compost: {result['Compost']}")
        print(f"🔵 Formula: {result['Formula']}")
        print(f"🟤 Manure: {result['Manure']}\n")


if __name__ == "__main__":
    main()
