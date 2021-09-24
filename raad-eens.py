import random

ronden=0
score=0
hoge=1000
lage=1

while round < 20:
    ronden+=1
    count=0
    num=random.randint(lage, hoge)
    print ("ronden", ronden)
    if ronden<19:
        print("wil je nog een keer raden?")
    while count <10:
        count +=1
        guess = int(input("gok een nummer: "))
        if num == guess:
            print("je hebt", count," keer gegokt voordat je het goed had geraden! je scoren: ",score)
        elif num > guess:
            print("je hebt te laag gegokt")
        elif num > guess:
            print("je hebt te hoog gegokt")
    if count >= 10:
        print("het nummer is ", num)
        print("jammer je had te veel gegokt, probeer het nog een keer")