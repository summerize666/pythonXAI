# Python 程式學習筆記 class4

### 1. 數學運算（計算東西的規則）

我們可以用「=」來存東西，然後用「+=、-=、\*=、/=」來做加減乘除的簡單計算：

```python
a = 1   # 把1放到a裡面
a += 1  # a變成a+1，也就是2
a -= 1  # a變成a-1，也就是1
a *= 2  # a變成a*2，也就是2
a /= 2  # a變成a/2，也就是1.0
```

運算的順序要記得：

- 括號()最重要
- 次方（像 2 的 3 次方）
- 乘、除、取餘數（%）
- 加、減
- 邏輯判斷（not, and, or）

---

### 2. 重複做事情：迴圈

- **while 迴圈**：當條件是對的，就一直重複做。

```python
i = 0
while i < 5:
    print(i)   # 印出i
    i += 1     # i加1
```

- **for 迴圈**：可以重複做固定次數。

```python
for i in range(5):
    print(i)   # 會印出0到4
```

---

### 3. 隨機數字遊戲

用 `random` 這個工具，可以讓電腦挑一個隨機數字！

```python
import random
num = random.randint(1, 100)  # 從1到100中選一個數字
```

你可以寫一個猜數字遊戲，讓電腦說你猜的數字是太大、太小還是正確。

---

### 4. 字典（存東西的小箱子）

字典可以幫你用名字找東西：

```python
d = {"apple": 20, "banana": 30}
print(d["apple"])  # 找出apple的數量是20
```

可以用迴圈看所有的東西和數量：

```python
for k, v in d.items():
    print(k, v)  # 印出每個水果和它的數量
```

你也可以改字典裡的東西，或是刪除：

```python
d["apple"] = 10  # 改成10
d.pop("banana")  # 刪除banana
```

---

### 5. 用 Streamlit 做簡單網頁

Streamlit 是一個幫你快速做網頁的工具，可以做按鈕、輸入框等等。

- **標題**：

```python
import streamlit as st
st.title("我的第一個網頁")
```

- **按鈕和輸入框**：

```python
item = st.text_input("請輸入商品")
if st.button("加入購物籃"):
    st.write(f"你加入了 {item}")
```

- **用欄位（columns）排版**：

```python
col1, col2 = st.columns(2)
with col1:
    st.button("按鈕1")
with col2:
    st.button("按鈕2")
```

- **購物籃功能**：

用 `st.session_state` 來記住你加了什麼東西，關掉網頁還能記得！

---

### 6. 重要小提醒

- **條件判斷**用 `if`、`elif`、`else`。
- **用 break 可以跳出迴圈**。
- **session_state**可以幫你記住變數的值。

---

# 小結

今天學到：

- 算術運算和優先順序
- while 和 for 迴圈
- 隨機數字和猜數字遊戲
- 字典的用法（存東西的盒子）
- 用 Streamlit 做簡單的網頁介面
- 用欄位排版和按鈕互動
- 用 session_state 記住資料

希望你能用這些指令做出很酷的程式喔！
