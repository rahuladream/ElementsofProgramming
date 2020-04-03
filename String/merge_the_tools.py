"""
A string, , of length  where .
An integer, , where  is a factor of .
We can split  into  subsegments where each subsegment, , consists of a contiguous block of  characters in . Then, use each  to create string  such that:

"""


def merge_the_tools(string, k):
    size = len(string)
    subsequent = int(size / k)
    for i in range(0, size, subsequent):
        print("".join(set(string[i:i+3])))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)