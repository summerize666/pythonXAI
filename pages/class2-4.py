import streamlit as st

nuber = st.number_input("請輸入一個數字:", step=1, min_value=0, max_value=10000)
st.write(f"你輸入的數字是：{nuber}")
st.write("---")
st.write("##練習")
score = st.number_input("請輸入的分數", min_value=0, max_value=100, step=1)
if score >= 90:
    st.write("你得到了A")
elif score >= 80:
    st.write("你得到了B！")
elif score >= 70:
    st.write("你得到了C！")
elif score >= 60:
    st.write("你得到了D！")
else:
    st.write("你拿到了和大熊做朋友的機會 ")
