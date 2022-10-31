from multiprocessing.reduction import duplicate
from platform import python_version
import os
import pandas as pd

# DateTime module to measure the execution time of the program
from datetime import datetime as dt
start_time = dt.now()

try:
    att_df = pd.read_csv("input_attendance.csv")
    stud_df = pd.read_csv("input_registered_students.csv")

except Exception as e: 
    print("There was some error due to " + str(e))
os.mkdir('output2')
total_studs = len(stud_df.axes[0])
total_attendance = len(att_df.axes[0])

total_lecture_taken = 0

att_df["Timestamp"] = pd.to_datetime(att_df["Timestamp"], format = '%d/%m/%Y %H:%M:%S')

student = att_df["Attendance"].str.split(" ", n = 1, expand = True)
att_df["Roll No"] = student[0]
att_df["Name"] = student[1]

unique_dates = att_df["Timestamp"].map(lambda timestamp: timestamp.date()).unique()
for timestamp in unique_dates:
    if(timestamp.weekday() == 0 or timestamp.weekday() == 3):
        total_lecture_taken += 1
open_time = dt.strptime('14:00:00', '%H:%M:%S').time()
close_time = dt.strptime('15:00:00', '%H:%M:%S').time()
consolidate_df = pd.DataFrame()
duplicate_df = pd.DataFrame()
def attendance_report():
    for i in range(total_studs):
        attendance_count_actual = 0
        attendance_count_fake = 0
        # attendance_count_absent = 0
        for j in range(total_attendance):
            if(stud_df.at[i, "Roll No"] == att_df.at[j, "Roll No"]):
                if(att_df.at[j, "Timestamp"].weekday() == 0 or att_df.at[j, "Timestamp"].weekday() == 3 or 
                att_df.at[j, "Timestamp"].time() >= open_time or att_df.at[j, "Timestamp"].time() < close_time):
                    attendance_count_actual += 1
                else:
                    attendance_count_fake += 1
                temp_df = pd.DataFrame()
                temp_df.at[0, "Roll No"] = consolidate_df.at[i, "Roll No"] = stud_df.at[i, "Roll No"]
                temp_df.at[0, "Name"] = consolidate_df.at[i, "Name"] = stud_df.at[i, "Name"]
                temp_df.at[0, "Total Lecture Taken"] = consolidate_df.at[i, "Total Lecture Taken"] = total_lecture_taken
                temp_df.at[0, "Attendance Count Actual"] = consolidate_df.at[i, "Attendance Count Actual"] = attendance_count_actual
                temp_df.at[0, "Attendance Count Fake"] = consolidate_df.at[i, "Attendance Count Fake"] = attendance_count_fake
                temp_df.at[0, "Attendance Count Absent"] = consolidate_df.at[i, "Attendance Count Absent"] = total_lecture_taken - attendance_count_actual
                temp_df.at[0, "Percentage (Attendance Count Actual/Total Lecture Taken)"] = consolidate_df.at[i, "Percentage (Attendance Count Actual/Total Lecture Taken)"] = (attendance_count_actual/total_lecture_taken)*100
                temp_df.to_csv(f'output1/{temp_df.at[0, "Roll No"]}.csv', index = False)
                break
        # duplicate_df.at[i, "Roll No"] = stud_df.at[i, "Roll No"]
        # duplicate_df.at[i, "Name"] = stud_df.at[i, "Name"]
        # duplicate_df.at[i, "Total count of attendance on that day"] = len(att_df[att_df["Timestamp"]])
    consolidate_df.to_csv(f'output1/attendance_report_consolidated.csv', index = False)




ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


attendance_report()

#This shall be the last lines of the code.
end_time = dt.now()
print('Duration of Program Execution: {}'.format(start_time - end_time))
