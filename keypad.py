keypad: list = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    ['*',0,'#']
]

for i in keypad:
    for j in i:
        print(j, end = ' ')
    print()
        