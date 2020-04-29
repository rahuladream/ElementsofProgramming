"""

A contact list is a place where you can store a specific contact with other associated information such as a phone number, email address, birthday, etc. Write a program that creates a dictionary with the following entries:

Joe 123-5432 
Linda 983-4123 
Frank 867-5309
The program presents the user with a menu of choices:

What would you like to do?
a - add entry
l - look up entry
d - delete entry
p - print all entries
q - quit
It reads in user's choice and performs the action requested by user. E.g. if the wishes to add an entry, the program will ask for name and phone number, then add that entry to the dictionary. If the user wishes to look up entry, the program will ask for the name and will print the phone number associated with that name. If the user wishes to print all entries, the program just does that.

After the action is complete, the program should present the menu of choices again. It should do so until the user chooses to quit.
thank you
"""


# dict = {'Joe': '123-5432', 'Linda': '983-4123', 'Frank': '867-5309'}

# contact_data = {}

# question = input(f'What would you like to do?\na - add entry\nl - look up entry\nd - delete entry\np - print all entries\nq - quit\n')

# while question != "q":
#     if question == "a":
#         name = input("Enter name ")
#         number = input("Enter phone ")
#         dict[name] = number
#     elif question == "l":
#         name = input()
#         print(dict[name])
#     elif question == "d":
#         name = input()
#         dict.pop(name)
#     elif question == "p":
#         print(dict)
#     question = input(f'What would you like to do?\na - add entry\nl - look up entry\nd - delete entry\np - print all entries\nq - quit\n')

dict = {}

q = input(f'What would you like to do?\na - add entry\nl - look up entry\nd - delete entry\np - print all entries\nq - quit\n')
while(q != "q"):
    if q == "a":
        name = input()
        number = input()
        dict[name] = number
    elif q == "l":
        name = input().strip()
        print(dict[name])
    elif q == "d":
        name = input().strip()
        dict.pop(name)
    elif q == "p":
        print(dict)
    elif q == "q":
        exit()
    q = input(f'What would you like to do?\na - add entry\nl - look up entry\nd - delete entry\np - print all entries\nq - quit\n')