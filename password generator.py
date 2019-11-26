import random
import string




def function  ():

    print('please enter the values below to generate your password')

    length_password = int(input("password length?:"))
    
    pass_char = int(input('how many numbers of charcaters do you want in your password?:'))

    pass_numbers = int(input(" how many numbers do you want in your password?:"))





    pass_char_value = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase , k = pass_char))

    pass_numbers_value = ''.join(random.choices(string.digits, k = pass_numbers))




 

    result = pass_numbers_value + pass_char_value


    re = ''.join(random.sample(result,len(result)))


    if len(re) > int(length_password):
        print('*Error* The length of the password is: ' + str(length_password))
    else:
        print(re)



function()

input()




