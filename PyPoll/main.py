import os
import csv

# define file path
csvpath_election = os.path.join('..', 'Resources', 'election_data.csv')

vote_count = 0
candidate_list = []
vote_count_list = []
percentages_list = []
winner_index = 0
max_votes = 0
candidate_in_list = False

with open(csvpath_election, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader_election = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader_election, None)
    
    
    for row in csvreader_election:
        vote_count = vote_count + 1

        for i in range(len(candidate_list)):
            if candidate_list[i] == row[2]:
                candidate_position = i
                candidate_in_list = True

        
        if candidate_in_list == False:
            candidate_list.append(row[2])
            vote_count_list.append(0)
            candidate_position = len(candidate_list)-1
            
        vote_count_list[candidate_position] = vote_count_list[candidate_position] + 1
            
        
        candidate_in_list = False


 

print(f"\nElection Results\n--------------------------")
print(f"Total Votes: {vote_count}\n--------------------------")
for j in range(len(candidate_list)):
    percentj = round(100*vote_count_list[j]/vote_count,3)
    percentages_list.append(percentj)

    print(f"{candidate_list[j]}: {percentages_list[j]}%  ({vote_count_list[j]})")
    if max_votes < vote_count_list[j]:
        max_votes = vote_count_list[j]
        winning_candidate_index = j

print(f"--------------------------\nWinner: {candidate_list[winning_candidate_index]}\n--------------------------\n")

with open ('poll_results.txt','w') as text_file:

    text_file.write("%s\n%s\n%s %i\n%s"%("Election Result","--------------------------","Total Votes: ",vote_count,"--------------------------"))
    
    for j in range(len(candidate_list)):
        text_file.write("\n%s: %.2f%s (%i)"%(candidate_list[j],percentages_list[j],"%",vote_count_list[j]))
    
    text_file.write("\n--------------------------\nWinner: %s \n--------------------------\n"%(candidate_list[winning_candidate_index]))



#poll_file =    open('poll_results.txt', 'w')
#poll_file.write("%s\n%s\n%s %i\n%s"%("Election Result","--------------------------","Total Votes: ",vote_count,"--------------------------"))

#for j in range(len(candidate_list)):
    #poll_file.write(f"\n")
    #poll_file.write(f"{candidate_list[j]}: {percentages_list[j]}  ({vote_count_list[j]})")

    #poll_file.write(f"--------------------------\nWinner: {candidate_list[winning_candidate_index]}\n--------------------------\n

#poll_file.append("\n%s%s %f %s %i %s"%(candidate_list[j],":",percentages_list[j],"(",vote_count_list[j],")"))
