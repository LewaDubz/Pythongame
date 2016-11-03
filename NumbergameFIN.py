import random
print("Welcome to the number guess game! \n In this game i think of a number between 2 values and your task is to guess this number,if you guessed correctly,you level up,but if you guess wrong you lose a life,in each turn you get 5 lives to begin with,after every level  the range of the numbers increase.\n Let the game begin")
running=True
gamerlevel=1
lifes=5
pcnumber=random.randint(0,10*gamerlevel)
print("The number i have thought of is between 0 and",(10*gamerlevel))
while running==True:
    gamerinputraw=(raw_input("Please guess a number"))
    print("You have",lifes,"lives left")
    if gamerinputraw.isdigit():
        gamerinput=int(gamerinputraw)
        if gamerinput<pcnumber and gamerinput<=10*gamerlevel and 0<=gamerinput:
            print("Your answer is too small")
            lifes+=-1
        if pcnumber<gamerinput and 0<=gamerinput and gamerinput<=10*gamerlevel:
            print("Your answer is too big")
            lifes+=-1
        if gamerinput<0 or 10*gamerlevel<gamerinput:
            print("The number you have entered is out of range")
        if pcnumber==gamerinput:
            print("Your answer is correct")
            lifes=5
            gamerlevel+=1
            pcnumber=random.randint(0,10*gamerlevel)
            print("The number i have thought of is between 0 and",(10*gamerlevel))
        if lifes==0:
            print("You have lost,Game Over!")
            quit()
    if gamerinputraw.isalpha():
        print("Wrong input")