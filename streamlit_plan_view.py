import streamlit as st
import pandas as pd

st.set_page_config(page_title="EXP/MASS PLAN", layout="wide")
# st.title("")

uploaded_file = st.file_uploader("엑셀 파일을 업로드하세요", type=['xlsx', 'xls'])

if uploaded_file:
    df = pd.read_excel(uploaded_file, header=1)

    search_term = st.text_input("🔍 검색어를 입력하세요 (예: 상품명, 이름)")

    if search_term:
        # 모든 컬럼에서 검색어가 포함된 행만 필터링
        filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_term).any(), axis=1)]
        st.write(f"검색 결과: {len(filtered_df)}건")
        st.dataframe(filtered_df) # 모바일에서도 표가 깔끔하게 보임
    else:
        st.write("전체 데이터 미리보기:")
        st.dataframe(df)

else:
    st.info("파일을 업로드하면 조회를 시작할 수 있습니다.")