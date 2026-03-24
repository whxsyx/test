year = int(input("请输入一个4位数的年份："))

res = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if res:
    print(f"{year}年是闰年")
else:
    print(f"{year}年不是闰年")
