# 1. THE PARENT CLASS (Base Logic)
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        print(f"🏦 Account Created for {self.owner} with Rs. {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited Rs. {amount}. New Balance: {self.balance}")
        else:
            print("❌ Error: Deposit amount must be positive.")

    # Generic Withdraw (Will be overridden by Children)
    def withdraw(self, amount):
        print("Processing withdrawal...")

# 2. THE CHILD CLASS (Savings - Strict Rules)
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        try:
            # Rule: Cannot withdraw if balance falls below 500
            if (self.balance - amount) < 500:
                # We raise an error manually!
                raise ValueError("Insufficient Funds! Min balance 500 required.")
            
            self.balance -= amount
            print(f"💸 Withdrawn Rs. {amount}. Remaining: {self.balance}")
            
        except ValueError as e:
            # Catch the error and show a nice message
            print(f"⚠️ Transaction Failed: {e}")

# 3. THE CHILD CLASS (Current - Loose Rules)
class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        # Current account has a fee of Rs 10 per withdrawal
        fee = 10
        total_deduction = amount + fee
        
        if self.balance >= total_deduction:
            self.balance -= total_deduction
            print(f"💸 Withdrawn Rs. {amount} (Fee: Rs. {fee}). Remaining: {self.balance}")
        else:
            print("❌ Insufficient Funds for withdrawal + fee.")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    print("--- SCENARIO 1: SAVINGS ACCOUNT (Bibek) ---")
    bibek_acc = SavingsAccount("Bibek", 2000)
    bibek_acc.deposit(500)
    bibek_acc.withdraw(1000) # Should work
    bibek_acc.withdraw(2000) # Should FAIL (Balance would go below 500)

    print("\n--- SCENARIO 2: CURRENT ACCOUNT (Office) ---")
    office_acc = CurrentAccount("Office Admin", 5000)
    office_acc.withdraw(1000) # Should deduct 1010 (1000 + 10 fee)