import streamlit as st

st.chat_message("user").write("這是使用者的訊息")
st.chat_message("assistant").write("這是AI的訊息")
history = [
    {"role": "user", "content": "你好,AI!"},
    {"role": "assistant", "content": "你好,使用者!"},
    {"role": "user", "content": "請問st.chat_message()怎摸用？"},
    {
        "role": "assistant",
        "content": "st.chat_message()是用來在網頁上顯示訊息的函式，可以用來顯示使用者的訊息和AI的訊息。",
    },
]
for message in history:
    if message["role"] == "user":
        st.chat_message("user", avatar="👤").write(message["content"])
    else:
        st.chat_message("assistant", avatar="👤").write(message["content"])
