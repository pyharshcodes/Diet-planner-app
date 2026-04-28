def calculate_diet(weight, goal, budget):
    calories = weight * 30

    if goal == "loss":
        calories -= 500
    elif goal == "gain":
        calories += 500

    diet = """Breakfast: Oats + Milk + Fruits
Lunch: Rice + Chicken / Paneer + Dal
Dinner: Roti + Paneer + Salad
Snack: Nuts + Shake"""

    explanation = f"This diet supports your goal of {goal} with approx {calories} kcal and fits your budget."

    return calories, diet, explanation
