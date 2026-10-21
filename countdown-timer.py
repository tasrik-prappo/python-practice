import time

total_seconds: int = int(input("Enter time in seconds: "))

for remaining in range(total_seconds, 0, -1):
    seconds: int = remaining % 60
    minutes: int = (remaining // 60) % 60
    hours: int = remaining // 3600

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP")