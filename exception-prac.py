try:
    n = float(input("Enter a number: "))
    print(1/n)

except ZeroDivisionError:
    print("You can't divide by ZERO")

except ValueError:
    print("Enter a number only")

except Exception:
    print("Something went wrong")

finally:
    print("Do some cleanup here")