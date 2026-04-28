def calculate_diet(weight, goal, budget):
    
    # Calories logic
    if goal == "loss":
        calories = weight * 25
    elif goal == "maintain":
        calories = weight * 30
    else:
        calories = weight * 35

    # Diet plan
    if budget <= 150:
        diet = """
Breakfast: Oats + Milk + Banana
Lunch: Rice + Dal + 2 Eggs
Dinner: Roti + Soy chunks / Paneer
Snack: Peanuts
"""
    else:
        diet = """
Breakfast: Oats + Milk + Fruits
Lunch: Rice + Chicken / Paneer + Dal
Dinner: Roti + Paneer + Salad
Snack: Nuts + Shake
"""

    explanation = f"This diet supports your goal of {goal} with approx {calories} kcal and fits your budget."

    return calories, diet, explanation


# --- USER INPUT ---
weight = float(input("Enter your weight (kg): "))
goal = input("Enter goal (loss / maintain / gain): ").lower()
budget = int(input("Enter your daily budget (₹): "))

# --- OUTPUT ---
calories, diet, explanation = calculate_diet(weight, goal, budget)

print("\n🔥 YOUR PLAN")
print(f"Calories needed: {calories} kcal")

print("\n🍽️ DIET PLAN:")
print(diet)

print("\n🧠 WHY THIS DIET?")
print(explanation)