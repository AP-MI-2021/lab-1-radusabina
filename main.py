'''
Returneaza true daca n este prim si false daca nu.
'''

 def is_prime(n) :
    if n<2 :
        return False
    else :
        for i in range(2,n//2 + 1) :
            if (n%i == 0) :
                return False
            else :
                return True
 assert is_prime(2) is True
 assert is_prime(11) is True
 assert is_prime(4) is False
  
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
    produs=1
    for x in lst:
        produs=produs*x
        return produs

  
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x,y):
    while(x!=y):
        if(x>y):
            x=x-y
        else:
            y=y-x
    return x
  
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
    while(y!=0):
        r=x%y
        x=y
        y=r
    return x
  
  
def main():
  # interfata de tip consola aici
 x = int(input())
 y = int(input())

get_cmmdc_v1(x,y)
get_cmmdc_v2(x,y)

get_cmmdc_v1(7,12)
get_cmmdc_v2(4,16)
  
  

if __name__ == '__main__':
  main()
