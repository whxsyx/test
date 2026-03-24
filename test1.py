id = input("请输入18位身份证号码：")

num = int(id[16])

if num % 2 == 0:
    print(f"性别：女性")
else:
    print(f"性别：男性")

