from platform import python_version
from datetime import datetime
start_time = datetime.now()

ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")
import pandas as pd
import csv
# We read the input files into a pandas dataframe each
reg_students=pd.read_csv("input_registered_students.csv")
df=pd.read_csv("input_attendance.csv")
dfc=pd.DataFrame()

dfc['Roll']=reg_students['Roll No'].copy()
dfc['Name']=reg_students['Name'].copy()

actual_attendance=[]
attendance_report()