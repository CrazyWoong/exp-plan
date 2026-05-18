import streamlit as st
import pandas as pd
import datetime
import numpy

dot = datetime.datetime.now().isocalendar()[1] - 1

st.set_page_config(
    page_title="📂 EXP/MASS 계획 조회",
    layout="wide", # 화면을 넓게 사용
    initial_sidebar_state="collapsed" # 모바일에서 사이드바를 숨겨 공간 확보
)

col1, col2, col3, col4 = st.tabs([f"📋DOT {dot}주 시험용 계획", f"🏗️DOT {dot}주 양시 계획",
                                        "✨EXP History","✨MASS History"])

search = st.text_input("🔍찾으실 내용을 입력하세요")

pd.set_option('future.no_silent_downcasting', True)

with col1:
    try:
        df1 = pd.read_excel("exp_now.xlsx", header=1)
        dfs = df1.drop_duplicates(subset="ECN No.", keep='first')
        st.write(f"📌DOT {dot} 주차 시험용 반영 수량 ({len(dfs)})")
                
        if search:
            mask = df1.apply(lambda row: row.astype(str).str.contains(search, case=False).any(), axis=1)
            filtered_df = df1[mask]
            
            # filtered_df_1 = filtered_df.replace(["None", "none", ""], numpy.nan)
            # filtered_df_1 = filtered_df.ffill()
            
            st.dataframe(filtered_df, width='stretch')
        else:
            # df1 = df1.replace(["None", "none", ""], numpy.nan)
            st.dataframe(df1, width='stretch')
                
    except Exception as e:
        print(e)
        st.warning("시험용 계획 파일을 찾을 수 없습니다.")

with col2:
    try:
        df2 = pd.read_excel("mass_now.xlsx", header=1)
        st.write(f"📌DOT {dot} 주차 양시 반영 수량 ({len(df2)})")
        
        if search:
            mask_1 = df2.apply(lambda rows: rows.astype(str).str.contains(search, case=False).any(), axis=1)
            filtered_df_1 = df2[mask_1]
            
            filtered_df_1 = filtered_df_1.replace(["None", "none", ""], numpy.nan)
            filtered_df_1 = filtered_df_1.ffill()
            
            st.dataframe(filtered_df_1, width='stretch')
        else:
            df2 = df2.replace(["None", "none", ""], numpy.nan)
            df2 = df2.ffill()
            
            st.dataframe(df2, width='stretch') # use_container_width=True : 2026 new
            
    except:
        st.warning("양시 계획 파일을 찾을 수 없습니다.")
        
with col3:
    try:
        df3 = pd.read_excel("exp_list.xlsx", sheet_name="시험용", header=9)
        
        df3["DOT"] = df3["DOT"].astype("str")
        df3["DOT"] = df3["DOT"].str.zfill(2)
        df3["DOT"] = "DOT " + df3["DOT"]
        
        df3_1 = df3[["DOT", "담당", "R&D", "PI", "LINE", "ECN No.", "제조 특이 사항",
                "Product", "Size", "Pattern", "PR", "T/L", "B/W", "USE", "BR", "Spec No.", "EA.", "Plan",
                "성형기\n(OE/RE)", "ECN Purpose",
                "T/D\nCTB", "T/D\nSUT", "T/D\nTRW", "T/D\nChimney", "T/D\nDie No", "T/D\nNew/Exist", "T/D\nTotal Width",
                "S/W\nBSW", "S/W\nRIC", "S/W\nDie No", "S/W\nNew/Exist", "S/W\nWidth",
                "PA", "Belt Drum\nCircumference",
                "I/L#1\nCode", "I/L#1\nWidth", "I/L#2\nWidth",
                "C/C#1\nCode", "C/C#1\nRolled", "C/C#1\nWidth", "C/C#1\nAngle",
                "C/C#2\nCode", "C/C#2\nRolled", "C/C#2\nWidth", "C/C#2\nAngle",
                "BT#1\nCode", "BT#1\nRolled", "BT#1\nWidth", "BT#1\nAngle",
                "BT#2\nCode", "BT#2\nRolled", "BT#2\nWidth", "BT#2\nAngle",
                "JLB\nRolled", "Side Filling Tape\nWidth", "SRFM\nCode", "SRFM\nWidth", "SRFM\nAngle",
                "Bead Filler Tape\nCode", "Bead Filler Tape\nComp'd",
                "Over", "Rim Cushion Sheet\nWidth", "Special Material", "비고1", "Inch",
                "Mold No.", "Bladder\nCode", "Curing\nTime(Old)", "CTR",
                "비드\nOE", "Bead\nCode", "Bead\nBundle", "Bead\nFiller", "Bead\nBIC", "Special Notice", "Mold Ware\nStatus",
                "ISSUE","업체"]]
        
        if search:
            mask_2 = df3_1.apply(lambda row_exp: row_exp.astype(str).str.contains(search, case=False).any(), axis=1)
            filtered_df_2 = df3_1[mask_2]
        
            filtered_ecn = filtered_df_2.drop_duplicates(subset="ECN No.", keep='first')
            filtered_ecn["ECN No."].replace("None", numpy.nan)
            filtered_ecn = filtered_ecn.dropna(subset=["ECN No."]) #, inplace=True)
            st.write(f"⚡{len(filtered_ecn)} 개 ECN이 검색되었습니다.")

            filtered_df_2 = filtered_df_2.replace(["None", "none", ""], numpy.nan)
            filtered_df_2 = filtered_df_2.ffill()
            
            st.dataframe(filtered_df_2, width='stretch')       
        else:
            df3_1 = df3_1.replace(["None", "none", ""], numpy.nan)
            df3_1 = df3_1.ffill()
                        
            st.dataframe(df3_1, width='stretch')
            
    except:
        st.warning("History 파일을 찾을 수 없습니다.")

with col4:
    try:
        df4 = pd.read_excel("exp_list.xlsx", sheet_name="양시", header=8)
        
        df4["DOT"] = df4["DOT"].astype("str")
        df4["DOT"] = df4["DOT"].str.zfill(2)
        df4["DOT"] = "DOT " + df4["DOT"]
        
        df4_1 = df4[["DOT", "담당", "R&D", "PI", "LINE", "ECN No.", "제조 특이 사항",
                "Product", "Size", "Pattern", "PR", "T/L", "B/W", "USE", "BR", "Spec No.", "EA.", "Plan",
                "성형기\n(OE/RE)", "ECN Purpose",
                "T/D\nCTB", "T/D\nSUT", "T/D\nTRW", "T/D\nChimney", "T/D\nDie No", "T/D\nNew/Exist", "T/D\nTotal Width",
                "S/W\nBSW", "S/W\nRIC", "S/W\nDie No", "S/W\nNew/Exist", "S/W\nWidth",
                "PA", "Belt Drum\nCircumference",
                "I/L#1\nCode", "I/L#1\nWidth", "I/L#2\nWidth",
                "C/C#1\nCode", "C/C#1\nRolled", "C/C#1\nWidth", "C/C#1\nAngle",
                "C/C#2\nCode", "C/C#2\nRolled", "C/C#2\nWidth", "C/C#2\nAngle",
                "BT#1\nCode", "BT#1\nRolled", "BT#1\nWidth", "BT#1\nAngle",
                "BT#2\nCode", "BT#2\nRolled", "BT#2\nWidth", "BT#2\nAngle",
                "JLB\nRolled", "Side Filling Tape\nWidth", "SRFM\nCode", "SRFM\nWidth", "SRFM\nAngle",
                "Bead Filler Tape\nCode", "Bead Filler Tape\nComp'd",
                "Over", "Rim Cushion Sheet\nWidth", "Special Material", "비고1", "Inch",
                "Mold No.", "Bladder\nCode", "Curing\nTime(Old)", "CTR",
                "비드\nOE", "Bead\nCode", "Bead\nBundle", "Bead\nFiller", "Bead\nBIC", "Special Notice", "Mold Ware\nStatus",
                "ISSUE", "업체"]]
            
        if search:
            mask_3 = df4_1.apply(lambda row_mass: row_mass.astype(str).str.contains(search, case=False).any(), axis=1)
            filtered_df_3 = df4_1[mask_3]
            
            filtered_ecn_1 = filtered_df_3.drop_duplicates(subset="ECN No.", keep='first')
            filtered_ecn_1["ECN No."].replace("None", numpy.nan)
            filtered_ecn_1 = filtered_ecn_1.dropna(subset=["ECN No."]) #, inplace=True)
            st.write(f"⚡{len(filtered_ecn_1)} 개 ECN이 검색되었습니다.")
            
            filtered_df_3 = filtered_df_3.replace(["None", "none", ""], numpy.nan)
            filtered_df_3 = filtered_df_3.ffill()
            
            st.dataframe(filtered_df_3, width='stretch')
        else:
            df4_1 = df4_1.replace(["None", "none", ""], numpy.nan)
            df4_1 = df4_1.ffill()
            st.dataframe(df4_1, width='stretch')
            
    except Exception as e:
        print(e)
        st.warning("History 파일을 찾을 수 없습니다.")
