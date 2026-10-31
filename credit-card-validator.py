def credit_card_validator(card_num: str) -> bool:
    card_num = card_num.replace(" ","")
    card_num = card_num.replace("-","")
    card_num = card_num[::-1]
    
    sum_of_odd_digits: int = 0
    sum_of_even_digits: int = 0        
    
    
    for i in range(len(card_num)):
        store: int = 0
        if (i+1) % 2 == 0:
            store = int(card_num[i]) * 2
            if is_double_digit(store):
                sum_of_even_digits += sum_of_digits(store)
            else:
                sum_of_even_digits += store
        else:
            sum_of_odd_digits += int(card_num[i])

    return (sum_of_odd_digits + sum_of_even_digits) % 10 == 0


def is_double_digit(num: int) -> bool:
    return 10 <= num <= 18

def sum_of_digits(num: int) -> int:
    num = abs(num)
    total: int = 0

    while num > 0:
        total += num % 10
        num = num //10

    return total


def main():
    card_num: str = input("Please enter your credit card number: ")
    if credit_card_validator(card_num):
        print("Valid")
    else:
        print("Invalid")
    

    
if __name__ == '__main__':
    main()