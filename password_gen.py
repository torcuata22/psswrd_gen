import random
import array
import re 

#strong password generator: 12 character password using letters, numbers, and symbols
#After generating the password, determine if the generated password is strong or weak, and if weak,return reason it is weak
#Strong password: between 9 and 20 characters, no spaces, no more than 3 repeated chars, no string pattern should be repeated
#need to import re (Regex) for this
 
def password_gen(max_length=input("Enter the desired length of your password: ")):
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
    
    for x in range(int(max_length) - 4):
        temp = temp + random.choice(char_list)    
        temp_list = array.array('u', temp)
        random.shuffle(temp_list)
        password = ""
    for x in temp_list:
        password = password + x
    
    print("your password is: " + password)

    def strong_password(password):
        
        if 9<= len(password) <=20:
            if re.search(r'(.)\1\1', password):
                print ("Weak password: the same character repeats three or more times")
            if re.search(r'(..)(.*?)\1', password):
                print ("Weak password: Pattern repetition")
            else:
                print ("This is a strong password!")
        else:
            print ("Your password must be between 9 and 20 characters")
    
    strong_password(password)
    
password_gen()





    

            


