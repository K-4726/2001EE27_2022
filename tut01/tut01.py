# I have used pandas module for my code
import csv
import pandas as pd
velocity=pd.read_csv("octant_input.csv")

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

