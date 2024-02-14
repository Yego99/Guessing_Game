import random
rn = random.randint(1,10)

print('I am thinking of a number between 1 and 10; enter a number to see if you guessed it right:')
while True:
    try:
        guess = int(input(''))
        if (guess != rn and (0<guess<11)):
            print('Good guess, not quite. Try again:')
        if guess == rn:
            print('OMG you guessed it!! Great job you win!!!!')
            break
        if guess>=11 or guess<=0:
            print('Bro I said between 1 and 10')
    except ValueError:
        print('Enter a number bozo')