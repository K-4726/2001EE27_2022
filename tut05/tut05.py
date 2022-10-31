from datetime import datetime
from decimal import DivisionByZero
start_time = datetime.now()


try:
    from platform import python_version
    import pandas as pd
    ver = python_version()

    if ver == "3.8.10":
        print("Correct Version Installed")
    else:
        print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

    #Opening the input excel file
    velocity = pd.read_excel('octant_input.xlsx')

    # Calculation of the mean value of U, V, W
    velocity.at[0, 'U Avg'] = velocity['U'].mean()
    velocity.at[0, 'V Avg'] = velocity['V'].mean()
    velocity.at[0, 'W Avg'] = velocity['W'].mean()

    #The difference between the value and the mean 
    velocity["U'=U - U avg"] = velocity['U'] - velocity['U Avg'][0]
    velocity["V'=V - V avg"] = velocity['V'] - velocity['V Avg'][0]
    velocity["W'=W - W avg"] = velocity['W'] - velocity['W Avg'][0]

    #Identification of octant values
    for i in range(len(velocity)):
        if(velocity["U'=U - U avg"][i] > 0 and velocity["V'=V - V avg"][i] > 0):
            velocity.at[i, 'Octant'] = int(1)
        if(velocity["U'=U - U avg"][i] < 0 and velocity["V'=V - V avg"][i] > 0):
            velocity.at[i, 'Octant'] = int(2)
        if(velocity["U'=U - U avg"][i] < 0 and velocity["V'=V - V avg"][i] < 0):
            velocity.at[i, 'Octant'] = int(3)
        if(velocity["U'=U - U avg"][i] > 0 and velocity["V'=V - V avg"][i] < 0):
            velocity.at[i, 'Octant'] = int(4)
        if(velocity["W'=W - W avg"][i] < 0):
            velocity.at[i, 'Octant'] = velocity['Octant'][i] * -1

    #Adding 'User Input' and 'Overall Count' 
    velocity.at[1, ''] = 'User Input'
    velocity.at[0, 'Octant ID'] = 'Overall Count'

    #A dictionary is created to find the overall octant counts and each mod ranges
    octant_counts = {'overall': {}, 'mod_ranges': {}}

    #The count of all the occurance in each octant is added to the dictionary and output file
    for oct in [1, -1, 2, -2, 3, -3, 4, -4]:
        octant_counts['overall'][oct] = velocity['Octant'].value_counts()[oct]
        velocity.at[0, oct] = octant_counts['overall'][oct]

    # the mod value
        
    mod=5000

    #

    # a function to be done in later commits
    octant_range_names(mod)

    velocity.to_excel('octant_output_ranking_excel.xlsx', index = None)

except PermissionError:
    print("ERROR : Permission required to read/write in the parent directory")
except FileNotFoundError:
    print("ERROR: File not found in the parent directory")
except ImportError:
    print("ERROR: 'pandas' was not recognised.")

end_time = datetime.now()
#total duration of the execution of our program
print('Duration of Program Execution: {}'.format(end_time - start_time))