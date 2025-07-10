import streamlit as st

st.title("欄位元件")
(
    col1,
    col2,
) = st.columns(2)
col1.button("按鈕1", key="btn1")
col2.button("按鈕2", key="btn2")
(
    col1,
    col2,
) = st.columns([1, 2])
col1.button("按鈕3", key="btn3")
col2.button("按鈕4", key="btn4")
col1, col2, col3 = st.columns([1, 2, 3])
col1.button("按鈕5", key="btn5")
col2.button("按鈕6", key="btn6")
col3.button("按鈕7", key="btn7")
st.write("---")
col1, col2 = st.columns([1, 2])
with col1:
    st.write("這是col1")
    if st.button("按鈕8", key="btn8"):
        st.balloons()
with col2:
    st.write("這是col2")
    st.button("按鈕9", key="btn9")
cols = st.columns(4)
for i in range(len(cols)):
    with cols[i]:
        st.write(f"for當中的按鈕{i+1}", key=f"多col{i+10}")
st.write("---")
st.title("columns排列元素比較")
(
    col1,
    col2,
) = st.columns(2)
with col1:
    st.button("按鈕1", key="btn10")
    st.button("按鈕2", key="btn11")
    st.button("按鈕3", key="btn12")
with col2:
    st.write("這是col2")
    st.write("這是col2")
    st.write("這是col2")
st.write("---")
for i in range(3):
    col1, col2 = st.columns(2)
    with col1:
        st.button(f"按鈕{i+1}", key=f"排版測試{i+4}")
        with col2:
            st.write(f"這是col2{i+1}")
st.write("---")
st.title("文字輸入元件")
text = st.text_input("請輸入一個文字", value="這是預設文字")
st.write(f"你輸入的文字是：{text}")
st.write("---")
st.title("session_state")
ans = 1
if st.button("按下去and家1", key="and"):
    ans = ans + 1
st.write(f"ans={ans}")
if "ans1" not in st.session_state:
    st.session_state.ans1 = 1
if st.button("按下去ans加1", key="ans2"):
    st.session_state.ans1 = st.session_state.ans1 + 1
    st.write(f"ans={st.session_state.ans1}")
    if st.button("重新整理", key="banana"):
        st.rerun()
