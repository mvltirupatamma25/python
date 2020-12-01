def n_string(str):
    lst=list(str)
    l=["a","i","e","o","u"]
    for i in l:
        if i in lst:
            lst.remove(i)
            str1=" ".join(lst)
    return(str1)
    
