import re

# Function to assess password strength
def assess_password_strength(password):
    strength_criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"\d", password)),
        "special_char": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)),
    }
    
    # Calculate strength score
    strength_score = sum(strength_criteria.values())

    # Provide feedback to the user
    if strength_score == 5:
        feedback = "Strong password"
    elif strength_score >= 3:
        feedback = "Medium password, consider adding more complexity."
    else:
        feedback = "Weak password, you should improve the following:\n"
        if not strength_criteria["length"]:
            feedback += "- Increase length (at least 8 characters)\n"
        if not strength_criteria["uppercase"]:
            feedback += "- Add at least one uppercase letter\n"
        if not strength_criteria["lowercase"]:
            feedback += "- Add at least one lowercase letter\n"
        if not strength_criteria["digit"]:
            feedback += "- Add at least one digit\n"
        if not strength_criteria["special_char"]:
            feedback += "- Add at least one special character\n"

    return feedback

# Main function to handle user input
def main():
    password = input("Enter a password to assess its strength: ")
    feedback = assess_password_strength(password)
    print(feedback)

if __name__ == "__main__":
    main()


