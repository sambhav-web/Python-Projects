from random import randint,choice,shuffle
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','&','*','_','-','+','=','^','?','.']
def generate_password():
    """This function helps to generate a strong password"""
    password=[]
    alpha=randint(8,10)
    num=randint(2,4)
    sym=randint(2,4)
    for _ in range(alpha):
        password.append(choice(alphabets))
    for _ in range(num):
        password.append(choice(numbers))
    for _ in range(sym):
        password.append(choice(symbols))
    shuffle(password)
    return "".join(password)
print(generate_password())