def MenorNumero(*args):
    oMenor = 99999999
    for x in args:
        if(oMenor >= x):
            oMenor = x

    return oMenor


print(MenorNumero(45,89,3,65,738,5539,5)) 
           