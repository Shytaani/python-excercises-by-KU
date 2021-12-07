while True:
    x = input("正の数値を入力してください ")
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
        print(rnew, "は0以下の数値です")
        continue
    rnew = xfloat
    diff = rnew - xfloat/rnew
    diff = abs(diff)
    while (diff > 1.0E-6):
        r1 = rnew
        r2 = xfloat/r1
        rnew = (r1 + r2)/2
        print(r1, rnew, r2)
        diff = r1 - r2
        diff = abs(diff)
