import pandas as pd
import math
from platform import python_version

velocity = pd.read_excel("input_octant_longest_subsequence_with_range.xlsx")

num = len(velocity) - 1

def octant_longest_subsequence_count():
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


    LongSub = {"-1" : 0, "+1" : 0 ,  "-2" : 0 , "+2" : 0 , "-3" : 0 , "+3" : 0 , "-4" : 0, "+4" : 0}

    # The column of the files have to be initialized now... we will do so

    velocity[" "]= " "
    velocity["count"] = ""
    velocity["Longest Subsquence Length"] = ""
    velocity["Count"] = ""
        
    velocity["  "] = " "
    velocity["count2"] = ""
    velocity["Longest Subsquence Length2"] = ""
    velocity["Count2"] = ""

    # In the following while loop I have basically filled the columns

    var = 0 # Counting longest Subsequence Length 
    while var <= num:
        octant1 = velocity["Octant"][var]
        curr_cnt = 0
        j = var
        while j <= num:
            #adding some try except here
            try:
                octant2= velocity["Octant"][j]
                if(octant2 == octant1):
                    curr_cnt +=1 
                else:
                    break
                j += 1
            except:
                print("Error: this row is not found")
        LongSub[velocity["Octant"][var]] = max(LongSub[velocity["Octant"][var]], curr_cnt)
        var = j

    # Creating a dictionary, basically a map type logic
    mapng = { 0 : "+1" , 1 : "-1",  2 : "+2" , 3 : "-2", 4 : "+3" , 5 : "-3" , 6 : "+4", 7 : "-4"}

    for i in range(8):
        try:  
            velocity.loc[i , "count"] = mapng[i]
        except:
            print("Error: this row was not found")
            
    for i in range(8):
        try:
            velocity.loc[i, "Longest Subsquence Length"] =LongSub[mapng[i]]
        except:
            print("Error: this row was not found")
            
            
    var2 = 0
        
    # This dictionary will be counting number of longest subsequences for each octant
    count_Long_Sub = {"-1" : 0, "+1" : 0 ,  "-2" : 0 , "+2" : 0 , "-3" : 0 , "+3" : 0 , "-4" : 0, "+4" : 0}

    #  for each octant's longest subsequence Creating list of strings(Time Ranges)
    range_of_Long_Sub = {"-1" : [], "+1" : [] ,  "-2" : [] , "+2" : [] , "-3" : [] , "+3" : [], "-4" : [], "+4" : []}

    # in the following while loop I will append the timerange to range of long subcount 
    while var2 <= num:
            curr_cnt = 0
            octant1 = ""
            #trying to add a try and except here
            try:
                octant1 = velocity["Octant"][var2]
                j = var2
                while j <= num:
                
                    octant2= velocity["Octant"][j]
                    if(octant2 == octant1):
                        curr_cnt +=1 
                    else:
                        break
                    j += 1
            except:
                    print("Error Row not found")
            
            if(curr_cnt == LongSub[octant1]):
                count_Long_Sub[octant1] += 1 
                # form var2 till j-1
                try:
                    timeRange = str(velocity["Time"][var2]) + "," + str(velocity["Time"][j-1])
                    range_of_Long_Sub[octant1].append(timeRange)
                except:
                    print("Error: Invalid mod value or invalid data or Excel file is empty") 
                
            var2 = j

    ind2 = 0 


    for index1 in range(8):
        velocity.loc[index1, "Count"] = count_Long_Sub[mapng[index1]]
        currOctant = mapng[index1]
        
        velocity.loc[ind2, "count2"] = currOctant
        velocity.loc[ind2, "Longest Subsquence Length2"] = LongSub[currOctant]
        velocity.loc[ind2, "Count2"] = count_Long_Sub[currOctant]
        
        ind2 += 1
        velocity.loc[ind2, "count2"] = "Time"
        velocity.loc[ind2, "Longest Subsquence Length2"] = "From"
        velocity.loc[ind2, "Count2"] = "To"
        
        ind2 += 1
        for timeRange in range_of_Long_Sub[currOctant]:
            lst = timeRange.split(",")
            velocity.loc[ind2, "Longest Subsquence Length2"]  = lst[0]
            velocity.loc[ind2, "Count2"] = lst[1]
            ind2 += 1

    # seeing out
    velocity.to_excel('./output_octant_longest_subsequence_with_range.xlsx')
    print("The Output file is ready.")
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

octant_longest_subsequence_count()
