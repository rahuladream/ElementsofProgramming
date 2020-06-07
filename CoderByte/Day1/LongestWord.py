def LongestWord(sen):

    a = [] # creating a tmp value
    # code goes here
    for val in sen.split(' '):
        tmp = ''.join(e for e in val if e.isalnum())
        # joining the string by removing any special character
        a.append(tmp)  
    return max(a, key = len)
    # returning the length on the basis of their length

# keep this function call here 
print(LongestWord(input()))