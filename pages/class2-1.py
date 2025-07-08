# 型態轉換
print(int(1.0))  # float轉int
print(float(1))  # int轉float
print(str(1))  # int轉str
print(bool(1))  # int轉bool
print(int("1.234"))  # str轉int
print(float("1.234"))  # str轉float
print(str(1.234))  # float轉str
print(int("hello"))  # 這行會報錯誤,因為字串裡面如果有非數字的字元,無法轉換成數字
# input()函式的使用
input("請輸入一個數字")
# input()是一個函式,它會在終端機要求使用者輸入一個數字,然後回傳該數字
# ()裡面的文字試題是訊息會先顯示在終端機才會等待使用者輸入
a = input("請輸入一個數字")
print("輸入結束")
print(int(a) + 10)  # 透過input()輸入內容都是字串
# 1. 請使用者輸入半徑
r = float(input("請輸入圓的半徑："))

# 2. 計算圓的面積（用公式 π × r²）
pi = 3.14
area = pi * r * r

# 3. 顯示結果
print(f"圓的面積是：{area}")
