#Lab 6 encoder and main
# Camila Maldonado
#10/20/24

def encoder(password):
    #variables
    encoded_password = ""
    original_password = str(password)
    
    #iterates through each number in password and increases by 3
    for digits in (password):
        new_num = (int(digits) + 3)
        if new_num >= 10:
            new_num = (int(new_num) - 10)
        encoded_password += str(new_num)

    return encoded_password
    
def decode(encoded_password):
    decoded_pass = ''
    for digits in encoded_password:
        num = (int(digits) - 3) % 10
        decoded_pass += str(num)
    return decoded_pass

def main():
    encoded_password = ''
    while True:
        #menu
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        menu_option = int(input("Please enter an option: "))

        if menu_option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)
            print("Your password has been encoded and stored!\n")
            continue

        elif menu_option == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
            continue

        elif menu_option == 3:
            break
        
if __name__ == "__main__":
    main()
