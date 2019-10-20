def Descending_Order(num):
    lst = [x for x in str(num)] #conversion of inpout into string
    new_lst = sorted(list(lst))[::-1] # sorting the list and reversing it
    x = '' # output storage
    for c in new_lst: #iterating over the new_lst
        x += c #concateneating the components of c
    return int(x) #returning x by converting it into integer
