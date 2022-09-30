from platform import python_version
import pandas as pd
import math

velocity = pd.read_excel('input_octant_longest_subsequence.xlsx')

velocity.loc[0, "U_Avg"] = velocity["U"].mean()
velocity.loc[0, "V_Avg"] = velocity["V"].mean()
velocity.loc[0, "W_Avg"] = velocity["W"].mean()
velocity["u_"] = velocity["U"]-velocity["U"].mean()
velocity["v_"] = velocity["V"]-velocity["V"].mean()
velocity["w_"] = velocity["W"]-velocity["W"].mean()


velocity.loc[((velocity.u_ > 0) & (velocity.v_ > 0) & (velocity.w_ > 0)), "Octant"] = "+1"
velocity.loc[((velocity.u_ > 0) & (velocity.v_ > 0) & (velocity.w_ < 0)), "Octant"] = "-1"
velocity.loc[((velocity.u_ < 0) & (velocity.v_ > 0) & (velocity.w_ > 0)), "Octant"] = "+2"
velocity.loc[((velocity.u_ < 0) & (velocity.v_ > 0) & (velocity.w_ < 0)), "Octant"] = "-2"
velocity.loc[((velocity.u_ < 0) & (velocity.v_ < 0) & (velocity.w_ > 0)), "Octant"] = "+3"
velocity.loc[((velocity.u_ < 0) & (velocity.v_ < 0) & (velocity.w_ < 0)), "Octant"] = "-3"
velocity.loc[((velocity.u_ > 0) & (velocity.v_ < 0) & (velocity.w_ > 0)), "Octant"] = "+4"
velocity.loc[((velocity.u_ > 0) & (velocity.v_ < 0) & (velocity.w_ < 0)), "Octant"] = "-4"

num = len(velocity)

total_count=[0,0,0,0,0,0,0,0]
for i in range(num):
    str = velocity["Octant"][i]
    if str == "+1":
        total_count[0] += 1
    elif str == "-1":
        total_count[1] += 1
    elif str == "+2":
        total_count[2] += 1
    elif str == "-2":
        total_count[3] += 1
    elif str == "+3":
        total_count[4] += 1
    elif str == "-3":
        total_count[5] += 1
    elif str == "+4":
        total_count[6] += 1
    elif str == "-4":
        total_count[7] += 1
        