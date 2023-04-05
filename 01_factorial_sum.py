"""def factorial(num):
    
    fact= 1
    for num in range(1, num+1):
        fact = fact * num
        
    print(fact)
    list = [int(x) for x in str(fact)]

    sum = 0
    for i in list:
        sum = sum + i
    print (sum)

user_input = int(input("Enter any number to find factorial : "))
factorial(user_input)

"""

class factorial:
    def __init__(self, num):
        self.num = num     

    def result(self):
        fact = 1
        for num in range(1, self.num+1):
            fact = fact * num
        print(fact)
        list = [int(x) for x in str(fact)]

        sum = 0
        for i in list:
            sum = sum + i
        print (sum)
        
try:
    user_input = int(input("Enter any number to find factorial :"))
    fact = factorial(user_input)
    fact.result()
except:
    print("Enter integer value")
    
    


