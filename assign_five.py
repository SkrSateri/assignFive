

def main():
    number = int(input("Please give a number-> "))
    factors = []
    factorsString = ""
    for x in range(number):
        tryNumber = x+1
        if number%tryNumber == 0:
            factors.append(tryNumber)
    for x in factors:
        if x == number:
            factorsString = factorsString + str(x)
        else:
            factorsString = factorsString + str(x) + ","
    if len(factors) <= 2:
        print(str(number) + " is prime number and factors are-> " + factorsString)
    else:
        print(str(number) + " is composite number and factors are-> " + factorsString)
main()