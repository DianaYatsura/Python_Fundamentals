"""Sort the numbers only using if else statement
You are provided with 3 arguments num1 num2 num3
Print the sorted value result like print(1,2,3) """

def sortNumbers(num1,num2,num3):
    if num1 < num2 < num3:
        print(num1, num2, num3)
    elif num2 < num1 < num3:
        print(num2, num1, num3)
    elif num1 > num2 > num3:
        print(num3, num2, num1)
    elif num1 < num2 > num3:
        print (num1, num3, num2)

# enter values for num1 num2 num3
sortNumbers(num1=, num2=, num3=)

