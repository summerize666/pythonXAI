# 比較運算子
print(1 == 1)  # true
print(1 == 2)  # false
print(1 != 1)  # false
print(1 != 2)  # true
print(1 < 2)  # true
print(1 > 2)  # false
print(1 <= 2)  # true
print(1 >= 2)  # false

# 邏輯運算子
print(True and True)  # true
print(True and False)  # false
print(False and True)  # false
print(False and False)  # false
print(True or True)  # true
print(True or False)  # true
print(False or True)  # true
print(False or False)  # false
# 優先順序
# 1.()括號
# 2.**次方
# 3./除
# 4.%取餘數
# 5.+加
# 6.-減
# 7and
# 8or
# 9not
# 密碼門檢查
password = input("請輸入密碼：")
if password == "123456":
    print("密碼正確！")
elif password == "12345678":
    print("密碼正確！")
else:
    print("密碼錯誤！")
