import math

# Github link => https://github.com/SkrSateri/assignFive.git

def main():
    run = True
    while run:#to keep the program running
        try:
            number = int(input("Please give a number-> "))
            if number <= 1 :# The if method to check input value if its valid
                print("The entered number is smaller or equals to 1! Please try again")
            iteration_one = method_one(number)
            iteration_two = method_two(number)
            print("With 1st method number of iteration is:" + str(iteration_one))
            print("With 2nd method number of iteration is:" + str(iteration_two))
        except:
            print("Please enter a whole number !")
        print("")
        print("")

def method_one(number): #The first method which controls everynumber from 2 to input value
    factors = []
    factorsString = ""
    iterations = 0
    for x in range(number):
        if x != number - 2:
            x = x+2
        elif x == number - 2:
            break
        iterations = iterations+1
        if number%x == 0:
            factors.append(x)
            factorsString = factorsString + " " + str(x)
    return iterations

def method_two(number): # the second method which controls with advanced square root operation(pseudo code from slides)
    b = math.sqrt(number)
    x = number
    i = 2
    factors = []
    iteration = 0
    while x > 1 and i <= b:
        iteration = iteration+1
        while x%i == 0:
            iteration = iteration + 1
            try:
                factors.index(i)
            except:
                pass
            factors.append(i)
            x = x/i
            b = math.sqrt(x)
        i = i+1
    if x > 1 and x != number:
        factors.append(int(x))
    factors = list(dict.fromkeys(factors))
    if len(factors) <= 0:
        print(str(number) + " is prime number and factors are-> " + str(factors))
    else:
        print(str(number) + " is composite number and factors are-> " + str(factors))
    return iteration



main()