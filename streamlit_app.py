from io import StringIO
import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv("aid_summary.csv")
# 创建一个国家列表供用户选择
country_list = df['Country Name'].unique().tolist()
# 使用 Streamlit 的下拉列表
selected_country = st.selectbox('Select a country:', country_list)

# 筛选 DataFrame 以只包含选定国家的数据
country_data = df[df['Country Name'] == selected_country]

# 使用 Plotly Express 创建条形图
fig = px.bar(
    country_data,
    x='Fiscal Year',
    y='Total Aid Disbursement',
    color='Foreign Assistance Objective Name',
    barmode='group',
    title=f'Aid to {selected_country} by Year and Objective',
    labels={'Total Aid Disbursement': 'Total Aid Disbursement', 'Fiscal Year': 'Fiscal Year'}
)

# 显示图表
# fig.show()

st.plotly_chart(fig)

# 创建一个 CSV 文件内容的字符串
csv_buffer = StringIO()
country_data.to_csv(csv_buffer, index=False)
csv_str = csv_buffer.getvalue()

# 添加下载按钮
st.download_button(
    label="Download data as CSV",
    data=csv_str,
    file_name=f"{selected_country}_aid_data.csv",
    mime="text/csv",
)