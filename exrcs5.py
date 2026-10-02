def check_even_odd(number: int) -> str:
    if number % 2 == 0:
        return "Even"
    return "Odd"


def count_vowels(text: str) -> int:
    vowels = "aeiou"
    vowel_counter = 0
    for char in text:
        if char.lower() in vowels:
            vowel_counter += 1
    return vowel_counter


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


def calculate_average_marks(marks: list[float]) -> float:
    if not marks:
        return 0.0
    return sum(marks) / len(marks)


if __name__ == "__main__":
    print(f"check_even_odd(7) ➔ {check_even_odd(7)}")
    print(f"count_vowels('Apna College') ➔ {count_vowels('Apna College')}")

    test_primes = [-5, 1, 2, 4, 7, 12]
    for num in test_primes:
        print(f"is_prime({num}) ➔ {is_prime(num)}")

    marks = [85.5, 90.0, 78.0, 92.5]
    print(f"calculate_average_marks({marks}) ➔ {calculate_average_marks(marks)}")