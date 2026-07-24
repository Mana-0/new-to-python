n = int(input())
for row in range(n):
    spaces = ' ' * (n - row - 1)
    print(spaces + '*' * (row + 1))
