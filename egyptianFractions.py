# Egyptian fraction Greedy
from math import ceil
  
# n is the numerator, d is the denominator
def egyptian(n, d):
  
    print("The Egyptian Fraction of {}/{}".format(n, d))
    ans = []
    # while numerator is not 0
    while (n > 0):
        x = ceil(d / n)          # compute the minimal larger denominator
        ans.append(x)            # hold it to the numerator list
        n, d = x * n - d, d * x  # update the remainder to n and d
    for a in ans:
        print("1/{}".format(a), end=" ")

def main():
    print("Greedy Algorithm to Compute Egytian Fractions")
    stay = True
    while stay:
        n = int(input("Enter the numerator: "))
        d = int(input("Enter the denominator: "))
        egyptian(n, d)
        stay = ("n" != (input("\nCompute another? (no to stop) ")+" ")[0])

main()

# The Egyptian Fraction of 5/6 = 1/2 1/3 
# The Egyptian Fraction of 7/15 = 1/3 1/8 1/120 
# The Egyptian Fraction of 23/34 = 1/2 1/6 1/102 
# The Egyptian Fraction of 121/321 = 1/3 1/23 1/7383 
# The Egyptian Fraction of 5/123 = 1/25 1/1538 1/4729350 
# The Egyptian Fraction of 5/121 = 1/25 1/757 1/763309 1/873960180913 1/1527612795642093385023488 