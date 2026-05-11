import streamlit as st
import pandas as pd

st.title("📂 주차별 계획 실시간 조회")

col1, col2 = st.tabs(["📋 시험용 계획", "🏗️ 양시 계획"])

with col1:
    try:
        df1 = pd.read_excel("plan_now.xlsx")
        st.dataframe(df1)
    except:
        st.warning("시험용 계획 파일을 찾을 수 없습니다.")

with col2:
    try:
        df2 = pd.read_excel("mold_now.xlsx")
        st.dataframe(df2)
    except:
        st.warning("양시 계획 파일을 찾을 수 없습니다.")