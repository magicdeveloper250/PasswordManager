import string 
import random
import cryptocode

upper_case= list(string.ascii_uppercase)
lower_case= list(string.ascii_lowercase)
digits=list(string.digits)
punctuations= list(string.punctuation)
 

def generate_complex_password():
    global upper_case,lower_case,digits,punctuations
    random_upper_case=random.sample(upper_case, k=random.randint(3,len(lower_case)))
    random_lower_case= random.sample(lower_case, k= random.randint(3,len(upper_case)))
    random_digits= random.sample(digits, k=random.randint(3,len(digits)))
    random_punctuations= random.sample(punctuations, k= random.randint(3,len(punctuations)))
    random_password=random_upper_case+random_lower_case+random_digits+random_punctuations
    random.shuffle(random_password)
    complex_password="".join(random_password)
    
    return complex_password

 
def decrypt_generated_password(password, key ):
    decrypted_password=cryptocode.decrypt(password, key)
    return decrypted_password
def __test():
    
    password=generate_complex_password("kigali")
    decrypted=decrypt_generated_password( password, "kigali")
    print("password: ",password)
    print()
    print("encrypted: ",password)
    print()
    print("decrypted:", decrypted)
if __name__=="__main__":
    __test()

# Impano Manzi Enock
