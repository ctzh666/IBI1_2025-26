class food_item:
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = float(calories)
        self.protein = float(protein)
        self.carbs = float(carbs)
        self.fat = float(fat)
def daily_intake(food_list):
    total_calories = 0.0
    total_protein = 0.0
    total_carbs = 0.0
    total_fat = 0.0
    for item in food_list:
        total_calories += item.calories
        total_protein += item.protein
        total_carbs += item.carbs
        total_fat += item.fat
    if total_calories > 2500:
        print(f"calories:({total_calories:.1f} kcal)more than 2500 kcal")
    if total_fat > 90:
        print(f"fat:({total_fat:.1f} g)more than 90 g")
    return {
        'total_calories': total_calories,
        'total_protein': total_protein,
        'total_carbs': total_carbs,
        'total_fat': total_fat
    }
apple = food_item("Apple", 60, 0.3, 15, 0.5)
ice_cream = food_item("Ice Cream", 350, 5, 40, 20)
burger = food_item("Burger", 500, 25, 35, 25)
todays_food = [apple,ice_cream,burger,burger,burger,burger,burger]
totals = daily_intake(todays_food)
print("\ntotal:")
for key, value in totals.items():
     print(f"{key}: {value:.1f}")