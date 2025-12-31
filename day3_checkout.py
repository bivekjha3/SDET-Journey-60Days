def calculate_total_bill(*items, **details):
    # *items = A list of items (Tuples) passed as arguments
    # **details = Key-Value pairs for extra info (Tax, Discount)
    
    market_prices = {
        "Rice": 100,
        "Dal": 150,
        "Oil": 200
    }
    
    total = 0
    print(f"--- Invoice for {details.get('customer_name', 'Guest')} ---")
    
    for item, quantity in items:
        try:
            # TRY to find the price
            if quantity < 0:
                raise ValueError("Quantity cannot be negative!")
                
            price = market_prices[item] # This might fail if item is not in dict
            cost = price * quantity
            total += cost
            print(f"Added: {item} ({quantity} kg) = {cost}")
            
        except KeyError:
            # HANDLE the missing item error
            print(f"⚠️  ALERT: '{item}' is not available in the market today.")
        except ValueError as ve:
            # HANDLE negative quantity
            print(f"❌ ERROR: {ve} for item '{item}'")
            
    # Apply Discount if provided in **kwargs
    if 'discount_percent' in details:
        disc = details['discount_percent']
        discount_amount = (total * disc) / 100
        total -= discount_amount
        print(f"Discount Applied: {disc}% (-{discount_amount})")
        
    print(f"Total To Pay: Rs. {total}")
    print("--------------------------------")

if __name__ == "__main__":
    # Scenario 1: Happy Path
    calculate_total_bill(("Rice", 2), ("Dal", 1), customer_name="Manjhi")
    
    # Scenario 2: Error Path (Item missing + Negative Quantity)
    # Notice: The code will NOT crash. It will handle 'Ghee' and continue.
    print("\n--- Running Second Test Case ---")
    calculate_total_bill(
        ("Rice", 2), 
        ("Ghee", 1), # Missing item
        ("Oil", -5), # Invalid Quantity
        customer_name="Ramesh", 
        discount_percent=10
    )