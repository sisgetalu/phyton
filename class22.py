"""if (True):
    print("hello")
    print ("sisay")
print("done")"""

"""def max_3(num1,num2,num3):
    if ( num1>num2 and num1>num3):
        g=num1
        
    elif (num2>num1 and num2>num3):
        g=num2   
    else:
        g=num3
    print(g)
max_3(3,1,2,)
max_3(3,8,4)"""

"""def check_div(a):
    if(a % 2 == 0):
        if(a % 3 == 0):
            print("It is divisiable by 2 and 3")
        else:
            print("it is divisable by 2")
    elif(a % 3 == 0):
         print("it is divisable by 3")
    else:
        print("nither div by 2 and 3")
        
check_div(6)
check_div(8)
check_div(11)
check_div(9)"""
"""def comput_ot(rate,hour):
    
    if(hour >= 40):
        a=hour*10+(hour-40)*rate
        print(a)
    else:
         a=hour*10
         print(a)


comput_ot(1.5,52)"""

"""while (False):
    print("hello")
    print("sisay")
print("done")"""


"""while (True):
    print("hello")
    print("sisay")
print("done")"""


"""i=1
while(i <= 10):
    i = i+1
    print(i)"""


"""count = 1
sum = 0
while count <= 20:
    sum = sum + count
    count = count +1
print(sum)"""

"""def lcm(a,b):
    greater =  max(a,b)
    while (greater <= a* b):
        found = greater % a== 0 and greater % a== 0
        if(found):
            break
        greater +=1
    return greater
print(lcm(2,3))
print(lcm(6,9))
print(lcm(5,15))
print(lcm(3,4))"""


import random
def guessGame(upperNo):
    number = random.randint(1,upperNo)
    guess = int(input("gess the number betwen 1 and 50"))
    while (guess != number):
        if(guess < number):
            print ("you guessed to low")
        elif(guess > number):
            print ("you gussed to high")
        break
    if(guess == number):
        print("you have found it") 

guessGame(10)
















      










          
