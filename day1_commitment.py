# Day 1: The Commitment
import datetime

def calculate_success_date(days_needed):
    today = datetime.date.today()
    success_date = today + datetime.timedelta(days=days_needed)
    return success_date

def my_motivation():
    name = "Dashrath Manjhi"
    mountain_height = 360  # feet (symbolic)
    daily_walk_km = 8
    
    print(f"--- {name} Spirit Activated ---")
    print(f"Daily Walk: {daily_walk_km} km")
    print(f"Target: Senior SDET Role")
    
    # Calculate when the 60 days end
    end_date = calculate_success_date(60)
    print(f"I will be ready by: {end_date}")
    print("Jab tak todenge nahi, tab tak chodenge nahi!")

if __name__ == "__main__":
    my_motivation()