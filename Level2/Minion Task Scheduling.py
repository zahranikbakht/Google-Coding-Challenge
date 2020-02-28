def solution(n,b):
    
    list_of_id = []     # list of IDs
    length = len(n)     # fixed length of IDs
    loop_found = False  
    list_of_id.append(n)   # putting the first ID in the list
    next_id = n
    
    # computing the next ID as long as no loop is found
    while not loop_found:
        x = ""
        y = ""
        list_of_digits = []     # list of the digits of the given ID
        for i in next_id:
            list_of_digits.append(int(i))
        
        # calculating y in base ten    
        list_of_digits.sort()
        for i in list_of_digits:
            y += str(i)
        y = int(y,b)
        
        # calculating x in base ten
        list_of_digits.sort(reverse=True)
        for i in list_of_digits:
            x += str(i)
        x = int(x,b)
        
        # calculating z in base ten, then taking it to base b
        z = x-y
        i = z
        new = ""
        while i > 0:
            rem = i%b
            i = i//b
            new += str(rem)
        new = new[len(new)::-1]     # our newly calculated ID
        
        # checking if we have to add leading zeros
        if len(new) < length:
            final = ""
            digits =[]
            for i in new:
                digits.append(i)
            num_zeros = length - len(new)
            for i in range (num_zeros):
                digits.insert(0,"0")
            for i in digits:
                final += i
            new = final
        
        # now that we have z, we check if it's already in the list. 
        # if it is, then we have created the loop. so we need to find where it starts.
        # if no loop is found, add the ID and go back to calculate the next one
        for i in range(len(list_of_id)):
            if list_of_id[i] == new:
                loop_found = True
                magic = i   # the index where the loop starts
                break
        if not loop_found:
            list_of_id.append(new)
        next_id = new
        
    return len(list_of_id) - magic

print(solution("1211", 10))