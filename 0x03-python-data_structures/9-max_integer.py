def max_integer(my_list=[]):
    if not my_list:
        return None
    
    maximum_int = my_list[0]
    for n in my_list:
        if n > maximum_int:
            maximum_int = n
    
    return maximum_int
