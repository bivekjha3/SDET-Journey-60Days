import pytest

# 1. A Simple Function (Not a test, just logic)
def calculate_bonus(salary):
    return salary * 0.10  # 10% Bonus

# 2. The Test Case (Must start with 'test_')
def test_calculate_bonus_correctly():
    salary = 50000
    expected_bonus = 5000
    
    # Calculate actual result
    actual_bonus = calculate_bonus(salary)
    
    # The Assertion (The Judge)
    # If this is True -> Green Tick (PASS)
    # If this is False -> Red Cross (FAIL)
    assert actual_bonus == expected_bonus

# 3. A Failing Test (To see what happens)
def test_calculate_bonus_wrongly():
    salary = 50000
    wrong_expectation = 6000 # This is wrong!
    
    actual_bonus = calculate_bonus(salary)
    
    # This will FAIL and Pytest will tell you WHY
    assert actual_bonus == wrong_expectation