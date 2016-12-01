def move_zeros(array):
    zeros = []
    non_zeros = []
    for el in array:
        if type(el) == type(False) or el != 0:
            non_zeros.append(el)
        else:
            zeros.append(el)
    array = non_zeros + zeros

    return array


print move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9])
