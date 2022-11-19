from datetime import datetime
start_time = datetime.now()

def scorecard():
    
    print("The function was called sucessfully.")
    print("Please wait while the output file is created.")
	#the informationon the scoreboard will be stored in this dictionary
	innings_01 = {'runs': 0, 'wickets': 0, 'balls': 0, 'batting': {player : {'runs': 0, 'balls': 0, '4s': 0, '6s': 0, 'Status': ''} for player in pak_players}, 'bowling': {player : {'runs': 0, 'balls': 0, 'maidens': 0, 'wickets': 0, 'nb': 0, 'wide': 0} for player in ind_players}, 'Extras': {'byes': 0, 'nb': 0, 'lb': 0, 'wide': 0, 'pty': 0}, 'dnb': pak_players.copy(), 'fow': [], 'powerplay': 0}
	innings_02 = {'runs': 0, 'wickets': 0, 'balls': 0, 'batting': {player : {'runs': 0, 'balls': 0, '4s': 0, '6s': 0, 'Status': ''} for player in ind_players}, 'bowling': {player : {'runs': 0, 'balls': 0, 'maidens': 0, 'wickets': 0, 'nb': 0, 'wide': 0} for player in pak_players}, 'Extras': {'byes': 0, 'nb': 0, 'lb': 0, 'wide': 0, 'pty': 0}, 'dnb': ind_players.copy(), 'fow': [], 'powerplay': 0}


from platform import python_version
ver = python_version()

if ver == "3.8.10":
	print("Correct Version Installed")
else:
	print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

# we define all the players of both the teams
india_players = ['Rohit Sharma (c)', 'KL Rahul', 'Virat Kohli', 'Suryakumar Yadav', 'Dinesh Karthik (w)', 'Hardik Pandya', 'Ravindra Jadeja', 'Bhuvneshwar Kumar', 'Avesh Khan', 'Yuzvendra Chahal', 'Arshdeep Singh']
pakistan_players = ['Babar Azam (c)', 'Mohammad Rizwan (w)', 'Fakhar Zaman', 'Iftikhar Ahmed', 'Khushdil Shah', 'Asif Ali', 'Shadab Khan', 'Mohammad Nawaz', 'Naseem Shah', 'Haris Rauf', 'Shahnawaz Dahani']
all_players = ind_players + pak_players

#calling the function
try:
 scorecard()
except:
 print("Function was not called correctly.")