
def factorial_iterative(n):
    if n < 0:
        return "Undefined for negative numbers"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    num = 5  # Change this value to test with other numbers
    print(f"Factorial of {num} (iterative): {factorial_iterative(num)}")