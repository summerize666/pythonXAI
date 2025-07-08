# 🐍Python class2 筆記 ✨

## 一、🔁 資料轉換（型態轉換）

有時候我們需要把一種資料變成另一種，像這樣：

| 原本              | 轉換方式         | 結果              |
| ----------------- | ---------------- | ----------------- |
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
- **粗體**
- _斜體_
- [連結](https://www.example.com)
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
