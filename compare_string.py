
def compare_string(s1,s2):
    
    aList1 = list(s1)
    aList2 = list(s2)
    
    aList1.sort()
    aList2.sort()
    
    pos = 0 
    match = True
    
    while pos < len(s1) and match:
        if aList1[pos] == aList2[pos]:
            pos = pos + 1
        else:
            match = False
    return match 


print(compare_string('abcdef' , 'pdsfsdf'))
print(compare_string('abcdef' , 'abcdef'))