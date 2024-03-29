from datetime import datetime
from decimal import DivisionByZero
start_time = datetime.now()


def octant_range_names(mod=5000):
    print("Please wait while the output file is processed. :]");
    #A function to find the count in each intervals
    octact_identification(mod)

    #A diactionary 'octant_name_id_map' 
    octant_name_id_map = {1:"Internal Outward Interaction", -1:"External Outward Interaction", 2:"External Ejection", -2:"Internal Ejection", 3:"External Inward Interaction", -3:"Internal Inward Interaction", 4:"Internal Sweep", -4:"External Sweep"}
    
    #The oct_rank dictionary used as a map
    oct_rank = {key: rank for rank, key in enumerate(sorted(octant_counts['overall'], key=octant_counts['overall'].get, reverse=True), 1)}

    #The rank of each octant is added to the output file
    for oct in [1, -1, 2, -2, 3, -3, 4, -4]:
        velocity.at[0, f'Rank of {oct}'] = oct_rank[oct]
    
    #Adding Octant ID of octant having rank 1
    velocity.at[0, 'Octant ID of Rank 1'] = list(oct_rank.keys())[list(oct_rank.values()).index(1)]
    
    #The Octant name -> octant id
    velocity.at[0, 'Octant Name of Rank 1'] = octant_name_id_map[list(oct_rank.keys())[list(oct_rank.values()).index(1)]]

    # The ranks of each octant, Octant ID and name of the octant with Rank 1 is added to the output file for each mod range
    for i, (mod_range, octant_count) in enumerate(octant_counts['mod_ranges'].items()):
        oct_rank = {key: rank for rank, key in enumerate(sorted(octant_count, key=octant_count.get, reverse=True), 1)}
        for oct in [1, -1, 2, -2, 3, -3, 4, -4]:
            velocity.at[2 + i, f'Rank of {oct}'] = oct_rank[oct]
        velocity.at[2 + i, 'Octant ID of Rank 1'] = list(oct_rank.keys())[list(oct_rank.values()).index(1)]
        velocity.at[2 + i, 'Octant Name of Rank 1'] = octant_name_id_map[list(oct_rank.keys())[list(oct_rank.values()).index(1)]]

    velocity.at[11, 1] = 'Octant ID'
    velocity.at[11, -1] = 'Octant Name'
    velocity.at[11, 2] = 'Count of Rank 1 Mod Values'
    
    # The total number of occurences of Rank 1
    for i, oct in enumerate([1, -1, 2, -2, 3, -3, 4, -4]):
        velocity.at[12 + i, 1] = oct
        velocity.at[12 + i, -1] = octant_name_id_map[oct]
        counts_rank1 = 0
        for mod_range, octant_count in octant_counts['mod_ranges'].items():
            oct_rank = {key: rank for rank, key in enumerate(sorted(octant_count, key=octant_count.get, reverse=True), 1)}
            if oct_rank[oct] == 1:
                counts_rank1 += 1
        velocity.at[12 + i, 2] = counts_rank1


def octact_identification(mod=5000):
    # The mod range value  added to the output file
    velocity.at[1, 'Octant ID'] = 'Mod ' + str(mod)

    #An array wirh boundary values for each mod intervals
    range_values = [0]
    while range_values[-1] < len(velocity.index):
        range_values.append(range_values[-1] + mod)
    range_values[-1] = len(velocity.index)

    #The total count of octant occured are evaluated for each mod intervals
    for i in range(len(range_values) - 1):

        #found  range label and added it to the 'mod_ranges' dictionary inside the 'octant_counts' dictionary and o/p file
        range_name = str(range_values[i]) + " - " + str(range_values[i + 1] - 1)
        octant_counts['mod_ranges'][range_name] = {}
        velocity.at[2 + i, 'Octant ID'] = range_name

        # evaluation of occurances in given range for octants
        for oct in [1, -1, 2, -2, 3, -3, 4, -4]:
            octant_counts['mod_ranges'][range_name][oct] = velocity['Octant'].iloc[range_values[i]:(range_values[i + 1])].value_counts()[oct]
            velocity.at[2 + i, oct] = octant_counts['mod_ranges'][range_name][oct] 

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
    print("Program execution started successfully.")
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

print("Output file is ready ^_^ ")
end_time = datetime.now()
#total duration of the execution of our program
print('Duration of Program Execution: {}'.format(end_time - start_time))


