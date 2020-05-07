

def performPermutation(str, tail=''):
    if len(str) == 0: return tail
    else:
        for i in range(len(str)):
            performPermutation(str[0:i] + str[i+1:], tail+str[i])