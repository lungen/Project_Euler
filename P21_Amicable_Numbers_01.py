def make_divi(n):
    
    divi = [i for i in range(1, n) if not n % i]
    s = list(map(int, divi))
    #print(n, " = ", divi)
    #print(sum(s))
    return sum(s)
    
    
def loop_it(start=2, limit=5):
    
    for r in range(start, limit + 1):
        sum1 = make_divi(r)
        sum2 = make_divi(sum1)
        
        if r == sum2 and sum1 != sum2:
            print("GOT IT: ", r, sum1, sum2)
        
        
    
    
def start():
    
    #loop_it(1, 230)
    loop_it(228,229)
    
    
start()
