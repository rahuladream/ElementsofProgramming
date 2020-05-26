

def alternatingCharacters(s):
    count = 0
    new_s = list(s)
    for i in range(0, len(s)-1):
        if s[i] == s[i + 1]:
            count += 1
            new_s.remove(s[i])
    return count




print(alternatingCharacters("AAABBB"))