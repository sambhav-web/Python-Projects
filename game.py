import random
def compare(user_choice,computer_choice):
    if user_choice==computer_choice:
        return 'Draw'
    elif (user_choice==0 and computer_choice==1) or (user_choice==1 and computer_choice==2) or (user_choice==2 and computer_choice==0):
        return 'User won!'
    else:
        return 'Computer won!'
def winner(user,computer,output):
    print(f'User chose : {user}')
    print(f'Computer chose : {computer}')
    print(f'The result of game is {output}')
print('Welcome to Rock,Paper,Scissor Game\nThe game consists 3 rounds')
user_score=0
computer_score=0
for i in range(1,4):
    print(f'Round : {i}')
    computer=random.randint(0,2)
    while True:
        try:
            user=int(input('Choose \n0. Scissor,\n1. Paper,\n2. Rock'))
            if 0<=user<=2:
                break
            else:
                raise ValueError('Choose a valid operation.')
        except ValueError as exp:
            print(exp)
    result=compare(user,computer)
    winner(user,computer,result)