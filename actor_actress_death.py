#Import required libaries
import csv
import re
import matplotlib.pyplot as plt

#define our variables that we will use to search each row
actor = re.compile(r'actor')
actress = re.compile(r'actress')
na = re.compile(r"\\N")

#our lists that compile each actor and actress from the IMBD .tsv file
actorList = []
actorDeath = []
actorDeathTotal = 0
actressList = []
actressDeath = []
actressDeathTotal = 0

#opens data.tsv and reads it
with open("data.tsv", encoding ="utf8") as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar='"')
    #for each row
    for row in rd:
        #if actor is in the 5th column
        if actor.search(row[4]):
            #if there is a birthdate
            if not na.search(row[2]):
                #if there is a deathdate
                if not na.search(row[3]):
                    #set some integers pulled from that row
                    life = int(row[2])
                    death = int(row[3])
                    #we add the actors name to the list
                    actorList.append(row[1])
                    #we add the actors age of death to the list
                    actorDeath.append(death-life)
        # we repeate this process for actresses
        if actress.search(row[4]):
            if not na.search(row[2]):
                if not na.search(row[3]):
                    life = int(row[2])
                    death = int(row[3])
                    actressList.append(row[1])
                    actressDeath.append(death-life)

    #an example of what we can do with this data such as finding the average
    for x in actorDeath:
        actorDeathTotal += actorDeath[x]
    
    for x in actressDeath:
        actressDeathTotal += actressDeath[x] 


    actorDeathAVG = (actorDeathTotal/len(actorDeath))
    actressDeathAVG = (actressDeathTotal/len(actressDeath))



    #Generates a histogram to compare.
    plt.hist([actorDeath, actressDeath], 100, label = ['Actors', 'Actresses'])
    plt.legend(loc = 'upper right',)
    plt.ylabel("Number of Deaths")
    plt.xlabel("Age")
    plt.show()

     



