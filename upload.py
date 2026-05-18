import os
import shutil
import datetime
import glob

dot = datetime.datetime.now().isocalendar()[1] - 1

base_path = r"C:\Users\HANTA\OneDrive - HKNC\2026 PI PJT\시험용 계획 양시 계획"
plan_dir = os.path.join(base_path, "PCR LTR 시험용 계획 작성\파이썬 실행")
mold_dir = os.path.join(base_path, "양시 계획")

exp_file = glob.glob(os.path.join(plan_dir, f"DOT {dot}주차 Dp-X-*.xlsx"))
mass_file = glob.glob(os.path.join(mold_dir, f"DOT {dot}주차 Mass*.xlsx"))
exp_file = glob.glob(os.path.join(base_path, "2026년 시험 양시 규격 Total List*.xlsx"))

if exp_file:
    shutil.copy(exp_file[0], "exp_now.xlsx")
if mass_file:
    shutil.copy(mass_file[0], "mass_now.xlsx")
if exp_file:
    shutil.copy(exp_file[0], "exp_list.xlsx")

# 5. GitHub 업로드 명령 실행 (Git이 설치되어 있어야 함)
os.system("git add .")
os.system(f'git commit -m "{dot}주차 데이터 업데이트"')
os.system("git push")

print(f"{dot}주차 파일 업로드 완료!")

# cmd 에서 해당 위치 찾아가서 실행 upload : cd OneDrive - HKNC\Streamlit Python

# 에러 발생 시
# git add .
# git commit -m "temp commit for rebase"

# git pull origin main --rebase
# git push origin main