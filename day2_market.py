def analyze_market_trip():
    # 1. This Dictionary represents an API Response (like from a Cart API)
    # Key = Item Name, Value = Price per kg
    market_prices = {
        "Tomato": 40,
        "Potato": 30,
        "Onion": 60,
        "Garlic": 120
    }

    # 2. This List represents what you actually bought
    # A List of Tuples: (Item, Kg)
    my_shopping_bag = [
        ("Tomato", 1.5),
        ("Potato", 2.0),
        ("Onion", 0.5)
    ]

    print("--- User Shopping Bill ---")
    
    total_cost = 0

    # 3. The Logic Loop (Iterating through Data)
    for item, weight in my_shopping_bag:
        if item in market_prices:
            price_per_kg = market_prices[item]
            cost = price_per_kg * weight
            total_cost += cost
            print(f"Bought {weight}kg of {item} @ {price_per_kg}/kg = Rs. {cost}")
        else:
            print(f"Error: {item} not found in market!")

    print("--------------------------")
    print(f"Total Expense: Rs. {total_cost}")

    # 4. Senior Logic: Finding the most expensive vegetable in the market
    # Using 'max' with a key (Lambda function)
    most_expensive = max(market_prices, key=market_prices.get)
    print(f"Most expensive item in market today: {most_expensive}")

if __name__ == "__main__":
    analyze_market_trip()