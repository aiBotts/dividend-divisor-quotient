dividend = input("Enter a dividend: ")
divisor = input("Enter a divisor: ")

try:
    quotient = int(dividend) / int(divisor)
except ValueError:
    print("Divisor or dividend was not an integer")

except ZeroDivisionError:
    print("The divisor cannot be 0")
    exit()

print(quotient)

