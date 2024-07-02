import re

#Method Overloading --(Same method name but different input params)
def check_password_validation(password):

    # Check the password length > 8
    if len(password) < 8:
        return False

    # Check if the password contains both uppercase and lowercase letters
    if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password):
        return False
    
    # Check if the password contains at least one digit
    if not re.search(r'\d', password):
        return False
    
    # Check if the password contains at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    # If all conditions are met, return True
    return True

def check_password_strength(password):
    # Criteria for a strong password
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r"[a-z]", password) is not None
    uppercase_criteria = re.search(r"[A-Z]", password) is not None
    digit_criteria = re.search(r"[0-9]", password) is not None
    special_char_criteria = re.search(r"[\W_]", password) is not None
    
    # Check all criteria
    if length_criteria and lowercase_criteria and uppercase_criteria and digit_criteria and special_char_criteria:
        return "Strong"
    elif length_criteria and (lowercase_criteria or uppercase_criteria) and digit_criteria:
        return "Moderate"
    else:
        return "Weak"

# Example usage
password = "" #Write logic to have input from user
password = input("Enter Password : ")
isValid = check_password_validation(password)

if isValid:
    password_strength = check_password_strength(password)
    print(f"The given password {password} is {password_strength}")
else:
    print("Password doesn't meet the criteria / Invalid pasword")
    



