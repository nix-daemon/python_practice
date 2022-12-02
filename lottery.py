from random import choice

i = 0
l = 0
win = 0
winner = []
my_ticket = ['a', 'p', 4, 48]

lottery_pool = ['a', 't', 'p', 'w','l', 13, 4, 48, 62, 857, 0, 56, 3, 5, 9]

while winner != my_ticket:
    if i < 4:
        winner.append(choice(lottery_pool))
        i += 1
    else:
        print('Any ticket with the following 4 numbers wins:')
        for num in winner:
            print(num)            
        winner.clear()
        i = 0
        l += 1
print(f"It took {l} number of attempts to win!")