def chk_strength(p):
    if not any(i.isalpha() for i in p):
        return 'False4'
    if not any(i.isdigit() for i in p):
        return 'False3'
    if not any( i.islower() for i in p):
        return 'False1'
    if not any(i.isupper() for i in p):
        return 'False2'
    if not any(i in ['!','@','#','$','%','^','&','*','(',')','_','-','.'] for i in p):
        return 'False5'
    return True
print(chk_strength('HELLO23!world@'))