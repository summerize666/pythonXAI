import streamlit as st

st.write("## 按鈕練習")
st.button("按我一下", key="bnt1")
if st.button("按我一下", key="bnt2"):
    st.balloons()
if st.button("按我一下", key="bnt3"):
    st.snow()
    st.write("---")
st.write("## 數字金字塔")
num = st.number_input("請輸入一個數1到9", min_value=1, max_value=9, step=1)
for i in range(1, num + 1):
    st.write(f"{i} " * i)
