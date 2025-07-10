# 算術指定運算種子
a = 1
a += 1
print(a)
a -= 1
print(a)
a *= 2
print(a)
a /= 2
print(a)
a //= 2
print(a)
a %= 2
print(a)
a **= 2
print(a)
# 優先順序
# 1.()括號
# 2.**次方
# 3//%乘 除 取商 餘數
# 4.+加
# 5.-減
# 6.not
# 7.and
# 8.or
# 9.= +=-=*=/=%//=%=
# while迴圈
# while 會搭配一個條件使用
# 條件式為 True 時會一直執行迴圈
# 條件式為 False 時會跳出迴圈
i = 0
while i < 5:
    print(i)
    for j in range(5):
        print(j)
        if i == 3:
            break
    i += 1

for i in range(5):
    print(i)
    if i == 3:
        break


import random

print(random.randrange(7))
print(random.randrange(1, 7))
print(random.randrange(1, 7, 2))
print(random.randint(1, 6))
ans = random.randint(1, 100)
while True:
    num = int(input(f"請輸入1到100："))
    if num > 100 or num < 1:
        print("請輸入正確的數字！")
    elif num > ans:
        print("太大咯！")
    elif num < ans:
        print("太小咯！")
    else:
        print("正確！")
        break
d = {"apple": 20, "banana": 30, "orange": 25}
print(d)
d = {"apple": 20, "banana": 30, "orange": 25}
print(d["apple"])
d = {"apple": 20, "banana": 30, "orange": 25}
for k in d:
    print(k)
    print(d[k])
for k in d.keys():
    print(k)
    print(d[k])
for k in d.keys():
    print(k)
    print(d[k])
    for v in d.values():
        print(v)
for k, v in d.items():
    print(f"{k}:{v}")
    d = {"apple": 20, "banana": 30, "orange": 25}
    print(d)
    d["蓮霧"]
    print(d)
    d = {"apple": 20, "banana": 30, "orange": 25}
    d["apple"] = 10
    print(d)
    d["蓮霧"]
    print(d)
    d = {"apple": 20, "banana": 30, "orange": 25}
    d.pop("apple")
    popiten = d.pop("蓮霧", "不存在這筆資料")
    print(d)
    print(popitem)
