from datetime import datetime
start_time = datetime.now()

def scorecard():
    
    print("The function was called sucessfully.")
    print("Please wait while the output file is created.")
	#the informationon the scoreboard will be stored in this dictionary
	innings_01 = {'runs': 0, 'wickets': 0, 'balls': 0, 'batting': {player : {'runs': 0, 'balls': 0, '4s': 0, '6s': 0, 'Status': ''} for player in pak_players}, 'bowling': {player : {'runs': 0, 'balls': 0, 'maidens': 0, 'wickets': 0, 'nb': 0, 'wide': 0} for player in ind_players}, 'Extras': {'byes': 0, 'nb': 0, 'lb': 0, 'wide': 0, 'pty': 0}, 'dnb': pak_players.copy(), 'fow': [], 'powerplay': 0}
	innings_02 = {'runs': 0, 'wickets': 0, 'balls': 0, 'batting': {player : {'runs': 0, 'balls': 0, '4s': 0, '6s': 0, 'Status': ''} for player in ind_players}, 'bowling': {player : {'runs': 0, 'balls': 0, 'maidens': 0, 'wickets': 0, 'nb': 0, 'wide': 0} for player in pak_players}, 'Extras': {'byes': 0, 'nb': 0, 'lb': 0, 'wide': 0, 'pty': 0}, 'dnb': ind_players.copy(), 'fow': [], 'powerplay': 0}
    
    #For finding maiden over we have to store runs gave by the bowler_curr before giving the over
	initial=-1

	#Creating output of scoreboard by reading the inning files
	with open('pak_inns1.txt', 'r') as pakistan_inns, open('india_inns2.txt', 'r') as india_inns, open('output.txt','w') as output:
		# Input file reading is done now
		tot_lines1 = pakistan_inns.readlines()
		tot_lines2 = india_inns.readlines()

		# Let's define a variable cnt to mark the player who is batting
		cnt=0
		print("", file=output)

		# Now the following loops will go through the innings of both the teams
		for innings, lines in zip([innings_01, innings_02], [tot_lines1, tot_lines2]):

			#This loop, loops through the lines of the comment section for getting the information	
			for info in [line for line in lines if line.strip()]:

				#extracting the names of the batsmen and bowler, result and the over using the information in line
				batter_curr= getPlayer(info.split(",")[0].split(" ", 1)[1].split("to")[1].strip())
				bowler_curr = getPlayer(info.split(",")[0].split(" ", 1)[1].split("to")[0].strip())
				outcome = info.split(",")[1].strip()
				over=info.split(",")[0].split(" ", 1)[0].strip()


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