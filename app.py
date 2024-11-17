#User input as Constant - About to change based on each user input 

user_name = "Nadia"
user_age = 21
period_start = "2024-11-05"  # Format: YYYY-MM-DD
period_end = "2024-11-12"
today_date = "2024-11-16"  # Simulate current date

#Now calculate the Menstrual phase based on the user input, the end date 

from datetime import datetime, timedelta


def determine_phase(period_start,period_end_date, today_date):

    # Convert string dates to datetime objects
    period_start_date = datetime.strptime(period_start, "%Y-%m-%d")
    period_end_date = datetime.strptime(period_end, "%Y-%m-%d")
    today_date_obj = datetime.strptime(today_date, "%Y-%m-%d")
    
    # Calculate phase start and end dates
    follicular_start = period_end_date + timedelta(days=1)
    follicular_end = follicular_start + timedelta(days=6)
    
    ovulation_start = follicular_end + timedelta(days=1)
    ovulation_end = ovulation_start + timedelta(days=5)
    
    luteal_start = ovulation_end + timedelta(days=1)
    next_period_start = luteal_start + timedelta(days=13)  # Approx. cycle reset
    
    # Determine the current phase
    if period_start_date <= today_date_obj <= period_end_date:
        return "Menstrual Phase"
    elif follicular_start <= today_date_obj <= follicular_end:
        return "Follicular Phase"
    elif ovulation_start <= today_date_obj <= ovulation_end:
        return "Ovulation Phase"
    elif luteal_start <= today_date_obj < next_period_start:
        return "Luteal Phase"
    else:
        return "Unknown Phase (possibly irregular cycle)"

# Test function
phase = determine_phase(period_start, period_end, today_date)
print(f"Current menstrual phase: {phase}")

recommendations = {
    "Follicular Phase": {
        "food": ["Cruciferous vegetables, such as broccoli, cauliflower, cabbage and kale","Fermented foods, such as kombucha, sauerkraut and kimchi",
"Healthy fats, such as avocados, flaxseeds and pumpkin seeds","Leafy greens"],
        "exercise": ["Cardio", "Running","Swimming"],
        "description": "Choose foods to support your increased energy levels. Lean proteins and complex carbohydrates, such as whole wheat, brown rice and quinoa, will fuel higher-intensity workouts."
    },
    "Ovulation Phase": {
        "description": "During the Ovulation Phase, your energy levels peak. Focus on foods rich in antioxidants and healthy fats, and engage in high-intensity exercises for maximum performance.",
        "food": ["Cruciferous vegetable (Broccoli and cauliflower)", "Flax seeds","Berries", "Leafy Greens", 
                 "Nuts: Almonds and walnuts","Seeds: Pumpkin, sesame, sunflower seeds"],
        "food to limit": "Processed foods, refined sugar, and red meat.",
        "exercise": ["High-intensity interval training (HIIT) such as workouts such as: Boot camp, Kickboxing and Spinning."],
        
    },
    "Luteal Phase": {
        "food": ["Craving sweet or salty snacks", "Pumpkin seeds", "Fruits (bananas, berries, pineapple)",
"Nuts (Almonds, Pistachios, and Brazil nuts)",
"Seeds (sunflower, and sesame seeds)"],
        "Medium-intensity cardio such as": ["dance", "jogging", "skipping", "hiking", "riding a bike", "Walking"],
        "Medium-intensity strength such as": ["forearm planks", "Weight training increasing the time spent in each exercise over time"],
        "description": "In the Luteal Phase, your body benefits from comforting foods that stabilize mood and energy. Engage in gentle, low-impact exercises to support recovery.This phase usually brings on PMS, hunger and cravings. "
    },
    "Menstrual Phase": {
        "food": ["Warm soups", "Iron-rich foods like spinach and lentils", "Ginger tea"],
        "exercise": ["Restorative yoga", "Light stretching"],
        "description": "During the Menstrual Phase, your body needs extra care. Focus on iron-rich and hydrating foods while prioritizing rest and light movement."
    }
}

if phase in recommendations:
    food = recommendations[phase]["food"]
    exercise = recommendations[phase]["exercise"]
    print(f"Recommended food: {food}")
    print(f"Recommended exercise: {exercise}")
else:
    print("No recommendations available for the current phase.")


