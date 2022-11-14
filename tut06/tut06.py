def attendance_report():

    roll_nums = [str(i) for i in all_students['Roll No']]

    #we have now the list of all students and roll numbers

    #to get list of dates in which lectures were taken considering all  'Monday' and 'Thursday'
    date_list = list({datetime.strptime(str(i).split(" ")[0],"%d-%m-%Y").date() for i in df['Timestamp']  if datetime.strptime(str(i).split(" ")[0],"%d-%m-%Y").strftime('%a') in ['Mon','Thu']})
    date_list.sort()
    # We define a dictionary for storing the duplicate entries for each date
    duplicate = {date : {} for date in date_list}
    duplicate_info = {roll_number : {date.strftime('%d-%m-%Y') : 0 for date in date_list} for roll_number in roll_nums}
    attended_dates = {roll_number : [] for roll_number in roll_nums}
    fake_attendance=[]
    fake_info = {roll_number : {date.strftime('%d-%m-%Y') : 0 for date in date_list} for roll_number in roll_nums}

try:
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
    # We read the input files into a pandas dataframe
    all_students=pd.read_csv("input_registered_students.csv")
    df=pd.read_csv("input_attendance.csv")
    dfc=pd.DataFrame()

    dfc['Roll']=all_students['Roll No'].copy()
    dfc['Name']=all_students['Name'].copy()

    actual_attendance=[]
    attendance_report()
    try:
        dfc.to_excel('./output/attendance_report_consolidated.xlsx',index=False)
    except:
        print("You don't have the permission to read/write in this directory. Please grant permission or change the working directory")

except FileNotFoundError:
    print("Error: File not found in the parent directory.")
except ImportError:
    print("Error: While importing the module 'pandas'.")
except PermissionError:
    print("Error: Permission to read/write in this directory was denied.")


#last lines of the code
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
