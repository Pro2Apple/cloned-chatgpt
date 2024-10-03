import streamlit as st

tab1, tab2, tab3 = st.tabs(["性别", "联系方式", "喜欢吃的水果"])


with st.sidebar:

    name = st.text_input("请输入您的名字：")
    if name:
        st.write(f"你好，{name}")
    st.divider()

with tab1:
    password = st.text_input("请输入您的密码：", type = "password")
    st.divider()
    sex = st.radio("您的性别是：", ["男", "女", "不愿透漏"])
    if sex:
        st.write(f"您的性别为：{sex}")

    st.divider()
    st.divider()


with tab2:
    contact = st.write("您希望我们可以通过什么方式联系到您？")
    st.checkbox("电话")
    st.checkbox("微信")
    st.checkbox("QQ")
    st.checkbox("电子邮件")

    st.divider()

with tab3:
    fruits = st.multiselect("您喜欢的水果是什么", ["Apple", "Banana", "Orange", "Cherry"])
    for fruit in fruits:
        st.write(f"你喜欢吃的水果是{fruit}")
    age = st.number_input("请输入您的年龄：", value = 20, min_value=0, max_value=100, step = 5)

    st.write(f"您的年龄是：{age}岁")

    st.divider()


with st.expander("身高信息"):

    check = st.checkbox("我同意以上条款。")

    if check:
        st.write("感谢您接受服务条款。您可以开始使用啦。")

st.divider()
submitted = st.button("提交")

if submitted:
    st.write("提交成功！")

