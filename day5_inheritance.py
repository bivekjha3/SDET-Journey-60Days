# 1. THE PARENT CLASS (The "Baap")
class Employee:
    def __init__(self, name, id_card):
        self.name = name
        self.id = id_card
        self.salary = 50000 # Default salary
    
    def show_details(self):
        print(f"ID: {self.id} | Name: {self.name} | Salary: {self.salary}")

    def swipe_card(self):
        print(f"{self.name} entered the office.")

# 2. THE CHILD CLASS (The "Beta")
# Notice we put '(Employee)' inside the brackets.
# This means QA "Inherits" everything from Employee.
class QA_Engineer(Employee):
    
    # QA has a special skill that normal Employees don't have
    def report_bug(self, bug_name):
        print(f"🔴 {self.name} raised a bug: {bug_name}")

# --- Main Execution ---
if __name__ == "__main__":
    print("--- Creating a Normal Employee ---")
    manager = Employee("Ramesh", "E001")
    manager.swipe_card()
    # manager.report_bug("UI Broken") # ERROR! Manager doesn't know how to report bugs.

    print("\n--- Creating a QA Engineer ---")
    # See? We didn't write __init__ in QA, but it still works!
    # It used the Father's __init__.
    bibek = QA_Engineer("Bibek", "QA007")
    
    # 1. QA can use Father's methods
    bibek.swipe_card()   
    bibek.show_details() 

    # 2. QA can use his OWN methods
    bibek.report_bug("Login Button not working")