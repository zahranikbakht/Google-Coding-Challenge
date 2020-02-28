def solution(x, y):
    # convert the arguments to integer
    m = int(x)
    f = int(y)
   
    count = 0   # keeps track of the number of generations
    
    # if the numbers are equal (and not 1), it is impossible
    # (generally any two numbers that are not reltively prime
    # make an impossible combination.)    
    if (f == m and m != 1):
        return "impossible"
    else:
        
        # while none of them has reached 1, substract the biggest
        # multiplication of the smaller number from the bigger number
                    
        while f != 1 and m !=1:
            
            if m>1 and f>1 and m-f>0:
                count += m//f
                m = m-((m//f)*f)
                if m == 0:
                    break
            elif f>1 and m>1 and f-m>0: 
                count += f//m 
                f = f-((f//m) *m)
                if f == 0:
                    break
      
                        
      # if none of the numbers is 0 after the loop, show the number of generations 
        if m != 0 and f != 0:
            return str(count + max(m,f) - 1)
        else:
            return "impossible"

print(solution("7","8"))

