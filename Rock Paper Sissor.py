import random
#imports random function from library

def function():

    while( user_option != 'rock' or user_option != 'paper' or user_option != 'sissor' ):
        
        
        print( "~~~ROCK PAPER SISSOR ONLY~~~" )

            
		
        user = input()
            
        

        if user == 'rock' or user == 'paper' or user == 'sissor':
            print("")
            print("")
            
            print("Okay now you're good")
            

     
            print("")
            print("")
            print("")
            print("")

    
            print('computer chooses: '+(computer_option))
    


        if computer_option == 'rock' and user == 'rock' or computer_option == 'sissor' and user == 'sissor' or computer_option == 'paper' and user == 'paper':

            print("it's a tie")
            input()
            break
        
        if computer_option == 'rock' and user == 'paper':

            break
            input()
            print("you win")
        
        if computer_option == 'rock' and user == 'sissor':

            print("you lose")
            input()
            break
            
        if computer_option == 'paper' and user == 'rock':

            print("you lose")
            input()
            break
            
        if computer_option == 'paper' and user == 'sissor':

            print("you win")
            input()
            break
    
            
        if computer_option == 'sissor' and user == 'rock':
            print("you win")
            input()
            break
        
        if computer_option == 'sissor' and user == 'paper':

            print("you lose")    
            input()
            break
        

option = ["rock","sissor","paper"]

#Array of the list

computer_option = random.choice(option)

#generates random selection from array

print('choose rock, paper, or sissor only.')

#prints statment

user_option = str(input())

#Enter's data into the variable

if user_option == 'rock' or user_option == 'paper' or user_option == 'sissor':

#creates condition if the required data is correct

    print("Good job")
    print("")
    print("")
    print("")
    print("")

    
    print('computer chooses: '+(computer_option))
    


    if computer_option == 'rock' and user_option == 'rock' or computer_option == 'sissor' and user_option == 'sissor' or computer_option == 'paper' and user_option == 'paper':
        input()
        print("it's a tie")

    if computer_option == 'rock' and user_option == 'paper':
        input()
        print("you win")
        
    if computer_option == 'rock' and user_option == 'sissor':
        input()
        print("you lose")

    if computer_option == 'paper' and user_option == 'rock':
        input()
        print("you lose")

    if computer_option == 'paper' and user_option == 'sissor':
        input()
        print("you win")

    if computer_option == 'sissor' and user_option == 'rock':
        input()
        print("you win")
        
    if computer_option == 'sissor' and user_option == 'paper':
        input()
        print("you lose")    
    
    
#When computer chooses rock







    

elif user_option != 'rock' or user_option != 'paper' or user_option != 'sissor':

#creates condition if the required data is not correct run the function below
    
    function()













    
