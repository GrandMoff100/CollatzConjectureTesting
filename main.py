STEP_CACHE = {}


def collatz_rule(n: int) -> int:
    return STEP_CACHE.get(n, n * 3 + 1 if n % 2 else n // 2)

def collatz_steps(n :int) -> int:
    if n == 1:
        return 0
    else:
        return 1 + collatz_steps(collatz_rule(n))

i = 1
while True:
    print(i, collatz_steps(i))
    i += 1