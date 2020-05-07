#SAYI TAHMİN OYUNU
import random

number = random.randint(1,10)
can = int(input('how many lifes do you want??'))
life = can
sayac = 0

while life >0:
    life -= 1
    sayac += 1
    guess = int(input("Enter your guess (1,100): "))
    if number==guess:
        print(f'TRUE {sayac}. times. Points: {100-(100/can)*(sayac-1)}')
        break
    elif number< guess:
        print("down")
    elif number > guess:
        print("up")
    if life == 0:
        print(f'Hakkınız bitt. Tutulan sayı: {number}')



