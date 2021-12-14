def square_root(x):
    '引数 x の平方根を求める'
    rnew = x
    diff = rnew - x/rnew
    diff = abs(diff)
    while (diff > 1.0E-6):
        r1 = rnew
        r2 = x/r1
        rnew = (r1 + r2)/2
        print(r1, rnew, r2)
        diff = r1 - r2
        diff = abs(diff)
    return rnew

def get_positive_numeral():
    return input("正の数値を入力してください ")

while True:
    x = get_positive_numeral()
    if x == "end":
        exit()
    try:
        xfloat = float(x)
    except ValueError:
        print(x, "は数値に変換できません")
        continue
    except:
        print("予期していないエラーです")
        exit()
    if not xfloat > 0:
        print(x, "は0以下の数値です")
        continue
    square_root(xfloat)
