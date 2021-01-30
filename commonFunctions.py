def count(obj, lst):
    count = 0
    for e in lst:
        if e == obj:
            count = count + 1
    return count

def is_in(obj, lst):  
    for e in lst:
        if e == obj:
            return True
    return False

def reverse(lst):
    reversed = []
    for i in range(len(lst)-1, -1, -1): 
        reversed.append(lst[i])
    return reversed

def index(obj, lst):
    for i in range(len(lst)):
        if lst[i] == obj:
            return i
    return -1

def insert(obj, index, lst):
    newlst = []
    for i in range(len(lst)):
        if i == index:
            newlst.append(obj)
        newlst.append(lst[i])
    return newlst