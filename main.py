def collatz_rule(n: int) -> int:
    if n % 2:
        return n // 2
    else:
        return 3 * n + 1

def collatz_steps(n :int) -> int:
    print(n)
    if n == 1:
        return 0
    else:
        return 1 + collatz_steps(collatz_rule(n))

i = 4
print(i, collatz_steps(i))