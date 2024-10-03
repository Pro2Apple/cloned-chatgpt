import streamlit as st

name = st.text_input("请输入您的名字：")
if name:
    st.write(f"你好，{name}")

st.divider()

password = st.text_input("请输入您的密码：", type = "password")

st.divider()
st.divider()
st.divider()

paragraph = st.text_area("请输入一段自我介绍")

st.divider()
age = st.number_input("请输入您的年龄：", value = 20, min_value=0, max_value=100, step = 5)

st.write(f"您的年龄是：{age}岁")

st.divider()

check = st.checkbox("我同意以上条款。")

if check:
    st.write("感谢您接受服务条款。您可以开始使用啦。")

st.divider()
submitted = st.button("提交")

if submitted:
    st.write("提交成功！")