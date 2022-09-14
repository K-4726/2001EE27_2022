# I have used pandas module for my code
import csv
import pandas as pd
velo=pd.read_csv("octant_input.csv")

#2-D dataframe
velocity=pd.DataFrame(velo)
#uptill now we have read the input file
# now we will store the mean values 
velocity['U Avg']=' '
velocity['U Avg'][0]=velocity['U'].mean()
velocity['V Avg']=' '
velocity['V Avg'][0]=velocity['V'].mean()
velocity['W Avg']=' '
velocity['W Avg'][0]=velocity['W'].mean()

#filling of the next coluns i.e U-Uavg
velocity["U'=U - U avg"]=' '
velocity["U'=U - U avg"]= -velocity['U Avg'][0]+velocity['U']
velocity["V'=V - V avg"]=' '
velocity["V'=V - V avg"]= -velocity['V Avg'][0]+velocity['V']
velocity["W'=W - W avg"]=' '
velocity["W'=W - W avg"]= -velocity['W Avg'][0]+velocity['W']
velocity['octant']=' '

# Filling of the rows for all values 
for i in range(velocity['Time'].size):
  if(velocity["U'=U - U avg"][i]>0 and velocity["V'=V - V avg"][i]>0):velocity['octant'][i]=1
  if(velocity["U'=U - U avg"][i]<0 and velocity["V'=V - V avg"][i]>0):velocity['octant'][i]=2
  if(velocity["U'=U - U avg"][i]<0 and velocity["V'=V - V avg"][i]<0):velocity['octant'][i]=3
  if(velocity["U'=U - U avg"][i]>0 and velocity["V'=V - V avg"][i]<0):velocity['octant'][i]=4
  if(velocity["W'=W - W avg"][i]<0):velocity['octant'][i]*=-1

# Here you can change mod value

mod = 5000

#
 
# counts printing
data =  {1:0,-1:0,2:0,-2:0,3:0,-3:0,-4:0,4:0}
velo1 = velocity['OCTANT'].value_counts()
print(data)
velo2 = pd.DataFrame(columns=range(30000))

# ID of actant for all values
velocity['Assigned Octant']=' '
velocity['1']=' '
velocity['-1']=' '
velocity['2']=' '
velocity['-2']=' '
velocity['3']=' '
velocity['-3']=' '
velocity['4']=' '
velocity['-4']=' '

# loop over our defined column 
for i in velocity['OCTANT']:
  data[i]+=1


velocity['1'][0]=data[1]
velocity['-1'][0]=data[-1]
velocity['2'][0]=data[2]
velocity['-2'][0]=data[-2]
velocity['3'][0]=data[3]
velocity['-3'][0]=data[-3]
velocity['4'][0]=data[4]
velocity['-4'][0]=data[-4] 

velocity['Assigned Octant'][1]='Mod(intial hardcode 5000)'

