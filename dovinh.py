import random
import string
#used to generate random characters for passwords.
# Taomatkhau, which is Vietnamese for "PasswordGenerator".
class TaoMatKhau:
    def __init__(tao_matkhau):
            # Initialize the characters and password attributes
        tao_matkhau.characters = ''
        tao_matkhau.matkhau = ''
    def thuthapyeucau(tao_matkhau, use_upper, use_lower, use_digits, use_special):
            # Generate character set based on user preferences
        """
        use_upper: A boolean variable (True or False) indicating whether the password should contain uppercase characters or not.
use_lower: A boolean variable indicating whether the password should contain lowercase characters or not.
use_digits: A boolean variable indicating whether the password should contain digits or not.
use_special: A boolean variable indicating whether the password should contain special characters or not.
        """
        if use_upper:
            tao_matkhau.characters += string.ascii_uppercase
        if use_lower:
            tao_matkhau.characters += string.ascii_lowercase
        if use_digits:
            tao_matkhau.characters += string.digits
        if use_special:
            tao_matkhau.characters += string.punctuation
        
         # Check if at least one of each type of character is included
        if not all([use_upper, use_lower, use_digits, use_special]):
            raise ValueError("Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
        # Check if character set is long enough
        if len(tao_matkhau.characters) < 8:
            raise ValueError("Password must contain at least 8 characters.")
    def introduce_matkhau(tao_matkhau):
       # Provide guidance on creating a strong password
        print("Please choose a strong password.")
        print("A strong password should contain at least 8 characters, including uppercase letters, lowercase letters, numbers, and special characters.")

    def suggest_similar_matkhau(tao_matkhau, matkhau):
        # Generate a similar strong password suggestion
        similar_matkhau = matkhau
        while len(similar_matkhau) < 8 or not all(char in tao_matkhau.characters for char in similar_matkhau):
            similar_matkhau += random.choice(tao_matkhau.characters)
        return similar_matkhau

    def analyze_requirements(tao_matkhau):
        # Request user input for password and suggest a similar strong password if input is not strong enough
        while True:
            tao_matkhau.matkhau = input("Enter password: ")
            if len(tao_matkhau.matkhau) < 8 or not all(char in tao_matkhau.characters for char in tao_matkhau.matkhau):
                print("Password is not strong enough or invalid.")
                similar_matkhau = tao_matkhau.suggest_similar_matkhau(tao_matkhau.matkhau)
                print("Similar strong password suggestion:", similar_matkhau)
            else:
                break
    def design_matkhau(tao_matkhau):
        # Return the designed password
        return tao_matkhau.matkhau
    def implement_matkhau(tao_matkhau):
        # Return the implemented password
        return tao_matkhau.matkhau

    def test_matkhau(tao_matkhau):
        # Return the tested password
        return tao_matkhau.matkhau

    def deploy_matkhau(tao_matkhau):
        # Return the deployed password
        return tao_matkhau.matkhau
if __name__ == "__main__":
    tao_mat_khau = TaoMatKhau()
    
    # Collect requirements for the password
    use_upper = True
    use_lower = True
    use_digits = True
    use_special = True
    tao_mat_khau.thuthapyeucau(use_upper, use_lower, use_digits, use_special)

    # Introduce password and request user input
    tao_mat_khau.introduce_matkhau()

    # Request user input for password and suggest similar password if not strong enough
    tao_mat_khau.analyze_requirements()

    # Design password
    matkhau = tao_mat_khau.design_matkhau()

    # Implement password
    implemented_matkhau = tao_mat_khau.implement_matkhau()

    # Test password
    tested_matkhau = tao_mat_khau.test_matkhau()

    # Deploy password
    deployed_matkhau = tao_mat_khau.deploy_matkhau()

    # Print the generated password
    print("Generated password:", matkhau)
