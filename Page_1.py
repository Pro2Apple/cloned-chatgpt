import streamlit as st
import pandas as pd

"OpenAI"

a = 1.5

a

[11, 22, 33]

{"a" : 1, "b" : 2, "c" : 3}

st.title("欢迎来到我的个人网站 💡")

st.image("https://www.apple.com.cn/v/home/br/images/heroes/iphone-16-pro/hero_iphone16pro_avail__fnf0f9x70jiy_large_2x.jpg", width = 600)

df = pd.DataFrame({"学号": ["01", "02", "03", "04", "05"],
                   "班级": ["二班", "一班", "二班", "三班", "一班"],
                   "成绩": [92, 67, 70, 88, 79]})


st.dataframe(df)

st.divider()

st.table(df)