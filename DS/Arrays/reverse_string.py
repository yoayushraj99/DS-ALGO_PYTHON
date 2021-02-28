# Method-1
def reverse1(string):
    split_str = list(string)
    split_str.reverse()
    reverse_str = "".join(split_str)
    print(reverse_str)


def reverse2(string):
    reverse_list = []
    for i in range(len(string)-1, -1, -1):
        reverse_list.append(string[i])
    reverse_str = "".join(reverse_list)
    print(reverse_str)


reverse1("i am ayush")
# hsuya ma i

reverse2("Angela Yu")
# uY alegnA
