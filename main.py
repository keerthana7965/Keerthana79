print("Enter a Number: ", end="")
try:
    num = int(input())
    fact = 1
    for i in range(1, num+1):
        fact = fact*i
    print("\nFactorial of", num, "=", fact)
except ValueError:
    print("\nInvalid Input!")
