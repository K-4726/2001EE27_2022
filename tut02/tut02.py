import pandas as pd
import math
# reading a csv file using pandas
velocity = pd.read_csv("octant_input.csv")


velocity.loc[0, "U_Avg"] = f["U"].mean()
velocity.loc[0, "V_Avg"] = f["V"].mean()
velocity.loc[0, "W_Avg"] = f["W"].mean()
var1 = velocity["U"].mean()
var2 = velocity["V"].mean()
var3 = velocity["W"].mean()
velocity["u_"] = velocity["U"]-var1
velocity["v_"] = velocity["V"]-var2
velocity["w_"] = velocity["W"]-var3


# creating  a octant column and giving the octant number of the particular values
velocity.loc[((velocity.u_ > 0) & (velocity.v_ > 0) & (velocity.w_ > 0)), "Octant"] = "+1"
velocity.loc[((velocity.u_ > 0) & (velocity.v_ > 0) & (velocity.w_ < 0)), "Octant"] = "-1"
velocity.loc[((velocity.u_ < 0) & (velocity.v_ > 0) & (velocity.w_ > 0)), "Octant"] = "+2"
velocity.loc[((velocity.u_ < 0) & (velocity.v_ > 0) & (velocity.w_ < 0)), "Octant"] = "-2"
velocity.loc[((velocity.u_ < 0) & (velocity.v_ < 0) & (velocity.w_ > 0)), "Octant"] = "+3"
velocity.loc[((velocity.u_ < 0) & (velocity.v_ < 0) & (velocity.w_ < 0)), "Octant"] = "-3"
velocity.loc[((velocity.u_ > 0) & (velocity.v_ < 0) & (velocity.w_ > 0)), "Octant"] = "+4"
velocity.loc[((velocity.u_ > 0) & (velocity.v_ < 0) & (velocity.w_ < 0)), "Octant"] = "-4"
velocity.loc[1, ""] = "userinput"


# finding the total count of octants of indiviual of octant
h = velocity['Octant'].value_counts()
velocity.loc[0, "overall id"] = "overall count"




#mod value can be changed from here

mod = int(input("Enter mod value : "))

y = str(mod)  # conveting int to str

#



velocity.loc[1, "overall id"] = "mod"+" "+y
dat = math.ceil(29745/mod)
l = 0000
m = mod  # assigning mod value to m
a = str(l)  # changing the integer to string function
b = str(m)  # changing the integer to string function
j = 0
for j in range(dat):
    # changing the column overall id  according to mod value
    velocity.loc[j+2, "overall id"] = a+"-"+b
    j = j+1
    l = m+1
    m = m+mod
    a = str(l)
    b = str(m)


#Now we create new columns for each octant (+1,-1,+2,-2,+3,-3 and +4,-4)
velocity.loc[0, "+1"] = h["+1"]  
velocity.loc[0, "-1"] = h["-1"]  
velocity.loc[0, "+2"] = h["+2"]  
velocity.loc[0, "-2"] = h["-2"]  
velocity.loc[0, "+3"] = h["+3"]  
velocity.loc[0, "-3"] = h["-3"]  
velocity.loc[0, "+4"] = h["+4"]  
velocity.loc[0, "-4"] = h["-4"]  
