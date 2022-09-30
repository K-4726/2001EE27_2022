import pandas as pd
 
import math
# reading a csv file using pandas
def octant_transition_count(mod):
    try:
      velocity = pd.read_excel('./input_octant_transition_identify.xlsx')
    except:
      print("Error file not found")

    velocity.loc[0, "U_Avg"] = velocity["U"].mean()
    velocity.loc[0, "V_Avg"] = velocity["V"].mean()
    velocity.loc[0, "W_Avg"] = velocity["W"].mean()
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




   

    
    y = str(mod)  # conveting int to str

    



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


    # the following logic has to be repeated 2^3 ie 8 times

    #first time for +1
    t1 = 0  
    t2 = 0
    t3 = 2
    j = 0
    try:
        for j in range(dat):  # running the loop d times according to mod value
            for i in range(mod):  # running the loop according to mod value
                if velocity["Octant"][t2] == "+1":  # if octant is +1
                    t1= t1+1  # incrementing the q value by 1
                t2 = t2+1
                if t2 == 29745:
                    j = dat+1  # if r reached the last value then break the statment
                    break  # break statement
            j = j+1
            velocity.loc[t3, "+1"] = t1
            t3 = t3+1
            t1 = 0
    except:
        print("some error occured")
    # second time -1
    # similar try and except can be added for each of the loops
    q = 0  
    r = 0
    p = 2
    j = 0
    for j in range(dat):
        for i in range(mod):
            if velocity["Octant"][r] == "-1":  # if octant is -1
                q = q+1  # incrementing the q value by 1
            r = r+1
            if r == 29745:
                j = dat+1
                break  # break statement
        j = j+1
        velocity.loc[p, "-1"] = q
        p = p+1
        q = 0

    #third time +2 p=v3,q=v1,r=v2
    v1 = 0  
    v2 = 0
    v3 = 2
    j = 0
    for j in range(dat):
        for i in range(mod):
            if velocity["Octant"][v2] == "+2":  # if octant is +2
                v1 = v1+1  # incrementing the q value by 1
            v2 = v2+1
            if v2 == 29745:
                j = dat+1
                break  # break statement
        velocity.loc[v3, "+2"] = v1
        v3 = v3+1
        v1= 0

    #4th time -2
    a = 0  # creating  a variable for individual count
    b = 0
    c = 2
    j = 0
    for j in range(dat):
        for i in range(mod):
            if velocity["Octant"][b] == "-2":  # if octant is -2
                a = a+1  # incrementing the q value by 1
            b = b+1
            if b == 29745:
                j = dat+1
                break  # break statement
        j = j+1
        velocity.loc[c, "-2"] = a
        c = c+1
        a = 0

    #5th time +3
    q = 0  # creating  a variable for individual count
    r = 0
    p = 2
    j = 0
    for j in range(dat):
        for i in range(mod):
            if velocity["Octant"][r] == "+3":  # if octant is +3
                q = q+1  # incrementing the q value by 1
            r = r+1
            if r == 29745:
                j = dat+1
                break  # break statement
        j = j+1
        velocity.loc[p, "+3"] = q
        p = p+1
        q = 0

    #6th time -3
    v1 = 0  # creating  a variable for individual count
    v2 = 0
    v3 = 2
    j = 0
    for j in range(dat):
        for i in range(mod):
            if velocity["Octant"][v2] == "-3":  # if octant is -3
                v1 = v1+1  # incrementing the q value by 1
            v2 = v2+1
            if v2 == 29745:
                j = dat+1
                break  # break statement
        j = j+1
        velocity.loc[v3, "-3"] = v1
        v3 = v3+1
        v1 = 0


    q = 0  # creating  a variable for individual count
    r = 0
    p = 2
    j = 0
    for j in range(dat):
        for i in range(mod):
            if velocity["Octant"][r] == "+4":  # if octant is +4
                q = q+1  # incrementing the q value by 1
            r = r+1
            if r == 29745:
                j = dat+1
                break  # break statement
        j = j+1
        velocity.loc[p, "+4"] = q
        p = p+1
        q = 0


    t1 = 0  # creating  a variable for individual count
    t2 = 0
    t3 = 2
    j = 0
    for j in range(dat):
        for i in range(mod):
            if velocity["Octant"][t2] == "-4":  # if octant is -4
                t1 = t1+1  # incrementing the q value by 1
            t2 = t2+1
            if t2 == 29745:
                j = dat+1
                break  # break statement
        j = j+1
        velocity.loc[t3, "-4"] = t1
        t3 = t3+1
        t1 = 0


    m = n = j
    velocity.loc[m+4, ""] = "From"
    velocity.loc[m+1, "overall id"] = "Overall Transition Count"
    velocity.loc[m+2, "+1"] = "To"
    velocity.loc[m+3, "overall id"] = "Count"


    n = n+4
    num = len(velocity)-1


    l = n
    for i in range(num):
        str1 = velocity['Octant'][i]
        str2 = velocity['Octant'][i+1]
        if str2 == '+1':
            velocity.iat[n, velocity.columns.get_loc(str1)] = 0
        elif str2 == '-1':
            velocity.iat[n+1, velocity.columns.get_loc(str1)] = 0
        elif str2 == '+2':
            velocity.iat[n+2, velocity.columns.get_loc(str1)] = 0
        elif str2 == '-2':
            velocity.iat[n+3, velocity.columns.get_loc(str1)] = 0
        elif str2 == '+3':
            velocity.iat[n+4, velocity.columns.get_loc(str1)] = 0
        elif str2 == '-3':
            velocity.iat[n+5, velocity.columns.get_loc(str1)] = 0
        elif str2 == '+4':
            velocity.iat[n+6, velocity.columns.get_loc(str1)] = 0
        elif str2 == '-4':
            velocity.iat[n+7, velocity.columns.get_loc(str1)] = 0
    # f.to_csv('./octant_output.csvout.csv')


    for i in range(num):
        str1 = velocity['Octant'][i]
        str2 = velocity['Octant'][i+1]
        if str2 == '+1':
            velocity.iat[l, velocity.columns.get_loc(str1)] += 1
        elif str2 == '-1':
            velocity.iat[l+1, velocity.columns.get_loc(str1)] += 1
        elif str2 == '+2':
            velocity.iat[l+2, velocity.columns.get_loc(str1)] += 1
        elif str2 == '-2':
            velocity.iat[l+3, velocity.columns.get_loc(str1)] += 1
        elif str2 == '+3':
            velocity.iat[l+4, velocity.columns.get_loc(str1)] += 1
        elif str2 == '-3':
            velocity.iat[l+5, velocity.columns.get_loc(str1)] += 1
        elif str2 == '+4':
            velocity.iat[l+6, velocity.columns.get_loc(str1)] += 1
        elif str2 == '-4':
            velocity.iat[l+7, velocity.columns.get_loc(str1)] += 1

    velocity.to_csv('./octant_output.csvout.csv')


    n = n+10
    for x in range(0, num, mod):
        for i in range(x, mod+x, 1):
            if (i >= num):
                break

            str1 = velocity['Octant'][i]
            str2 = velocity['Octant'][i+1]
            if str2 == '+1':
                velocity.iat[n, velocity.columns.get_loc(str1)] = 0
            elif str2 == '-1':
                velocity.iat[n+1, velocity.columns.get_loc(str1)] = 0
            elif str2 == '+2':
                velocity.iat[n+2, velocity.columns.get_loc(str1)] = 0
            elif str2 == '-2':
                velocity.iat[n+3, velocity.columns.get_loc(str1)] = 0
            elif str2 == '+3':
                velocity.iat[n+4, velocity.columns.get_loc(str1)] = 0
            elif str2 == '-3':
                velocity.iat[n+5, velocity.columns.get_loc(str1)] = 0
            elif str2 == '+4':
                velocity.iat[n+6, velocity.columns.get_loc(str1)] = 0
            elif str2 == '-4':
                velocity.iat[n+7, velocity.columns.get_loc(str1)] = 0

        for i in range(x, mod+x, 1):
            if (i >= num):
                break
            l = n
            str1 = velocity['Octant'][i]
            str2 = velocity['Octant'][i+1]
            if str2 == '+1':
                velocity.iat[l, velocity.columns.get_loc(str1)] += 1
            elif str2 == '-1':
                velocity.iat[l+1, velocity.columns.get_loc(str1)] += 1
            elif str2 == '+2':
                velocity.iat[l+2, velocity.columns.get_loc(str1)] += 1
            elif str2 == '-2':
                velocity.iat[l+3, velocity.columns.get_loc(str1)] += 1
            elif str2 == '+3':
                velocity.iat[l+4, velocity.columns.get_loc(str1)] += 1
            elif str2 == '-3':
                velocity.iat[l+5, velocity.columns.get_loc(str1)] += 1
            elif str2 == '+4':
                velocity.iat[l+6, velocity.columns.get_loc(str1)] += 1
            elif str2 == '-4':
                velocity.iat[l+7, velocity.columns.get_loc(str1)] += 1

        n += 10
    try:
     velocity.to_excel('./output_octant_transition_identify.xlsx')
    except:
      print("Error file cannot be created")

try:
 mod=int(input("Enter the value of Mod: "))
 octant_transition_count(mod)
except:
 print("Error while calling function")
print("Execution successfull")
print("Output file is ready")