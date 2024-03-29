from platform import python_version
from datetime import datetime
start_time=datetime.now()
import pandas as pd
import math

def octant_longest_subsequence_count():
    try:
     velocity = pd.read_excel('input_octant_longest_subsequence.xlsx')
    except:
     print("Some error occurred")

    #finding mean and subtracting from each values
    velocity.loc[0, "U_Avg"] = velocity["U"].mean()
    velocity.loc[0, "V_Avg"] = velocity["V"].mean()
    velocity.loc[0, "W_Avg"] = velocity["W"].mean()

    velocity["u_"] = velocity["U"]-velocity["U"].mean()
    velocity["v_"] = velocity["V"]-velocity["V"].mean()
    velocity["w_"] = velocity["W"]-velocity["W"].mean()

    #assignment of octants 
    velocity.loc[((velocity.u_ > 0) & (velocity.v_ > 0) & (velocity.w_ > 0)), "Octant"] = "+1"
    velocity.loc[((velocity.u_ > 0) & (velocity.v_ > 0) & (velocity.w_ < 0)), "Octant"] = "-1"
    velocity.loc[((velocity.u_ < 0) & (velocity.v_ > 0) & (velocity.w_ > 0)), "Octant"] = "+2"
    velocity.loc[((velocity.u_ < 0) & (velocity.v_ > 0) & (velocity.w_ < 0)), "Octant"] = "-2"
    velocity.loc[((velocity.u_ < 0) & (velocity.v_ < 0) & (velocity.w_ > 0)), "Octant"] = "+3"
    velocity.loc[((velocity.u_ < 0) & (velocity.v_ < 0) & (velocity.w_ < 0)), "Octant"] = "-3"
    velocity.loc[((velocity.u_ > 0) & (velocity.v_ < 0) & (velocity.w_ > 0)), "Octant"] = "+4"
    velocity.loc[((velocity.u_ > 0) & (velocity.v_ < 0) & (velocity.w_ < 0)), "Octant"] = "-4"

    #taking out count for each of the octants
    n= len(velocity)

    total_count=[0,0,0,0,0,0,0,0]
    for i in range(n):
        str = velocity["Octant"][i]
        if str == "+1":      # octant +1
            total_count[0] += 1
        elif str == "-1":    # octant -1
            total_count[1] += 1 
        elif str == "+2":    # octant +2
            total_count[2] += 1
        elif str == "-2":    # octant -2
            total_count[3] += 1
        elif str == "+3":    # octant +3
            total_count[4] += 1
        elif str == "-3":    # octant -3
            total_count[5] += 1
        elif str == "+4":    # octant +4
            total_count[6] += 1
        elif str == "-4":    # octant -4
            total_count[7] += 1

    # creating a temporary count and a final count which we will obtain through looping        
    tmp_Cnt_Seq=[1,1,1,1,1,1,1,1]

    longest_subsequence_length=[0,0,0,0,0,0,0,0]


    for i in range(1, n):
        str = velocity["Octant"][i-1]
        # if the previous octant is same as current 
        if velocity["Octant"][i] == velocity["Octant"][i-1]:
            if str == "+1":
                tmp_Cnt_Seq[0] += 1
            elif str == "-1":
                tmp_Cnt_Seq[1] += 1
            elif str == "+2":
                tmp_Cnt_Seq[2] += 1
            elif str == "-2":
                tmp_Cnt_Seq[3] += 1
            elif str == "+3":
                tmp_Cnt_Seq[4] += 1
            elif str == "-3":
                tmp_Cnt_Seq[5] += 1
            elif str == "+4":
                tmp_Cnt_Seq[6] += 1
            elif str == "-4":
                tmp_Cnt_Seq[7] += 1
        else:
            for j in range(8):
                #updating the l_s_l
                longest_subsequence_length[j] = max(longest_subsequence_length[j], tmp_Cnt_Seq[j])
            # resetting the temporary count
            tmp_Cnt_Seq = [1, 1, 1, 1, 1, 1, 1, 1]

    # uptill now we have the final counts of longest subsequence for each octant 

    #now we have to calculate the count l_s_l for each octant
    count_longest_subsequence_length = [0, 0, 0, 0, 0, 0, 0, 0]

    temp = [1, 1, 1, 1, 1, 1, 1, 1] # declaring initial counts to 1

    for i in range(1, n):
        str = velocity["Octant"][i-1]
        # loop to get the l_s_l of each octant
        if velocity["Octant"][i] == velocity["Octant"][i-1]:
            if str == "+1":
                temp[0] += 1
            elif str == "-1":
                temp[1] += 1
            elif str == "+2":
                temp[2] += 1
            elif str == "-2":
                temp[3] += 1
            elif str == "+3":
                temp[4] += 1
            elif str == "-3":
                temp[5] += 1
            elif str == "+4":
                temp[6] += 1
            elif str == "-4":
                temp[7] += 1
        else:
            for j in range(8):
                # when we find one more l_s_l for our octant we add 1 to it
                if temp[j] == longest_subsequence_length[j] and temp[j] != 1:
                    count_longest_subsequence_length[j] += 1
                # else set the count to total count for that particular octant
                elif temp[j] == longest_subsequence_length[j] and temp[j] == 1 :
                    count_longest_subsequence_length[j] = total_count[j]
                    
            # once the above loop is done... 
            #reset the temp counts to 1
            temp = [1, 1, 1, 1, 1, 1, 1, 1]
            # continue towards the outer loop

    # now finally we create columns according to our output file (sample)
    velocity[" "]=""
    velocity["Count"]=""
    velocity["Longest Subsequence Length"]="" # longest subsequence length of each octant
    velocity["Count2"]="" # count of l_s_l for each octant

    velocity.loc[0, "Count"] = "+1"
    velocity.loc[1, "Count"] = "-1"
    velocity.loc[2, "Count"] = "+2"
    velocity.loc[3, "Count"] = "-2"
    velocity.loc[4, "Count"] = "+3"
    velocity.loc[5, "Count"] = "-3"
    velocity.loc[6, "Count"] = "+4"
    velocity.loc[7, "Count"] = "-4"

    for i in range(8):
        velocity.loc[i,"Longest Subsequence Length"]=longest_subsequence_length[i]
        velocity.loc[i,"Count2"]=count_longest_subsequence_length[i]

    try:
     velocity.to_excel("output_octant_longest_subsequence.xlsx")
    except:
     print("Some error occured")

octant_longest_subsequence_count()
print("Execution Successfull and Output file created")
end_time=datetime.now()
print('Executed in time (hr/min/sec) == {}'.format(end_time-start_time))