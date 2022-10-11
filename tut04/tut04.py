import pandas as pd
import math
from platform import python_version

velocity = pd.read_excel("input_octant_longest_subsequence_with_range.xlsx")

num = len(velocity) - 1

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
            print("row not found")
    LongSub[velocity["Octant"][var]] = max(LongSub[velocity["Octant"][var]], curr_cnt)
    var = j