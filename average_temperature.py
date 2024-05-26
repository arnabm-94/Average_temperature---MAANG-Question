
'''
##MAANG Question

CALCULATE AVERAGE TEMPERATURE 

Take user input for number of days for which the user wants to input the temperature. 
Calculate the average temperature and also mention how many days have the temperature and
also mention how many days have the temperature above the average temperature.  

'''

numDays = int(input ("How many day's temperature do you want to calculate?"))

total = 0 
temp = []

for i in range (numDays):
    nextDay = int(input("Day" + str(i+1)+ "'s high temp:"))

    temp.append(nextDay)
total += temp[i]

avg = round(total/numDays, 2)
print("\n Average =" + str(avg))

above = 0
for i in temp:
    if i> avg :
        above += 1

print(str(above) + "day(s) above average")

