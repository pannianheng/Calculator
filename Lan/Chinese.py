import math
import cmath

# ==================== 整数根号精确化简 ====================
def simplify_int_sqrt(n):
    """
    输入整数 n，返回：
    - int（当结果为纯整数，如 3）
    - str（当结果为符号形式，如 "2√2"、"2i"、"3√2i"）
    """
    if n == 0:
        return 0

    is_neg = n < 0
    n = abs(n)

    # 找最大平方因子
    max_i = math.isqrt(n)
    coeff = 1
    rem = n
    for i in range(max_i, 0, -1):
        sq = i * i
        if n % sq == 0:
            coeff = i
            rem = n // sq
            break

    # 纯整数情况：根号内为 1
    if rem == 1:
        if is_neg:
            return f"{coeff}i"
        else:
            return coeff   # 返回 int，不是 str

    # 有根号的情况
    if coeff == 1:
        result = f"√{rem}"
    else:
        result = f"{coeff}√{rem}"

    if is_neg:
        result += "i"

    return result


# ==================== 小数根号浮点计算 ====================
def calc_float_sqrt(val):
    """
    输入 float，返回复数形式的字符串表示
    """
    result = cmath.sqrt(val)

    real = result.real
    imag = result.imag

    # 浮点误差修正
    if abs(real) < 1e-12:
        real = 0.0
    if abs(imag) < 1e-12:
        imag = 0.0

    # 纯实数
    if imag == 0.0:
        return f"{round(real, 6)}"

    # 纯虚数
    if real == 0.0:
        return f"{round(imag, 6)}i"

    # 复数
    return f"{round(real, 6)}{'+' if imag >= 0 else ''}{round(imag, 6)}i"


# ==================== 判断整数还是小数 ====================
def is_integer_input(s):
    """
    通过字符串判断用户输入是否为整数
    """
    s = s.strip()
    if s.startswith('-'):
        s = s[1:]
    return s.isdigit()


# ==================== 主程序 ====================
print("命令行计算器（支持 + - * / sqrt）")
print("sqrt 模式：整数精确化简，小数浮点计算")

while True:
    op = input("\n运算符 (+ - * / sqrt(根号)，**(幂运算),q 退出): ").strip()

    if op == "q":
        print("退出")
        break

    # ---------- sqrt ----------
    if op == "sqrt":
        raw = input("数字: ").strip()

        if is_integer_input(raw):
            val = int(raw)
            result = simplify_int_sqrt(val)

            if isinstance(result, int):
                print("结果:", result)
            else:
                print("结果:", result)

        else:
            try:
                val = float(raw)
                print("结果:", calc_float_sqrt(val))
            except ValueError:
                print("输入无效")

    # ---------- 四则运算 ----------
    elif op in ("+", "-", "*", "/"):
        try:
            a = float(input("第一个数: "))
            b = float(input("第二个数: "))
        except ValueError:
            print("输入无效")
            continue

        if op == "+":
            print("结果:", a + b)
        elif op == "-":
            print("结果:", a - b)
        elif op == "*":
            print("结果:", a * b)
        elif op == "/":
            if b == 0:
                print("错误：除数不能为 0")
            else:
                print("结果:", a / b)
    elif op == "**":
        try:
            a = float(input("底数："))
            b = float(input("指数："))
        except:
            print("输入无效")
            continue

        c = a ** b
        if int(c) == c:
            print(int(c))
        else:
            print(c)

    else:
        print("不支持的运算符")