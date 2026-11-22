import math
import cmath
import sys
sys.set_int_max_str_digits(0)

# ==================== Exact Simplification for Integer Square Roots ====================
def simplify_int_sqrt(n):
    """
    Input: integer n
    Returns:
    - int (when result is a pure integer, e.g. 3)
    - str (when result is symbolic, e.g. "2√2", "2i", "3√2i")
    """
    if n == 0:
        return 0

    is_neg = n < 0
    n = abs(n)

    # Find the largest square factor
    max_i = math.isqrt(n)
    coeff = 1
    rem = n
    for i in range(max_i, 0, -1):
        sq = i * i
        if n % sq == 0:
            coeff = i
            rem = n // sq
            break

    # Pure integer case: radicand is 1
    if rem == 1:
        if is_neg:
            return f"{coeff}i"
        else:
            return coeff   # return int, not str

    # Case with a radical
    if coeff == 1:
        result = f"√{rem}"
    else:
        result = f"{coeff}√{rem}"

    if is_neg:
        result += "i"

    return result


# ==================== Floating-Point Square Root ====================
def calc_float_sqrt(val):
    """
    Input: float
    Returns: string representation of the complex result
    """
    result = cmath.sqrt(val)

    real = result.real
    imag = result.imag

    # Floating-point error correction
    if abs(real) < 1e-12:
        real = 0.0
    if abs(imag) < 1e-12:
        imag = 0.0

    # Pure real
    if imag == 0.0:
        return f"{round(real, 6)}"

    # Pure imaginary
    if real == 0.0:
        return f"{round(imag, 6)}i"

    # Complex
    return f"{round(real, 6)}{'+' if imag >= 0 else ''}{round(imag, 6)}i"


# ==================== Check Integer Input ====================
def is_integer_input(s):
    """
    Determine whether user input is an integer by string inspection
    """
    s = s.strip()
    if s.startswith('-'):
        s = s[1:]
    return s.isdigit()


# ==================== Main Program ====================
print("Command-Line Calculator (supports + - * / sqrt)")
print("sqrt mode: exact simplification for integers, floating-point for decimals")

while True:
    op = input("\nOperator (+ - * / sqrt, ** for power, q to quit): ").strip()

    if op == "q":
        print("Exiting")
        break

    # ---------- sqrt ----------
    if op == "sqrt":
        raw = input("Number: ").strip()

        if is_integer_input(raw):
            val = int(raw)
            result = simplify_int_sqrt(val)

            if isinstance(result, int):
                print("Result:", result)
            else:
                print("Result:", result)

        else:
            try:
                val = float(raw)
                print("Result:", calc_float_sqrt(val))
            except ValueError:
                print("Invalid input")

    # ---------- arithmetic operations ----------
    elif op in ("+", "-", "*", "/"):
        try:
            a = float(input("First number: "))
            b = float(input("Second number: "))
        except ValueError:
            print("Invalid input")
            continue

        if op == "+":
            print("Result:", a + b)
        elif op == "-":
            print("Result:", a - b)
        elif op == "*":
            print("Result:", a * b)
        elif op == "/":
            if b == 0:
                print("Error: division by zero")
            else:
                print("Result:", a / b)

    elif op == "**":
        try:
            a = float(input("Base: "))
            b = float(input("Exponent: "))
        except:
            print("Invalid input")
            continue

        c = a ** b
        if int(c) == c:
            print(int(c))
        else:
            print(c)

    else:
        print("Unsupported operator")