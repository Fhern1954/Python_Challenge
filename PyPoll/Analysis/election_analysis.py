#Dependencies
import os
import csv

#Path to collect data from Resources folder
poll_csv = os.path.join('Resources', 'election_data.csv')

votes = []
candidates = []
occurance = []
percentage =[]

#Read in the csv file
with open(poll_csv, 'r') as csvfile:
    poll_txt = os.path.join('election_results.txt')
    with open(poll_txt, 'w') as datafile:
    #Split the data on commas
        csvreader = csv.reader(csvfile, delimiter=',')
        #remove the header row
        csv_header = next(csvreader)

        for row in csvreader:
            votes.append(row[2])
        total_votes = len(votes)
        print(" ")
        print("Election Results")
        print("---------------------------------------------")
        print(f'Total Votes: {total_votes}')
        print("---------------------------------------------")


    #pull list of candidates
        for name in votes:
            if name not in candidates:
                candidates.append(name)
        # print(candidates)


    #count votes for each candidate
    #From "Kite" website https://www.kite.com/python/answers/how-to-count-the-number-of-occurrences-of-an-element-in-a-list-in-python
        for x in (candidates):
            occurance.append(votes.count(x))
        # print(f'{occurance}')


    #calculate percentages
        total = sum(occurance)
        # print(total)

        for x in (occurance):
            percent = x / total * 100
            percentage.append(percent)
        # print(f'{percentage}%')
        # print("-----------------------------------------------")



    #print results
        for x in range(len(candidates)):
            print(f'{candidates[x]}: {percentage[x]:.3f}% ({occurance[x]})')
            
        print("-------------------------------------------------") 



    # determine and annouce the winner
        win = max(occurance)
        winner = (candidates[occurance.index(win)])
        print(f'Winner: {winner}')
        print("-------------------------------------------------")

    #Works!!!!!


    # Specify file to write to
        # poll_txt = os.path.join('election_results.txt')

        # Open the file using "write" mode. Specify the variable to hold the contents
        # with open(poll_txt, 'w') as datafile:

            # Initialize txt.writer
        

        # Write rows
        datafile.write(" \n")
        datafile.write("Election Results\n")
        datafile.write("---------------------------------------------\n")
        datafile.write(f'Total Votes: {total_votes}\n')
        datafile.write("---------------------------------------------\n")
        for x in range(len(candidates)):
            datafile.write(f'{candidates[x]}: {percentage[x]:.3f}% ({occurance[x]})\n')
        datafile.write("-------------------------------------------------\n")
        datafile.write(f'Winner: {winner}\n')
        datafile.write("-------------------------------------------------")



