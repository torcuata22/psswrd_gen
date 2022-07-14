import random
import array

#strong password generator: 12 character password using letters, numbers, and symbols
def password_gen(max_length):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lcase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
    ucase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
    symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
    char_list = digits + lcase + ucase + symbols
    rand_digits = random.choice(digits)
    rand_lcase = random.choice(lcase)
    rand_ucase = random.choice(ucase)
    rand_symbols = random.choice(symbols)
    temp = rand_digits + rand_lcase + rand_ucase + rand_symbols #temporary password with 4 characters, so as I generate the rest, I need to substract 4
    
    for x in range(max_length - 4):
        temp = temp + random.choice(char_list)    
        temp_list = array.array('u', temp)
        random.shuffle(temp_list)
        password = ""
    for x in temp_list:
        password = password + x
        
    print("your password is: " + password)
    
password_gen(8)
            


