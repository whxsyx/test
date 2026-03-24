x1 = float(input("请输入第一个点的x坐标："))
y1 = float(input("请输入第一个点的y坐标："))
x2 = float(input("请输入第二个点的x坐标："))
y2 = float(input("请输入第二个点的y坐标："))

distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print(f"两点间的距离为：{distance:.2f}")