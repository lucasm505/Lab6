#Lab 6 encoder and main
# Camila Maldonado
#10/20/24

def encoder(password):
    #variables
    encoded_password = ""
    list_digits = []
    original_password = str(password)

    #puts all numbers in password into list to make them easily iterable
    while password > 0:
        list_digits.insert(0, password % 10)
        password = (password - password % 10) // 10
    
    #iterates through each number in password and increases by 3
    for digits in list_digits:
        encoded_password += str(digits + 3)

    return encoded_password


if __name__ == "__main__":

    while True:
        #menu
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        menu_option = int(input("Please enter an option: "))

        if menu_option == 1:
            password = input("Please enter your password to encode: ")
            encoder(int(password))
            print("Your password has been encoded and stored!\n")

        if menu_option == 2:
            pass

        if menu_option == 3:
            break