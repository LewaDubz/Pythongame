import random
print("Welcome to the number guess game! \nIn this game i think of a number between 2 values and your task is to guess this number,if you guessed correctly,you level up,but if you guess wrong you lose a life,\nin each turn you get 5 lives to begin with,after every level the range of the numbers increase.\nLet the game begin \n")
playername=raw_input("Please enter your name\n")
print('Welcome',playername,'Good Luck and have fun')
running=True
gamerlevel=1
lifes=5
bonuslife=0
pcnumber=random.randint(0,10*gamerlevel)
highscore=0
while running==True:
    print("The number i have thought of is between 0 and",(10*gamerlevel))
    print('You have',lifes,'lives left')
        
    if pcnumber%2==0 and pcnumber%3!=0:
            print('This number is dividable by 2')

    if pcnumber%3==0 and pcnumber%2!=0:
            print('This number is dividable by 3')

    if pcnumber%3==0 and pcnumber%2==0:
        print('This number is dividable by 2 and 3')

    gamerinputraw=(raw_input("Please guess a number \n"))
    
    if gamerinputraw.isdigit():
        gamerinput=int(gamerinputraw)
       
        if gamerinput<pcnumber and gamerinput<=10*gamerlevel and 0<=gamerinput:
            print('Your answer is too small\n')
            lifes+=-1
       
        if pcnumber<gamerinput and 0<=gamerinput and gamerinput<=10*gamerlevel:
            print('Your answer is too big\n')
            lifes+=-1
       
        if gamerinput<0 or 10*gamerlevel<gamerinput:
            print('The number you have entered is out of range')
       
        if pcnumber==gamerinput:
            print('Correct\n')
            gamerlevel+=1

            if gamerlevel%5==0:
                bonuslife+=1
                print("Congratulations you get a bonus life")

            if 3<=bonuslife:
                bonuslife=3
            
            lifes=5+bonuslife
            pcnumber=random.randint(0,10*gamerlevel)
            highscore=gamerlevel-1
       
        if lifes==0 or lifes<=0:
            print('You have lost,Game Over!')
            print(playername,'You have reached',highscore,'points')
            loss=1
            running=False
            if loss==1 and running==False:
                print("Do yo wanna play again?")
                restart=raw_input("Yes/No\n")
                if restart=='Yes' or restart=='yes':
                    loss=0
                    running=True
                    lifes=5
                    gamerlevel=1
                    pcnumber=random.randint(0,10*gamerlevel)

                if restart=='No'or restart=='no':
                    print("\nGoodbye",playername,"!")
                    quit()

    if gamerinputraw.isalpha():
        print('Wrong input')