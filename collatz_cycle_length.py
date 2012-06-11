
def collatz_cycle_length (n) :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n / 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

def improved(n, p) :                    ###Cache optimized max cycle length method
    if (n > p):
        k = n
        n = p
        p = k
    length_list = [0]*p
    assert n > 0, p > 0
    count = 1
    for i in range (n,p+1):
        origin = i
        while i > 1 :
            if (i <= p):
                if (length_list[i-1] > 0):
                    count += length_list[i-1]
                    length_list[origin-1] = count-1
                    break
            if (i % 2) == 0 :
                i = (i >> 1)
            else :
                i = (3 * i) + 1
            count += 1                
        if (i == 1):
            length_list[origin-1] = count
        count = 1
    print length_list.index(max(length_list)) +1
    return max(length_list)

def main():
#    length_list = [0]*10
#    for i in range (1,10):
    i = 100    
#    print i, "=", collatz_cycle_length (i)
    print improved(280039, 998681)
main()
