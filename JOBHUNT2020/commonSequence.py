

def longest_common_sequence(str1, str2):
    return "".join(i if i in str2 else "" for i in str1)

print(longest_common_sequence("ABCDGH", "AEDFHR"))