"""
這是多行註解
這邊可以放很多文字
"""

# 這是單行註解
# ctrl+? 可以快速註解/取消註解
# 基本型態
print(1)  # int這是整數,-1,0,1,2,3,4,5,6,7,8,9
print(1.0)  # float這是浮點數
print("apple")  # str這是字串"sadasd123125557"
print(True)  # bool這是布林值True,False
print(False)  # bool這是布林值True,False
# 變數
a = 10  # 新增一個存空間並取名為a,"="的功能是將右邊的值10存入邊的a
print(a)  # 在終端機顯示a所存的值
a = "apple"  # 將a的值改為"apple"
print(a)  # 在終端機顯示a所存的值
# 運算子
print(1 + 1)  # 加
print(1 - 1)  # 減
print(1 * 1)  # 乘
print(1 / 1)  # 除
print(1**1)  # 次方
print(1 % 1)  # 取餘數
print(1 // 1)  # 取整
# 優先順序
# 1.()括號
# 2.**次方
# 3./除
# 4.%取餘數
# 5.+加
# 6.-減
# 字串運算
print("apple" + "apple")  # 字串加
print("apple" * 3)  # 字串乘
# 練習
a = "10"
b = "20"
print(a + " " + b)
# 字串格式化
name = "apple"
age = 18
print(f"Hellow, my name is{name},I am{age}years old")  # f-string
