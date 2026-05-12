import streamlit as st
import pandas as pd

# st.title("📂 주차별 계획 실시간 조회")

st.set_page_config(
    page_title="📂 EXP/MASS 계획 조회",
    layout="wide", # 화면을 넓게 사용
    initial_sidebar_state="collapsed" # 모바일에서 사이드바를 숨겨 공간 확보
)

col1, col2 = st.tabs(["📋 시험용 계획", "🏗️ 양시 계획"])

search = st.text_input("🔍 찾으실 내용을 입력하세요")

with col1:
    try:
        df1 = pd.read_excel("exp_now.xlsx", header=1)
        # st.dataframe(df1)
        
        if search:
            # 모든 셀을 문자열로 바꿔서 검색어 포함 여부 확인
            mask = df1.apply(lambda row: row.astype(str).str.contains(search, case=False).any(), axis=1)
            filtered_df = df1[mask]
            st.dataframe(filtered_df, width='stretch')
        else:
            st.dataframe(df1, width='stretch')
                
    except:
        st.warning("시험용 계획 파일을 찾을 수 없습니다.")

with col2:
    try:
        df2 = pd.read_excel("mass_now.xlsx", header=1)
        # st.dataframe(df2)
        
        if search:
            # 모든 셀을 문자열로 바꿔서 검색어 포함 여부 확인
            mask_1 = df2.apply(lambda rows: rows.astype(str).str.contains(search, case=False).any(), axis=1)
            filtered_df_1 = df2[mask_1]
            st.dataframe(filtered_df_1, width='stretch')
        else:
            st.dataframe(df2, width='stretch') # use_container_width=True : 2026 new
            
    except:
        st.warning("양시 계획 파일을 찾을 수 없습니다.")
        
