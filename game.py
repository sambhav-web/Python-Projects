import random
def get_computer_choice():
    return random.randint(0,2)
def determine_winner(user,opponent,user_score,opponent_score):
    if user==opponent:
        return 'Draw',user_score,opponent_score
    elif (user==0 and opponent==1) or (user==1 and opponent==2) or (user==2 and opponent==0):
        return 'You won!',user_score+1,opponent_score
    return 'Computer won!',user_score,opponent_score+1
print('Welcome to Rock,Paper and Scissor Game')
is_on=True
menu={0:'Rock',1:'Scissor',2:'Paper'}
user_score=0
computer_score=0
while is_on:
    try:
        computer=get_computer_choice()
        user=int(input('Choose 0 for Rock, 1 for Scissor and 2 for Paper'))
        if user not in [0,1,2]:
            raise ValueError('Choose valid argument between 0 and 2')
    except ValueError as e:
        print(e)
        continue
    else:
        outcome,user_score,computer_score=determine_winner(user,computer,user_score,computer_score)
        print(f"Computer Choose : {menu[computer]}\nUser Choose : {menu[user]}\n{outcome}")
        print(f"User Score : {user_score} Computer Score : {computer_score}\n")
    try:
        decision=input('Do you want to play once more: Y/N').lower()
        if decision not in ('y','n'):
            raise ValueError('Plz choose y/n')
    except ValueError as e:
        print(e)
        continue
    if decision=='n':
        is_on=False