# Works but is not efficient. Memoization is needed.
def fib2(n: int) -> int:
    if n < 2: # base case
        return n
    return fib2(n-1) + fib2(n-2)


if __name__ == "__main__":
    print(fib2(45))
