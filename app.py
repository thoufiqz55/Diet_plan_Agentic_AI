import google.generativeai as genai

# --- CONFIGURE YOUR GEMINI API KEY ---
genai.configure(api_key="AIzaSyB4cROBXK8AL7-gIcigNFA7olrCOBtXleM")  # Replace with your actual key

# --- LOAD THE GEMINI MODEL ---
model = genai.GenerativeModel("gemini-2.5-flash-preview-05-20")

# --- COLLECT USER INPUTS ---
def collect_user_data():
    print("👋 Welcome to NutriBot – Your Personalized Diet Planner\n")

    name = input("Enter your name: ")
    age = input("Enter your age: ")
    gender = input("Enter your gender (Male/Female/Other): ")
    interests = input("What type of food do you like? (e.g., South Indian, Vegetarian, Keto): ")
    allergies = input("Any food allergies? (comma-separated): ")
    activity = input("Your daily activity level (Sedentary/Moderate/Active): ")
    calories = input("Your average required calories per day (leave blank to auto-calculate): ")

    return {
        "name": name,
        "age": age,
        "gender": gender,
        "interests": interests,
        "allergies": allergies,
        "activity": activity,
        "calories": calories if calories else "Estimate based on average need"
    }

# --- GENERATE PROMPT FOR GEMINI ---
def build_prompt(user):
    return f"""
You are a smart and caring AI nutritionist. Prepare a one-day nutritious meal plan based on the following user profile:

- Name: {user['name']}
- Age: {user['age']}
- Gender: {user['gender']}
- Food Preferences: {user['interests']}
- Food Allergies: {user['allergies']}
- Activity Level: {user['activity']}
- Required Calories per Day: {user['calories']}

Instructions:
- Provide meals for breakfast, lunch, and dinner.
- Ensure meals are healthy, balanced, and avoid any allergens.
- Mention estimated calories for each meal and total.
- Present the result in a neat, user-friendly format.
"""

# --- MAIN FUNCTION ---
def main():
    user_data = collect_user_data()
    prompt = build_prompt(user_data)

    print("\n🧠 Generating your personalized diet plan. Please wait...\n")
    response = model.generate_content(prompt)
    
    print("📋 Your Personalized Diet Plan:\n")
    print(response.text)

# --- EXECUTE SCRIPT ---
if __name__ == "__main__":
    main()

