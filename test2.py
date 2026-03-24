num = input("请输入一个5位数字：")

if num == num[::-1]:
    print(f"{num} 是回文数")
else:
    print(f"{num} 不是回文数")
