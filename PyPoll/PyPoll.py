import os
import csv
from operator import itemgetter
votes=0
candidate=[]
candvotes={}
csvpath=os.path.join("..","Module-3","election_data.csv")
writepath=os.path.join("..","Module-3","election.txt")

with open(csvpath,'r',newline='') as csvfile:
        csvreader=csv.reader(csvfile, delimiter=',')
        csv_header = next(csvreader)
        for row in csvreader:
            votes=votes+1
            candtotal=row[2]
            if row[2] not in candidate:
                candidate.append(row[2])
                candvotes[row[2]]=1
            else:
                candvotes[row[2]]=candvotes[row[2]]+1
print("Election Results")
print("-------------------------")
print("Total Votes: "+str(votes))
print("-------------------------")
for i in candvotes:
    print(i+" "+str(round(((candvotes[i]/votes)*100)))+"% ("+str(candvotes[i])+")")
    results=(i+" "+str(round(((candvotes[i]/votes)*100)))+"% ("+str(candvotes[i])+")")
candvotes

winner=sorted(candvotes.items(),key=itemgetter(1),reverse=True)
print("-------------------------")
print("Winner "+str(winner[0]))
print("-------------------------")

with open(writepath,"w")as txt_file:

    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write(i+" "+str(round(((candvotes[i]/votes)*100)))+"% ("+str(candvotes[i])+")")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(winner[0]))
    txt_file.write("\n")
    txt_file.write("Total Votes " + str(votes))