# Python3 program to find all subthat 
# contain all vowels 
  
# Returns true if x is vowel. 
def isVowel(x): 
      
    # Function to check whether a character is 
    # vowel or not 
    if (x == 'a' or x == 'e' or x == 'i' or 
        x == 'o' or x == 'u'): 
        return True
    return False
  
def FindSubstr1ing(str1): 
  
    # To store vowels 
  
    # Outer loop picks starting character and 
    # inner loop picks ending character. 
    n = len(str1) 
    for i in range(n): 
        hash = dict() 
        for j in range(i, n): 
  
            # If current character is not vowel, 
            # then no more result substr1ings 
            # possible starting from str1[i]. 
            if (isVowel(str1[j]) == False): 
                break
  
            # If vowel, then we insert it in hash 
            hash[str1[j]] = 1
  
            # If all vowels are present in current 
            # substr1ing 
            if (len(hash) == 5): 
                print(str1[i:j + 1], end = " ") 
  
# Driver code 
str1 = "azerdii"
aa = FindSubstr1ing(str1)
  
# This code is contributed by Mohit Kumar 
