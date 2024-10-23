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
        var = 0
        var += (digits + 3)
        if var > 10:
            var -= 10
        encoded_password += str(var)

    return encoded_password
    
def decode(encoded_password):
    decoded_pass = ''
    for digits in encoded_password:
        decoded_pass += str(int(digits) - 3)
    return decoded_pass
        
    

def main():
    encoded_password = ''
    while True:
        #menu
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        menu_option = int(input("Please enter an option: "))

        if menu_option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(int(password))
            print("Your password has been encoded and stored!\n")

        elif menu_option == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")

        elif menu_option == 3:
            break
        
if __name__ == "__main__":
    main()
