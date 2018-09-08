#import budget_data.csv
import os
import csv
month=0
chg=0
prv=0
inc=["",0]
dec=["",9999999999]
avgpl=[]
csvpath=os.path.join("..","Module-3","budget_data.csv")
write=os.path.join("..","Module-3","budget_analysis.txt")
with open(csvpath,'r',
) as csvfile:
        csvreader=csv.reader(csvfile, delimiter=',')
        csv_header = next(csvreader)
        total=0
        for row in csvreader:
            totalpl= (int(row[1]))
            total+=totalpl
            month=month+1
            avgpl.append(int(row[1]))
            chg=int(row[1])-prv
            prv=int(row[1])
            if(chg>inc[1]):
                inc[1]=chg
                largedate=row[0]
            if(chg<dec[1]):
                dec[1]=chg
                smalldate=row[0]
        
print("Financial Analysis")
print("--------------------")
print("Total Months: "+str(month))
print("Total: "+str(totalpl))
print("Average Change: "+str(round(sum(avgpl) / int(month))))
print("Greatest Increase: "+str(largedate)+" $("+str(inc[1])+")")
print("Greatest Decrease: "+str(smalldate)+" $("+str(dec[1])+")")

with open(write,'w') as analysis:
    analysis.write("Financial Analysis")
    analysis.write("\n")
    analysis.write("--------------------")
    analysis.write("\n")
    analysis.write("Total Months: "+str(month))
    analysis.write("\n")
    analysis.write("Total: "+str(totalpl))
    analysis.write("\n")
    analysis.write("Average Change: "+str(round(sum(avgpl) / int(month))))
    analysis.write("\n")
    analysis.write("Greatest Increase: "+str(largedate)+" $("+str(inc[1])+")")
    analysis.write("\n")
    analysis.write("Greatest Decrease: "+str(smalldate)+" $("+str(dec[1])+")")