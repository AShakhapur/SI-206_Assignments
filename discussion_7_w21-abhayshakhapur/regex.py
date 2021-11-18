def makeUpper(sentence):
    words = sentence.split(" ")
    lst1 = []
    lst2 = []
    string = ""
    for word in words:
        word1 = list(word)
        word1[0]=word1[0].upper()
        lst1.append(word1)
    for lst in lst1:
        string = string+"".join(lst)
        string = string+" "
    print(string.strip()+"hi")
    return string
makeUpper('hi my name is abhay')
def nums_until_negative(lst):
    new_lst = []
    for num in lst:
        if num>0:
            new_lst.append(num)
        else:
            break
    print(new_lst)
    return new_lst

def stringsThatContain(lst, must_contain):
    new_lst = []
    for string in lst:
        if must_contain in string:
            new_lst.append(string)
    print(new_lst)
    return new_lst