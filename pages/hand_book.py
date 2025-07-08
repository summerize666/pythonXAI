import streamlit as st

with st.expander("class1筆記"):
    st.write(
        '''
# 🐍 Python 程式設計入門小筆記

今天我們學到了好多好玩的 Python 指令～
讓我們一起來看看吧！😄

---

## ✍️ 註解（就是寫給自己看的小筆記）

程式裡有時候會加上註解，幫助自己或別人看懂：

```python
# 這是單行註解，只能寫一行喔！

"""
這是多行註解，
可以寫好多行的文字！
"""
```

---

## 🔢 基本資料種類（資料型態）

Python 可以處理很多種「資料」，這邊是幾種最常見的：

```python
print(1)         # 整數（int）像是 1、2、3、0、-5...
print(1.0)       # 小數（float）像是 1.0、3.14、0.5...
print("apple")   # 字串（str）用引號包起來的文字
print(True)      # 布林值（bool）只有兩種：True(真) 和 False(假)
print(False)
```

---

## 📦 變數（就像小盒子）

變數就像一個可以裝東西的盒子，我們可以給它取名字，讓我們記得裡面裝的是什麼。

```python
a = 10        # 我們把數字10放進a這個盒子裡
print(a)      # 印出a裡面的東西 → 結果是10

a = "apple"   # 現在我們把a裡的東西換成文字 "apple"
print(a)      # 印出a裡的東西 → 結果是apple
```

---

## ➕➖🟰 運算子（做數學的符號）

我們可以用 Python 做數學計算喔：

```python
print(1 + 1)   # 加法
print(1 - 1)   # 減法
print(1 * 1)   # 乘法
print(1 / 1)   # 除法
print(2 ** 3)  # 次方（像是 2 的 3 次方 = 8）
print(5 % 2)   # 餘數（5 除以 2 的餘數是 1）
print(7 // 2)  # 整數除法（7 除以 2 的整數部分是 3）
```

---

## 📏 計算順序（誰先算？）

做運算時，Python 會按照這個順序來算：

1. `()` 先算括號裡的
2. `**` 次方
3. `*`、`/`、`//`、`%` 乘、除、整除、餘數
4. `+` 和 `-` 最後才算加減

---

## 🔤 字串（就是文字）也可以運算喔！

```python
print("apple" + "apple")  # 加起來變成一長串文字：appleapple
print("apple" * 3)        # 重複3次：appleappleapple
```

---

## 🧪 小練習

我們來把兩個字串組合起來：

```python
a = "10"
b = "20"
print(a + " " + b)  # 結果會是：10 20（中間有一個空格）
```

---

## 🗣️ 字串格式化（把變數塞進句子裡）

這個方法可以讓我們把變數的內容放進句子中：

```python
name = "apple"
age = 18
print(f"Hello, my name is {name}, I am {age} years old.")
```

結果會是：
👉 Hello, my name is apple, I am 18 years old.

---

## 🎉 總結

今天我們學會了：

✅ 註解怎麼寫
✅ 變數是什麼
✅ 四種資料型態（數字、文字、布林）
✅ 數學運算怎麼做
✅ 字串可以加乘
✅ 怎麼讓字串變得更有趣（f-string）

'''
    )
with st.expander("class2筆記"):
    st.write(
        """

# 🐍Python class2筆記 ✨

## 一、🔁 資料轉換（型態轉換）

有時候我們需要把一種資料變成另一種，像這樣：

| 原本            | 轉換方式             | 結果           |
| ------------- | ---------------- | ------------ |
| `1.0`（小數）     | `int(1.0)`       | `1`（變整數）     |
| `1`（整數）       | `float(1)`       | `1.0`（變小數）   |
| `1`（整數）       | `str(1)`         | `"1"`（變文字）   |
| `"1.234"`（文字） | `float("1.234")` | `1.234`（變小數） |

> ⚠️ 注意：如果你用 `int("hello")` 會出錯，因為 "hello" 不是數字。

---

## 二、📊 比較運算子（看看誰大誰小）

這些可以用來比較兩個東西是不是一樣，或哪個比較大：

```python
print(1 == 1)  # 一樣嗎？→ True
print(1 != 2)  # 不一樣嗎？→ True
print(3 > 2)   # 左邊比較大？→ True
print(5 <= 5)  # 左邊比較小或一樣？→ True
```

---

## 三、🔀 邏輯運算子（判斷真假）

你可以用「而且」（`and`）或「或者」（`or`）來做更複雜的判斷：

```python
print(True and False)  # 而且 → False
print(True or False)   # 或者 → True
```

---

## 四、🧠 判斷分數等級（用 if 語法）

如果你輸入一個分數，程式會幫你分級：

```python
score = 85
if score >= 90:
    print("你得到了A")
elif score >= 80:
    print("你得到了B")
elif score >= 70:
    print("你得到了C")
elif score >= 60:
    print("你得到了D")
else:
    print("你拿到了和大熊做朋友的機會")
```

---

## 五、🔐 密碼檢查（用 `if`）

```python
password = input("請輸入密碼：")
if password == "123456":
    print("密碼正確！")
elif password == "12345678":
    print("密碼正確！")
else:
    print("密碼錯誤！")
```

---

## 六、🧮 計算圓面積的小程式

```python
r = float(input("請輸入圓的半徑："))
pi = 3.14
area = pi * r * r
print(f"圓的面積是：{area}")
```

---

## 七、🧾 `input()` 用法

```python
a = input("請輸入一個數字")
print("輸入結束")
print(int(a) + 10)
```

> 📝 `input()` 會請你輸入文字，但記得它回來的是「文字」，要轉成數字才能做加法！

---

## 八、📄 Streamlit 的顯示指令

這些是讓程式顯示文字的指令，特別是用在網頁上的 `Streamlit`：

```python
st.write("可以顯示各種東西，例如數字、文字、表格")
st.text("只能顯示純文字")
st.markdown("可以用 Markdown 語法")
st.info("顯示提示")
st.success("顯示成功")
st.warning("顯示警告")
st.error("顯示錯誤")
```

### ✨ Markdown 是一種讓文字變好看的語法，例如：

```markdown
* **粗體**
* *斜體*
* [連結](https://www.example.com)
```

---

## 九、⚙️ 運算優先順序（誰先算？）

1. `()` 括號先算
2. `**` 次方
3. `/` 除法
4. `%` 餘數
5. `+` 加法
6. `-` 減法
7. `and`（而且）
8. `or`（或者）
9. `not`（不是）
"""
    )
