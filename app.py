import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Nutrimate AI Diet Planner", page_icon="🥗", layout="centered")

# ---------- TITLE ----------
st.title("🥗 Nutrimate - AI Diet Planner")
st.markdown("Get your **personalized diet plan** based on your goal and budget 💪")

# ---------- INPUTS ----------
weight = st.number_input("Enter your weight (kg)", min_value=30, max_value=200, value=60)
goal = st.selectbox("Select your goal", ["loss", "maintain", "gain"])
budget = st.number_input("Enter your daily budget (₹)", min_value=50, max_value=2000, value=200)

# ---------- FUNCTION ----------
def calculate_diet(weight, goal, budget):
    base_calories = weight * 30

    if goal == "loss":
        calories = base_calories - 400
    elif goal == "gain":
        calories = base_calories + 400
    else:
        calories = base_calories

    # Budget-based food plan
    if budget < 150:
        diet = """
🥣 Breakfast: Poha / Oats + Banana  
🍛 Lunch: Rice + Dal  
🍽 Dinner: Roti + Sabzi  
🥜 Snack: Peanuts / Chana
"""
    elif budget < 300:
        diet = """
🥣 Breakfast: Oats + Milk + Fruits  
🍛 Lunch: Rice + Dal + Paneer  
🍽 Dinner: Roti + Sabzi + Salad  
🥤 Snack: Shake / Nuts
"""
    else:
        diet = """
🥣 Breakfast: Oats + Milk + Fruits + Eggs  
🍛 Lunch: Rice + Chicken / Paneer + Dal  
🍽 Dinner: Roti + Paneer + Salad  
🥤 Snack: Protein Shake + Nuts
"""

    explanation = f"""
This diet supports your goal of **{goal}** with approx **{int(calories)} kcal/day**  
and is optimized according to your budget of ₹{budget}.
"""

    return int(calories), diet, explanation

# ---------- BUTTON ----------
if st.button("🚀 Generate My Diet Plan"):

    calories, diet, explanation = calculate_diet(weight, goal, budget)

    st.success("Your personalized plan is ready!")

    st.subheader("🔥 Daily Calories")
    st.write(f"👉 {calories} kcal")

    st.subheader("📋 Diet Plan")
    st.markdown(diet)

    st.subheader("💡 Why this plan?")
    st.markdown(explanation)

# ---------- FOOTER ----------
st.markdown("---")
st.caption("Made with ❤️ for Hackathon | Nutrimate AI")
