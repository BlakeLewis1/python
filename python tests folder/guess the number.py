import random
name = input("enter your name")
num = random.randint(0,10)
number = True
attempts = 5

while number == True:
    
    guess=int(input(name.upper()+ " enter a number"))
    if guess < num:
        print(name.upper() + " The guess is higher than the number")
        number = True
        attempts = -1
        
    elif guess > num:
        print("its lower ,  my g fam ")
        number = True
        attempts = -1
        
    else:
        print("you smart")
        number = False
            
            
        


    


