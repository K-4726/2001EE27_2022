from platform import python_version
import math
import glob
import os
import pandas as pd
from datetime import datetime
start_time = datetime.now()
import threading

# firstly we have to create columns
# " " , "Octant Id" , "+1" ..... "-4" , "+1 " ..... "-4 " , "   ", "    " for integrating 5th tutorial
# 1 , 3, 4 spaces empty columns 

graph = {0:"+1 " , 1:"-1 "  , 2:"+2 "  , 3:"-2 "  , 4:"+3 "  , 5:"-3 "  , 6:"+4 "  , 7:"-4 "}


# first of all we have to copy tut 4

def octant_longest_subsequence_count(velocity):

    num = len(velocity)
    #first steps are to calculate mean,val-mean etc
    velocity.loc[0, "U_Avg"] = velocity["U"].mean()
    velocity.loc[0, "V_Avg"] = velocity["V"].mean()
    velocity.loc[0, "W_Avg"] = velocity["W"].mean()
    u_mean = velocity["U"].mean()
    v_mean = velocity["V"].mean()
    w_mean = velocity["W"].mean()
    velocity["u_"] = velocity["U"]-u_mean
    velocity["v_"] = velocity["V"]-v_mean
    velocity["w_"] = velocity["W"]-w_mean
    velocity.loc[((velocity.u_ > 0) & (velocity.v_ > 0) & (velocity.w_ > 0)), "Octant"] = "+1"
    velocity.loc[((velocity.u_ > 0) & (velocity.v_ > 0) & (velocity.w_ < 0)), "Octant"] = "-1"
    velocity.loc[((velocity.u_ > 0) & (velocity.v_ > 0) & (velocity.w_ < 0)), "Octant"] = "-1"
    velocity.loc[((velocity.u_ < 0) & (velocity.v_ > 0) & (velocity.w_ > 0)), "Octant"] = "+2"
    velocity.loc[((velocity.u_ < 0) & (velocity.v_ > 0) & (velocity.w_ < 0)), "Octant"] = "-2"
    velocity.loc[((velocity.u_ < 0) & (velocity.v_ < 0) & (velocity.w_ > 0)), "Octant"] = "+3"
    velocity.loc[((velocity.u_ < 0) & (velocity.v_ < 0) & (velocity.w_ < 0)), "Octant"] = "-3"
    velocity.loc[((velocity.u_ > 0) & (velocity.v_ < 0) & (velocity.w_ > 0)), "Octant"] = "+4"
    velocity.loc[((velocity.u_ > 0) & (velocity.v_ < 0) & (velocity.w_ < 0)), "Octant"] = "-4"
    longSub = {"-1": 0, "+1": 0,  "-2": 0, "+2": 0,
               "-3": 0, "+3": 0, "-4": 0, "+4": 0}
#now we have to make columns
#six spaces empty column
    velocity["      "] = " "
    velocity["count"] = ""
    velocity["Longest Subsquence Length"] = ""
    velocity["Count"] = ""
#and now same for seven empty space
    velocity["       "] = " " 
    velocity["count2"] = ""
    velocity["Longest Subsquence Length2"] = ""
    velocity["Count2"] = ""
    #columns filling
    i = 0
    #now we have to count longest Subsequence Length
    while i < num:
        octant1 = velocity["Octant"][i]
        current_cnt = 0
        j = i
        while j < num:
            octant2 = velocity["Octant"][j]
            if (octant2 == octant1):
                current_cnt += 1
            else:
                break
            j += 1
        longSub[velocity["Octant"][i]] = max(longSub[velocity["Octant"][i]], current_cnt)
        i = j
    #  creating a map for count and i
    mapss = {0: "+1", 1: "-1",  2: "+2", 3: "-2",
               4: "+3", 5: "-3", 6: "+4", 7: "-4"}
    for i in range(8):
        velocity.loc[i, "count"] = mapss[i]
        print("row not found")
    # adding a try except for longest subsequence 
    for i in range(8):
        try:
            velocity.loc[i, "Longest Subsquence Length"] = longSub[mapss[i]]
        except:
            print("row not found")

    i = 0
    # for each octant we the fo=ind out the count of Long_Sub_Len
    cnt_Long_Sub = {"-1": 0, "+1": 0,  "-2": 0,
                  "+2": 0, "-3": 0, "+3": 0, "-4": 0, "+4": 0}
    #  for each octant's longest subsequence Creating list of strings(T Ranges)
    rangeLongSub = {"-1": [], "+1": [],  "-2": [],
                    "+2": [], "-3": [], "+3": [], "-4": [], "+4": []}

    while i < num:
        current_cnt = 0
        octant1 = ""
        try:
            j = i
            octant1 = velocity["Octant"][i]
            while j < num:

                octant2 = velocity["Octant"][j]
                if (octant2 == octant1):
                    current_cnt += 1
                else:
                    break
                j += 1
                
            if (current_cnt == longSub[octant1]):
                cnt_Long_Sub[octant1] += 1
                # form i till j-1
                try:
                    limeRange = str(velocity["T"][i]) + "," + str(velocity["T"][j-1])
                    rangeLongSub[octant1].append(limeRange)
                except:
                    print("Invalid mod value or invalid data or Excel file is empty")

            i = j
        except:
            print("row not found")
     
    
    # for TRange in rangeLongSub["-2"]:
    #     lst = TRange.split(",")
    #     print(lst[0], lst[1])
        
    index2 = 0
    for index1 in range(8):
        velocity.loc[index1, "Count"] = cnt_Long_Sub[mapss[index1]]
        currOctant = mapss[index1]

        velocity.loc[index2, "count2"] = currOctant
        velocity.loc[index2, "Longest Subsquence Length2"] = longSub[currOctant]
        velocity.loc[index2, "Count2"] = cnt_Long_Sub[currOctant]

        index2 += 1
        velocity.loc[index2, "count2"] = "T"
        velocity.loc[index2, "Longest Subsquence Length2"] = "From"
        velocity.loc[index2, "Count2"] = "To"

        index2 += 1
        for TRange in rangeLongSub[currOctant]:
            lst = TRange.split(",")
            velocity.loc[index2, "Longest Subsquence Length2"] = str(lst[0])
            velocity.loc[index2, "Count2"] = str(lst[1])
            index2 += 1

#Now lets integrate tut 2
def octant_range_names(velocity, mod=5000):
    num = len(velocity)
    
    octant_name_id_mapping = {"+1 ": "Internal outward interaction", "-1 ": "External outward interaction", "+2 ": "External Ejection",
                              "-2 ": "Internal Ejection", "+3 ": "External inward interaction", "-3 ": "Internal inward interaction", "+4 ": "Internal sweep", "-4 ": "External sweep"}
    velocity.loc[0, "U_Avg"] = velocity["U"].mean()
    velocity.loc[0, "V_Avg"] = velocity["V"].mean()
    velocity.loc[0, "W_Avg"] = velocity["W"].mean()
    u_mean = velocity["U"].mean()
    v_mean = velocity["V"].mean()
    w_mean = velocity["W"].mean()
    velocity["u_"] = velocity["U"]-u_mean
    velocity["v_"] = velocity["V"]-v_mean
    velocity["w_"] = velocity["W"]-w_mean

    # creating  a octant column and giving the octant number of the particular values
    velocity.loc[((velocity.u_ > 0) & (velocity.v_ > 0) & (velocity.w_ > 0)), "Octant"] = "+1"
    velocity.loc[((velocity.u_ > 0) & (velocity.v_ > 0) & (velocity.w_ < 0)), "Octant"] = "-1"
    velocity.loc[((velocity.u_ < 0) & (velocity.v_ > 0) & (velocity.w_ > 0)), "Octant"] = "+2"
    velocity.loc[((velocity.u_ < 0) & (velocity.v_ > 0) & (velocity.w_ < 0)), "Octant"] = "-2"
    velocity.loc[((velocity.u_ < 0) & (velocity.v_ < 0) & (velocity.w_ > 0)), "Octant"] = "+3"
    velocity.loc[((velocity.u_ < 0) & (velocity.v_ < 0) & (velocity.w_ < 0)), "Octant"] = "-3"
    velocity.loc[((velocity.u_ > 0) & (velocity.v_ < 0) & (velocity.w_ > 0)), "Octant"] = "+4"
    velocity.loc[((velocity.u_ > 0) & (velocity.v_ < 0) & (velocity.w_ < 0)), "Octant"] = "-4"
    velocity.loc[1, " "] = "userinput"

    # finding the total count of octants of indiviual of octant
    h_ht = velocity['Octant'].value_counts()
    # f.loc[0,"Octant Id"]="overall count"

    velocity.loc[1, "Octant Id"] = "overall Count"
    velocity.loc[2, "Octant Id"] = "mod"+" " + str(mod)

    num_blocks = math.ceil(num/mod)
    l = 0
    m = mod
    start = 0
    end = m-1
    j = 0
    for j in range(num_blocks):
        if (start + mod > num):
            velocity.loc[j+3, "Octant Id"] = str(start)+"-" + str(num-1)
            break
        else:
            velocity.loc[j+3, "Octant Id"] = str(start)+"-" + str(end)

        j = j+1
        start = start + mod
        end = end + mod

    try:
        velocity.loc[1, "+1"] = h_ht["+1"]  # column for  +1 octant (creation)
    except:
        velocity.loc[1, "+1"] = 0
    try:
        velocity.loc[1, "-1"] = h_ht["-1"]  # for -1 octant
    except:
        velocity.loc[1, "-1"] = 0
    try:
        velocity.loc[1, "+2"] = h_ht["+2"]  #  for +2 octant
    except:
        velocity.loc[1, "+2"] = 0
    try:
        velocity.loc[1, "-2"] = h_ht["-2"]  # for -2 octant
    except:
        velocity.loc[1, "-2"] = 0
    try:
        velocity.loc[1, "+3"] = h_ht["+3"]  # for +3 octant
    except:
        velocity.loc[1, "+3"] = 0
    try:
        velocity.loc[1, "-3"] = h_ht["-3"]  # for -3 octant
    except:
        velocity.loc[1, "-3"] = 0
    try:
        velocity.loc[1, "+4"] = h_ht["+4"]  # for +4 octant
    except:
        velocity.loc[1, "+4"] = 0
    try:
        velocity.loc[1, "-4"] = h_ht["-4"] # for -4 octant
    except:
        velocity.loc[1, "-4"] = 0


    # creating rank columns 
    # and now for rank1 to rank8
    velocity.loc[0 , "+1 "] = "Rank1"  
    velocity.loc[0 , "-1 "] = "Rank2"
    velocity.loc[0 , "+2 "] = "Rank3"
    velocity.loc[0 , "-2 "] = "Rank4"
    velocity.loc[0 , "+3 "] = "Rank5"
    velocity.loc[0 , "-3 "] = "Rank6"
    velocity.loc[0 , "+4 "] = "Rank7"
    velocity.loc[0 , "-4 "] = "Rank8"
    velocity.loc[0, "   "] = "Rank1 Octant Id"
    velocity.loc[0, "    "] = "Rank1 Octant Name"
    
    rank1_count = {"+1 " : 0, "-1 " : 0, "+2 ": 0, "-2 ": 0, "+3 ": 0, "-3 ": 0, "+4 ": 0, "-4 ": 0 }
    
    rnum = 0
    # rn represents the row number which has to be checked
    row = 3
    # row represents the row where data needs to be inserted
    j = 0
    # current number block
    
    oct1 = oct2 = oct3 = oct4 = oct5 = oct6 = oct7 = oct8 = 0
    for j in range(num_blocks):
        
        for i in range(mod):
            try:
                if velocity["Octant"][rnum] == "+1":
                    oct1 = oct1+1
                elif velocity["Octant"][rnum] == "-1":
                    oct2 += 1
                elif velocity["Octant"][rnum] == "+2":
                    oct3 += 1
                elif velocity["Octant"][rnum] == "-2":
                    oct4 += 1
                elif velocity["Octant"][rnum] == "+3":
                    oct5 += 1
                elif velocity["Octant"][rnum] == "-3":
                    oct6 += 1
                elif velocity["Octant"][rnum] == "+4":
                    oct7 += 1
                elif velocity["Octant"][rnum] == "-4":
                    oct8 += 1
            except:
                print("Row Not found")

            rnum = rnum+1
            if rnum == num:
                j = num_blocks+1
                break  # break statement
        j = j+1
        try:
            velocity.loc[row, "+1"] = oct1
            velocity.loc[row, "+2"] = oct3
            velocity.loc[row, "-2"] = oct4
            velocity.loc[row, "+3"] = oct5
            velocity.loc[row, "-3"] = oct6
            velocity.loc[row, "+4"] = oct7
            velocity.loc[row, "-4"] = oct8
            velocity.loc[row, "-1"] = oct2
        except:
            print("Index out of Bound Error")
            
        
        
        #Before moving on to next block 
        lst = [ oct1, oct2 , oct3 , oct4 , oct5 , oct6, oct7 , oct8]
        st = set({})
        dict = {}
        
        for el in lst:
            st.add(el)
        for el in st:
            dict[el] = []
        #in st we hve octant values
        # and sorted in increasing order
        
        i = 0
        for el in lst:
            dict[el].append(graph[i])
            i+= 1
        for el in st:
            dict[el].sort(reverse = True)
        
        rank1 = "Initiate"
        # Now for each octant we assingn the ranks 
        rank = 8
        for el in st:
            for octant in dict[el]:
                try:
                   velocity.loc[row, octant] = rank
                except:
                   print("Index out of Bound Error") 
                if(rank == 1):
                    rank1 = octant
                rank -=  1
                
        # add data Rank1 Octant Id and its name 
        velocity.loc[row, "   "] = rank1
        velocity.loc[row, "    "] = octant_name_id_mapping[rank1]
        rank1_count[rank1] += 1
        oct1 = oct2 = oct3 = oct4 = oct5 = oct6 = oct7 = oct8 = 0
        
        row = row+1
    # adding data overall rank1 count for each octant 
    row += 4
    velocity.loc[row, "+1"] = "Octant Id"
    velocity.loc[row , "-1"] = "Octant Name"
    velocity.loc[row , "+2"] = "Count of Rank 1 Mod Values"
    
    row += 1
    cnt = 0
    for key in octant_name_id_mapping:
        velocity.loc[row, "+1"] = graph[cnt]
        velocity.loc[row, "-1"] = octant_name_id_mapping[graph[cnt]]
        velocity.loc[row, "+2"] = rank1_count[graph[cnt]]
        row += 1
        cnt += 1
  

#intialize function of tut 5
def Initialize(velocity, n, i):
    num = len(velocity)
    try:
       string_1 = velocity['Octant'][i] + "  "    
       for i in range(8):
            velocity.iat[n+i, velocity.columns.get_loc(string_1)] = 0
    except:
        print("Error: Out of bounds.")

def Update(velocity, l, i):
    num = len(velocity)
    try:
        string1 = velocity['Octant'][i]
        string2 = velocity['Octant'][i+1] + "  "

        if string1 == '+1':
            velocity.iat[l, velocity.columns.get_loc(string2)] += 1
        elif string1 == '-1':
            velocity.iat[l+1, velocity.columns.get_loc(string2)] += 1
        elif string1 == '+2':
            velocity.iat[l+2, velocity.columns.get_loc(string2)] += 1
        elif string1 == '-2':
            velocity.iat[l+3, velocity.columns.get_loc(string2)] += 1
        elif string1 == '+3':
            velocity.iat[l+4, velocity.columns.get_loc(string2)] += 1
        elif string1 == '-3':
            velocity.iat[l+5, velocity.columns.get_loc(string2)] += 1
        elif string1 == '+4':
            velocity.iat[l+6, velocity.columns.get_loc(string2)] += 1
        elif string1 == '-4':
            velocity.iat[l+7, velocity.columns.get_loc(string2)] += 1
    
    except:
        pass
  

#five space columns for given below an for integrating tut 2 
def Lol(velocity, m):
    num = len(velocity)
    velocity.loc[m+1, "     "] = "From"  
    velocity.loc[m-1, "+1  "] = "To"
    velocity.loc[m+1, 'overall id'] = "+"+str(1)
    velocity.loc[m+2, 'overall id'] = '-1'
    velocity.loc[m+3, 'overall id'] = "+"+str(2)
    velocity.loc[m+4, 'overall id'] = '-2'
    velocity.loc[m+5, 'overall id'] = "+"+str(3)
    velocity.loc[m+6, 'overall id'] = '-3'
    velocity.loc[m+7, 'overall id'] = '+4'
    velocity.loc[m, "overall id"] = "Count"
    velocity.loc[m, "+1  "] = "+"+str(1)
    velocity.loc[m, "-1  "] = '-1'
    velocity.loc[m, "+2  "] = "+"+str(2)
    velocity.loc[m, "-2  "] = '-2'
    velocity.loc[m, "+3  "] = "+"+str(3)
    velocity.loc[m, "-3  "] = '-3'
    velocity.loc[m, "+4  "] = "+"+str(4)
    velocity.loc[m, "-4  "] = '-4'
    velocity.loc[m+8, 'overall id'] = "+"+str(4)

# a fiunction we did in previous tuts for transition counts
def octant_transition_count(velocity, mod=5000):
    num = len(velocity)
    num_blocks = math.ceil(num/mod)
    l = 0
    m = mod
    start = 0
    end = m-1
    j = 0
    for j in range(num_blocks):
        if (start + mod > num):
            break
        else:
            pass

        j = j+1
        start = start + mod
        end = end + mod
    r = 0
    # r represents the row number which has to be checked
    row = 3
    # row represents the row where data needs to be inserted
    j = 0
    # j represents the current block number    
    m = n = y = j
    l = 0000
    z = mod-1  # assigning mod value to m
    a = 0
    b = mod-1
    velocity.loc[0, "     "] = ""
    for x in range(num_blocks):
        if x == 0:
            velocity.loc[y+2, "overall id"] = "Overall Transition Count"
        else:
            y += 12
            # changing the column overall id  according to mod value
            try:
                velocity.loc[y+1, "overall id"] = "Mod transition count "
                velocity.loc[y+2, "overall id"] = str(a)+"-"+str(b)
            except:
                 print("Row Not Found")
            j = j+1
            l = z+1
            z = z+mod
            a = str(l)

            b = str(z)
    y += 12
    try:
        velocity.loc[y+1, "overall id"] = "Mod transition count "
        velocity.loc[y+2, "overall id"] = str(a)+"-"+str(num)
    except:
        print("Row Not Found")

    m += 3

    Lol(velocity, m)

    n = n+4
    l = n
    
    for i in range(num):
        Initialize(velocity, n, i)

    for i in range(num):
        Update(velocity, l, i)

    n += 12
    z = n

    for x in range(0, num, mod):
        for i in range(x, mod+x-1, 1):
            if (i >= num):
                break
            Initialize(velocity, n, i)

        n += 12

    for x in range(0, num, mod):
        for i in range(x, mod+x-1, 1):
            if (i >= num):
                break
            l = z
            Update(velocity, l, i)
        z += 12

    m += 12

    for x in range(num_blocks):
        Lol(velocity, m)
        m += 12
 




def octant_analysis(mod=5000):
    print("Please wait while output files are created.")
    try:
      os.mkdir('output')
    except:
      print("Try deleting the Octant directory, and then run the program")
    path = os.getcwd()
    myfiles = glob.glob(os.path.join(path,"input1", "*.xlsx"))
    
    for df in myfiles:
         # df is the path name 
        velocity = pd.read_excel(df)
        fname = os.path.basename(df)
        file_name  = ""
        try:
            i = 0
            sz =len(fname)
            while i < sz-5:
                file_name += fname[i]
                i+= 1
        except:
            print("Program is strictly written for .xlsx extension files ")
        file_name += " cm_vel_octant_analysis_" + str(mod)
        
        trd1 = threading.Thread(target = octant_range_names, args=(velocity, mod,))
        trd1.start()
        trd1.join()
        trd2 = threading.Thread(target = octant_transition_count , args=(velocity, mod,))
        trd2.start()
        trd2.join()
        trd3 = threading.Thread(target = octant_longest_subsequence_count, args =(velocity,))
        trd3.start()
        trd3.join()
        
        
        
        # while outputting -> input file  name +" cm_vel_octant_analysis_" + str(mod)
        velocity.to_excel(f'output/{file_name}.xlsx', index = False)
        # f.to_excel('./combined_output.xlsx')
        
        
    
	
#for xlxs files only
#Read all the excel files in a batch format from the input/ folder
#Save all the excel files in a the output/ folder

from platform import python_version
ver = python_version()

if ver == "3.8.10":
	print("Correct Version Installed")
else:
	print("Error: Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")



#mod value can be changed from here 

mod=5000
octant_analysis(mod)

#


#This shall be the last lines of the code.
print("Output files are ready :] ")
end_T = datetime.now()
print('Duration of Program Execution: {}'.format(end_T - start_time))
