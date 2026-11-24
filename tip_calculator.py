print('Welcome to the tip Calculator!')
while True:
    try:
        bill=float(input('Enter the total bill to pay: $'))
        people=int(input('Enter the total number of people to distribute : '))
        if people<=0:
            raise ValueError('Choose valid Number of people')
        tip_to_give=int(input('Choose the percent of tip : 5,8 or 10 : '))
        if tip_to_give not in [5,8,10]:
            raise ValueError('Plz enter a valid percent')
    except Exception as e:
        print(e)
        continue
    else:
        total_bill=bill+((bill*tip_to_give)/100)
        bill_per_head=total_bill/people
        print(f'The total bill is ${total_bill} with tip of {tip_to_give}% and each to pay : ${bill_per_head:.2f}')
        break