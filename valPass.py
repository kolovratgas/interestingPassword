def is_valid_password(password):
    password = password.split(':')
    if len(password) != 3:
        return False

    testDig1 = password[0].isdigit()
    testDig2 = password[1].isdigit()
    testDig3 = password[2].isdigit()
    if testDig1 == False or testDig2 == False or testDig3 == False:
        return False

    pass1 = password[0]
    password1 = int(password[0])
    password2 = int(password[1])
    password3 = int(password[2])

    #password1
    polyndromTest = polyndrom(pass1)

    #password2
    prostTest = prost(password2)

    #password3
    chetTest = chet(password3)


    return result(polyndromTest, prostTest, chetTest)

#1
def polyndrom(pass1):
    chap1 = []
    for j in range(len(pass1)):
        chap1.append(pass1[j])

    if chap1 == chap1[::-1]:
        return True
    else:
        return False

#2
def prost(pass2):
    if pass2 == 1:
        return False
    for i in range(2, pass2 + 1):
        d = pass2 % i
        if i == pass2:
            return True
        elif d == 0:
            return False
#3
def chet(pass3):
    if pass3 % 2 == 0:
        return True
    else:
        return False

def result(pass1, pass2, pass3):
    if pass1 == True and pass2 == True and pass3 == True:
        return True
    else:
        return False

digit = str(input())
print(is_valid_password(digit))
