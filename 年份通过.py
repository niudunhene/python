nian = int(input("请输入年份")) 
yue = int(input("请输入月份"))
tian = int(input("请输入日期"))

if (nian % 4 == 0 and nian % 100 != 0) or (nian % 400 == 0):
    print(nian, "年是闰年")
else:
    print(nian, "年不是闰年")

x = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

y = 0

if (nian % 4 == 0 and nian % 100 != 0) or (nian % 400 == 0):
    x[1] = 29
    if yue == 1:
        print("这是此年第", tian, "天")
    else:
        for i in range(yue - 1):
            y += x[i]
        y += tian
        
        print("这是此年第", y, "天")
else:
    
    if yue == 1:
        print("这是此年第", tian, "天")
    else:
        for i in range(yue - 1):
            y += x[i]
        y += tian
        print("这是此年第", y, "天")
