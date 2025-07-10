import streamlit as st

st.title("簡單點餐機")

if "cart" not in st.session_state:
    st.session_state.cart = []

# 用兩欄，左邊放輸入框，右邊放按鈕
col1, col2 = st.columns([4, 1])

with col1:
    item = st.text_input("請輸入商品")

with col2:
    if st.button("加入購物籃"):
        st.session_state.cart.append(item)
        st.success(f"已加入 {item}！")

st.write("購物籃：")
if st.session_state.cart:
    for i in range(len(st.session_state.cart)):
        st.write(st.session_state.cart[i])
        if st.button("刪除", key=f"del_{i}"):
            st.session_state.cart.pop(i)
            st.rerun()
else:
    st.write("購物籃是空的")
