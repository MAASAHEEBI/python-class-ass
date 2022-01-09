##Write a Python class to implement pow(x, n)


x=int(input('enter base value: '))
n=int(input('enter power value: '))
class power_class:
   def pow(self, x, n):                  
        return x**n
print(x,'to the power',n,'is =',power_class().pow(x,n))
