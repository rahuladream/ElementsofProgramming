"""
INPUT:
N students store them in a nested list and print the name(s) of any student(s)
having 


"""



if __name__ == '__main__':
    students = [[input(), float(input())] for i in range(int(input()))]    
    studentsSet = sorted(set(x[1] for x in students))
    if len(studentsSet) > 1:
        for name in sorted(x[0] for x in students if x[1] == studentsSet[1]):
            print(name)   
