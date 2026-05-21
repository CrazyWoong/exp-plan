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

def color_weekday(val):
    if "월" in val :
        color = 'color: #FFFF00'
    elif '화' in val :
        color = 'color: #FF6600'
    elif '수' in val :
        color = 'color: #00CC00'
    elif '목' in val :
        color = 'color: #FF33CC'
    elif '금' in val :
        color = 'color: #0066FF'
    else:
        color = 'color: #FFFFFF'
    return color

with col1:
    try:
        df1 = pd.read_excel("exp_now.xlsx", header=1)
        dfs = df1.drop_duplicates(subset="ECN No.", keep='first')
        st.write(f"📌DOT {dot} 주차 시험용 반영 수량 ({len(dfs)})")
        
        df1_1 = df1[["담당", "R&D", "PI", "LINE", "ECN No.", "제조 특이 사항",
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
                "Over", "Rim Cushion Sheet\nWidth", "Special Material",
                "Mold No.", "Bladder\nCode", "Curing\nTime(Old)", "CTR",
                "Bead\nCode", "Bead\nBundle", "Bead\nFiller", "Bead\nBIC", "Special Notice", "Mold Ware\nStatus", "업체"]]
                
        if search:
            mask = df1_1.apply(lambda row: row.astype(str).str.contains(search, case=False).any(), axis=1)
            filtered_df = df1_1[mask]
            s_df = filtered_df.style.map(color_weekday, subset=['Plan'])
            st.dataframe(s_df, width='stretch')
        else:
            styled_df = df1_1.style.map(color_weekday, subset=['Plan'])
            st.dataframe(styled_df, width='stretch')
                
    except:
        st.warning("시험용 계획 파일을 찾을 수 없습니다.")

with col2:
    try:
        df2 = pd.read_excel("mass_now.xlsx", header=1)
        st.write(f"📌DOT {dot} 주차 양시 반영 수량 ({len(df2)})")
        
        df2_1 = df2[["담당", "R&D", "PI", "LINE", "ECN No.", "제조 특이 사항",
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
                "Over", "Rim Cushion Sheet\nWidth", "Special Material",
                "Mold No.", "Bladder\nCode", "Curing\nTime(Old)", "CTR",
                "Bead\nCode", "Bead\nBundle", "Bead\nFiller", "Bead\nBIC", "Special Notice", "Mold Ware\nStatus", "업체"]]
        
        if search:
            mask_1 = df2_1.apply(lambda rows: rows.astype(str).str.contains(search, case=False).any(), axis=1)
            filtered_df_1 = df2_1[mask_1]
            s_df_1 = filtered_df_1.style.map(color_weekday, subset=['Plan'])
            st.dataframe(s_df_1, width='stretch')
        else:
            styled_df_1 = df2_1.style.map(color_weekday, subset=['Plan'])
            st.dataframe(styled_df_1, width='stretch')
            
    except:
        st.warning("양시 계획 파일을 찾을 수 없습니다.")
        
with col3:
    try:
        df3 = pd.read_excel("exp_list.xlsx", sheet_name="시험용", header=9)
        
        df3["DOT"] = df3["DOT"].astype("str")
        df3["DOT"] = df3["DOT"].str.zfill(2)
        df3["DOT"] = "DOT " + df3["DOT"]
        
        # df3 = df3.astype("str")
        # df3 = df3.map(lambda x: str(x).replace('.0', '') if x.endswith('.0') else x)
        
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
            filtered_ecn["ECN No."] = filtered_ecn["ECN No."].replace(["None", "none", "nan", ""], numpy.nan)
            filtered_ecn = filtered_ecn.dropna(subset=["ECN No."]) #, inplace=True)
            st.write(f"⚡{len(filtered_ecn)} 개 ECN이 검색되었습니다.")
            
            filtered_df_2 = filtered_df_2.replace(["None", "none", "nan", ""], numpy.nan)
            filtered_df_2 = filtered_df_2.ffill()
            
            s_df_2 = filtered_df_2.style.map(color_weekday, subset=['Plan'])
            st.dataframe(s_df_2, column_config={"ISSUE" : st.column_config.Column(width=250)}, width='stretch')
        else:
            df3_1 = df3_1.replace(["None", "none", "nan", ""], numpy.nan)
            df3_1 = df3_1.ffill()
            
            styled_df_2 = df3_1.style.map(color_weekday, subset=['Plan'])
            styled_df_2 = styled_df_2.style.format(precison=0)
            st.dataframe(styled_df_2, column_config={"ISSUE" : st.column_config.Column(width=250)}, width='stretch')
            
    except Exception as e:
        st.write(e)
        st.warning("History 파일을 찾을 수 없습니다.")

with col4:
    try:
        df4 = pd.read_excel("exp_list.xlsx", sheet_name="양시", header=8)
        
        df4["DOT"] = df4["DOT"].astype("str")
        df4["DOT"] = df4["DOT"].str.zfill(2)
        df4["DOT"] = "DOT " + df4["DOT"]
        
        df4 = df4.astype("str")
        df4 = df4.map(lambda x: str(x).replace('.0', '') if x.endswith('.0') else x)
        
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
            filtered_ecn_1["ECN No."] = filtered_ecn_1["ECN No."].replace(["None", "none", "nan", ""], numpy.nan)
            filtered_ecn_1 = filtered_ecn_1.dropna(subset=["ECN No."]) #, inplace=True)
            st.write(f"⚡{len(filtered_ecn_1)} 개 ECN이 검색되었습니다.")
            
            s_df_3 = filtered_df_3.style.map(color_weekday, subset=['Plan'])
            st.dataframe(s_df_3, column_config={"ISSUE" : st.column_config.Column(width=250)}, width='stretch') 
        else:
            styled_df_3 = df4_1.style.map(color_weekday, subset=['Plan'])
            st.dataframe(styled_df_3, column_config={"ISSUE" : st.column_config.Column(width=250)}, width='stretch')
            
    except:
        st.warning("History 파일을 찾을 수 없습니다.")
