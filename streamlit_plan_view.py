import streamlit as st
import pandas as pd

import streamlit as st
import pandas as pd

st.set_page_config(page_title="EXP/MASS PLAN", layout="wide")
# st.title("📂 다중 엑셀 데이터 조회")

# accept_multiple_files=True 옵션을 추가합니다.
# uploaded_files = st.file_uploader(
#     "엑셀 파일들을 업로드하세요 (여러 개 가능)", 
#     type=['xlsx', 'xls'], 
#     accept_multiple_files=True
# )

import datetime
import glob

date = datetime.date.today()
dot = datetime.datetime.now().isocalendar()[1] - 1

file_path_full = glob.glob(r"C:\Users\HANTA\OneDrive - HKNC\2026 PI PJT\시험용 계획 양시 계획\PCR LTR 시험용 계획 작성\파이썬 실행\DOT " + str(dot) + "주차 Dp-X-*.xlsx")
mold_path_full = glob.glob(r"C:\Users\HANTA\OneDrive - HKNC\2026 PI PJT\시험용 계획 양시 계획\양시 계획\DOT " + str(dot) + "주차 Mass*.xlsx")

uploaded_files = [file_path_full, mold_path_full]

if uploaded_files:
    # 파일 이름을 리스트로 만들어 탭 생성
    file_names = [file.name for file in uploaded_files]
    tabs = st.tabs(file_names)

    for i, file in enumerate(uploaded_files):
        with tabs[i]:
            df = pd.read_excel(file, header=1)
            
            # 요약 정보 보여주기
            st.subheader(f"📄 {file.name} 데이터")
            # st.write(f"전체 행 수: {len(df)}개 / 컬럼 수: {len(df.columns)}개")
            
            # 검색 기능 (각 탭마다 별도로 작동)
            search = st.text_input(f"🔍 {file.name} 내 검색", key=f"search_{i}")
            
            if search:
                filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search).any(), axis=1)]
                st.dataframe(filtered_df, use_container_width=True)
            else:
                st.dataframe(df, use_container_width=True)
else:
    st.info("비교하거나 조회할 엑셀 파일들을 먼저 업로드해 주세요.")
    
# Github에 파일 올리고 steamlit cloud 에서 공유