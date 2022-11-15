def attendance_report():
    
    print("Please wait: Attendance function called successfully.")
     
    roll_nums = [str(i) for i in reg_students['Roll No']]
    #we got the list of registered students given to us
   
    #to get list of dates in which lectures were taken
    date_list = list({datetime.strptime(str(i).split(" ")[0],"%d-%m-%Y").date() for i in df['Timestamp']  if datetime.strptime(str(i).split(" ")[0],"%d-%m-%Y").strftime('%a') in ['Mon','Thu']})
    date_list.sort()

    # We define a dictionary for storing the duplicate entries for each date
    duplicate = {date : {} for date in date_list}
    duplicate_info = {roll_number : {date.strftime('%d-%m-%Y') : 0 for date in date_list} for roll_number in roll_nums}
    attended_dates = {roll_number : [] for roll_number in roll_nums}
    fake_attendance=[]
    fake_info = {roll_number : {date.strftime('%d-%m-%Y') : 0 for date in date_list} for roll_number in roll_nums}
    
    
    for i in range(len(df['Timestamp'])):
        date_obj = datetime.strptime(str(df['Timestamp'][i]), '%d-%m-%Y %H:%M')
        date = date_obj.date()
        #Verify if the person attended the class on monday or thursday
        if date_obj.weekday() == 0 or date_obj.weekday() == 3:
            if(date_obj.hour<14 or date_obj.hour>=15):
                fake_attendance.append((str(df['Attendance'][i])).split(" ")[0])
                fake_info[(str(df['Attendance'][i])).split(" ")[0]][date.strftime('%d-%m-%Y')]+=1
            if(date_obj.hour==14):
                student_roll_no=(str(df['Attendance'][i])).split(" ")[0]
                if student_roll_no == 'nan' or student_roll_no not in roll_nums:
                    continue
                if student_roll_no in duplicate[date]:
                    duplicate[date][student_roll_no]['entries'].append(date_obj)
                    duplicate_info[(str(df['Attendance'][i])).split(" ")[0]][date.strftime('%d-%m-%Y')]+=1
                else:
                    duplicate[date][student_roll_no] = {'name': df['Attendance'][i].split(' ', 1)[1], 'entries': [date_obj]}
                    attended_dates[student_roll_no].append(date.strftime('%d-%m-%Y'))
                    actual_attendance.append(student_roll_no)       
        else:
            fake_attendance.append((str(df['Attendance'][i])).split(" ")[0])

    #Next task to create individual reports and consolidateed report
    
    for i in range(len(reg_students['Name'])):
        for date in date_list:
            try:
             if date.strftime('%d-%m-%Y') in attended_dates[reg_students['Roll No'][i]]:
                 dfc.at[i, date.strftime('%d-%m-%Y')]='P'
             else:
                 dfc.at[i, date.strftime('%d-%m-%Y')]='A'
            except:
                print("Error in making file")
        dfc.at[i,'Actual Lecture Taken']=len(date_list)
        dfc.at[i,'Total Real Attendance']=actual_attendance.count(reg_students['Roll No'][i])
        dfc.at[i,'Percentage (attendance_count_actual/total_lecture_taken) 2 digit decimal']=(round((dfc['Total Real Attendance'][i]/len(date_list))*100,2))
        individual = pd.DataFrame()
        individual.at[0, 'Date']=''
        for j,date in enumerate(date_list):
            individual.at[j+1, 'Date'] = date.strftime('%d-%m-%Y')
        individual.at[0,'Roll No'] = reg_students['Roll No'][i]
        individual.at[0,'Name'] = reg_students['Name'][i]
        individual.at[0,'total_attendance_count']=''
        individual.at[0,'Real']=actual_attendance.count(reg_students['Roll No'][i])
        individual.at[0,'Absent']=len(date_list)-actual_attendance.count(reg_students['Roll No'][i])
        for j,date in enumerate(date_list):
            individual.at[j+1,'invalid']=fake_info[(str(df['Attendance'][i])).split(" ")[0]][date.strftime('%d-%m-%Y')]
            individual.at[j+1, 'duplicate']=duplicate_info[reg_students['Roll No'][i]][date.strftime('%d-%m-%Y')]
            if date.strftime('%d-%m-%Y') in attended_dates[reg_students['Roll No'][i]]:
                individual.at[j+1, 'Real']=1
                individual.at[j+1, 'Absent']=0
            else:
                individual.at[j+1, 'Absent']=1
                individual.at[j+1, 'Real']=0
            individual.at[j+1, 'total_attendance_count']=individual.at[j+1, 'Real']+individual.at[j+1,'invalid']+individual.at[j+1, 'duplicate']
        try:
            individual.to_excel('output/' + reg_students['Roll No'][i] + '.xlsx',index=False)
        except PermissionError:
            print("You don't have the permission to read/write in this directory. Please grant permission or change the working directory")

    
    
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
    
    reg_students=pd.read_csv("input_registered_students.csv")
    df=pd.read_csv("input_attendance.csv")
    dfc=pd.DataFrame()

    dfc['Roll']=reg_students['Roll No'].copy()
    dfc['Name']=reg_students['Name'].copy()

    actual_attendance=[]
    try:
     attendance_report()
    except:
     print("Error while fumction calling")
    try:
        dfc.to_excel('./output/attendance_report_consolidated1.xlsx',index=False)
    except:
        print("You don't have the permission to read/write in this directory. Please grant permission or change the working directory")

except FileNotFoundError:
  
    print("File could not be found in the parent directory")

except ImportError:
    
    print("Sorry, module 'Pandas' could not be imported")

except PermissionError:
    print("You don't have the permission to read/write in this directory. Please grant permission or change the working directory")


#these are last lines of the code
print("Output files are created successfully :] ")   
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))