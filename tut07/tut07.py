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
def octant_range_names(f, mod=5000):
    num = len(f)
    
    octant_name_id_mapping = {"+1 ": "Internal outward interaction", "-1 ": "External outward interaction", "+2 ": "External Ejection",
                              "-2 ": "Internal Ejection", "+3 ": "External inward interaction", "-3 ": "Internal inward interaction", "+4 ": "Internal sweep", "-4 ": "External sweep"}
    f.loc[0, "U_Avg"] = f["U"].mean()
    f.loc[0, "V_Avg"] = f["V"].mean()
    f.loc[0, "W_Avg"] = f["W"].mean()
    u_mean = f["U"].mean()
    v_mean = f["V"].mean()
    w_mean = f["W"].mean()
    f["u_"] = f["U"]-u_mean
    f["v_"] = f["V"]-v_mean
    f["w_"] = f["W"]-w_mean

    # creating  a octant column and giving the octant number of the particular values
    f.loc[((f.u_ > 0) & (f.v_ > 0) & (f.w_ > 0)), "Octant"] = "+1"
    f.loc[((f.u_ > 0) & (f.v_ > 0) & (f.w_ < 0)), "Octant"] = "-1"
    f.loc[((f.u_ < 0) & (f.v_ > 0) & (f.w_ > 0)), "Octant"] = "+2"
    f.loc[((f.u_ < 0) & (f.v_ > 0) & (f.w_ < 0)), "Octant"] = "-2"
    f.loc[((f.u_ < 0) & (f.v_ < 0) & (f.w_ > 0)), "Octant"] = "+3"
    f.loc[((f.u_ < 0) & (f.v_ < 0) & (f.w_ < 0)), "Octant"] = "-3"
    f.loc[((f.u_ > 0) & (f.v_ < 0) & (f.w_ > 0)), "Octant"] = "+4"
    f.loc[((f.u_ > 0) & (f.v_ < 0) & (f.w_ < 0)), "Octant"] = "-4"
    f.loc[1, " "] = "userinput"

    # finding the total count of octants of indiviual of octant
    h_ht = f['Octant'].value_counts()
    # f.loc[0,"Octant Id"]="overall count"

    f.loc[1, "Octant Id"] = "overall Count"
    f.loc[2, "Octant Id"] = "mod"+" " + str(mod)

    num_blocks = math.ceil(num/mod)
    l = 0
    m = mod
    start = 0
    end = m-1
    j = 0
    for j in range(num_blocks):
        if (start + mod > num):
            f.loc[j+3, "Octant Id"] = str(start)+"-" + str(num-1)
            break
        else:
            f.loc[j+3, "Octant Id"] = str(start)+"-" + str(end)

        j = j+1
        start = start + mod
        end = end + mod

    try:
        f.loc[1, "+1"] = h_ht["+1"]  # column for  +1 octant (creation)
    except:
        f.loc[1, "+1"] = 0
    try:
        f.loc[1, "-1"] = h_ht["-1"]  # for -1 octant
    except:
        f.loc[1, "-1"] = 0
    try:
        f.loc[1, "+2"] = h_ht["+2"]  #  for +2 octant
    except:
        f.loc[1, "+2"] = 0
    try:
        f.loc[1, "-2"] = h_ht["-2"]  # for -2 octant
    except:
        f.loc[1, "-2"] = 0
    try:
        f.loc[1, "+3"] = h_ht["+3"]  # for +3 octant
    except:
        f.loc[1, "+3"] = 0
    try:
        f.loc[1, "-3"] = h_ht["-3"]  # for -3 octant
    except:
        f.loc[1, "-3"] = 0
    try:
        f.loc[1, "+4"] = h_ht["+4"]  # for +4 octant
    except:
        f.loc[1, "+4"] = 0
    try:
        f.loc[1, "-4"] = h_ht["-4"] # for -4 octant
    except:
        f.loc[1, "-4"] = 0


    # creating rank columns 
    # and now for rank1 to rank8
    f.loc[0 , "+1 "] = "Rank1"  
    f.loc[0 , "-1 "] = "Rank2"
    f.loc[0 , "+2 "] = "Rank3"
    f.loc[0 , "-2 "] = "Rank4"
    f.loc[0 , "+3 "] = "Rank5"
    f.loc[0 , "-3 "] = "Rank6"
    f.loc[0 , "+4 "] = "Rank7"
    f.loc[0 , "-4 "] = "Rank8"
    f.loc[0, "   "] = "Rank1 Octant Id"
    f.loc[0, "    "] = "Rank1 Octant Name"
    
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
                if f["Octant"][rnum] == "+1":
                    oct1 = oct1+1
                elif f["Octant"][rnum] == "-1":
                    oct2 += 1
                elif f["Octant"][rnum] == "+2":
                    oct3 += 1
                elif f["Octant"][rnum] == "-2":
                    oct4 += 1
                elif f["Octant"][rnum] == "+3":
                    oct5 += 1
                elif f["Octant"][rnum] == "-3":
                    oct6 += 1
                elif f["Octant"][rnum] == "+4":
                    oct7 += 1
                elif f["Octant"][rnum] == "-4":
                    oct8 += 1
            except:
                print("Row Not found")

            rnum = rnum+1
            if rnum == num:
                j = num_blocks+1
                break  # break statement
        j = j+1
        try:
            f.loc[row, "+1"] = oct1
            f.loc[row, "+2"] = oct3
            f.loc[row, "-2"] = oct4
            f.loc[row, "+3"] = oct5
            f.loc[row, "-3"] = oct6
            f.loc[row, "+4"] = oct7
            f.loc[row, "-4"] = oct8
            f.loc[row, "-1"] = oct2
        except:
            print("Index out of Bound Error")
            
        
        
        # Tut 5 main work 
        #Before moving on to next block 
        ls = [ oct1, oct2 , oct3 , oct4 , oct5 , oct6, oct7 , oct8]
        st = set({})
        dict = {}
        
        for el in ls:
            st.add(el)
        for el in st:
            dict[el] = []
        # found distinct octant values in st and sorted in increasing order 
        
        i = 0
        for el in ls:
            dict[el].append(graph[i])
            i+= 1
        for el in st:
            dict[el].sort(reverse = True)
        
        rank1 = "Initiate"
        # assigning rank to octants 
        rank = 8
        for el in st:
            for octant in dict[el]:
                try:
                   f.loc[row, octant] = rank
                except:
                   print("Index out of Bound Error") 
                if(rank == 1):
                    rank1 = octant
                rank -=  1
                
        # Inserting Rank1 Octant Id and its name 
        f.loc[row, "   "] = rank1
        f.loc[row, "    "] = octant_name_id_mapping[rank1]
        rank1_count[rank1] += 1
        oct1 = oct2 = oct3 = oct4 = oct5 = oct6 = oct7 = oct8 = 0
        
        row = row+1
    # inserting overall rank1 count for each octant 
    row += 4
    f.loc[row, "+1"] = "Octant Id"
    f.loc[row , "-1"] = "Octant Name"
    f.loc[row , "+2"] = "Count of Rank 1 Mod Values"
    
    row += 1
    cnt = 0
    # graph2 = {0:"+1" , 1:"-1"  , 2:"+2"  , 3:"-2"  , 4:"+3"  , 5:"-3"  , 6:"+4"  , 7:"-4"}
    for key in octant_name_id_mapping:
        f.loc[row, "+1"] = graph[cnt]
        f.loc[row, "-1"] = octant_name_id_mapping[graph[cnt]]
        f.loc[row, "+2"] = rank1_count[graph[cnt]]
        row += 1
        cnt += 1
  
  
# Integrating tut 5 
def Initialize(f, n, i):
    num = len(f)
    try:
       string1 = f['Octant'][i] + "  "    
       for i in range(8):
            f.iat[n+i, f.columns.get_loc(string1)] = 0
    except:
        print("Index out of Bound Error1")

def Update(f, l, i):
    num = len(f)
    try:
        string1 = f['Octant'][i]
        string2 = f['Octant'][i+1] + "  "

        if string1 == '+1':
            f.iat[l, f.columns.get_loc(string2)] += 1
        elif string1 == '-1':
            f.iat[l+1, f.columns.get_loc(string2)] += 1
        elif string1 == '+2':
            f.iat[l+2, f.columns.get_loc(string2)] += 1
        elif string1 == '-2':
            f.iat[l+3, f.columns.get_loc(string2)] += 1
        elif string1 == '+3':
            f.iat[l+4, f.columns.get_loc(string2)] += 1
        elif string1 == '-3':
            f.iat[l+5, f.columns.get_loc(string2)] += 1
        elif string1 == '+4':
            f.iat[l+6, f.columns.get_loc(string2)] += 1
        elif string1 == '-4':
            f.iat[l+7, f.columns.get_loc(string2)] += 1
    
    except:
        pass
        
  
