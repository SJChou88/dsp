# PART 1 REGULAR EXPRESSIONS.



import csv, string, re

#Degree code
with open('/Users/stephenchou/ds/metis/metisgh/prework/dsp/python/faculty.csv') as f:
    reader = csv.DictReader(f, skipinitialspace=True,delimiter=',')
    degreelist = []
    freqlist = []
    for row in reader:
        degrees = row['degree'].translate({ord(char): None for char in string.punctuation})
        for deg in degrees.split():
            deglower=deg.lower()
            if deg.lower() in degreelist:
                index = degreelist.index(deg.lower())
                freqlist[index] +=1
                #increase accumulator for corresponding degreelist
            else:
                #add deg.lower() to degreelist and add a 1 to degreelist for position
                degreelist.append(deg.lower())
                freqlist.append(1)

#Title Code
with open('/Users/stephenchou/ds/metis/metisgh/prework/dsp/python/faculty.csv') as f:
    reader = csv.DictReader(f, skipinitialspace=True,delimiter=',')
    titlelist =[]
    tfreqlist =[]
    ofbio = re.compile('(\s*)[A-Za-z]{2} Biostatistics(\s*)')
    for row in reader:
        title = ofbio.sub('',row['title'])
        if title.lower() in titlelist:
            index = titlelist.index(title.lower())
            tfreqlist[index]+=1
        else:
            titlelist.append(title.lower())
            tfreqlist.append(1)
            
#Email code
with open('/Users/stephenchou/ds/metis/metisgh/prework/dsp/python/faculty.csv') as f:
    reader = csv.DictReader(f, skipinitialspace=True,delimiter=',')
    emaillist =[]
    for row in reader:
        emaillist.append(row['email'])
    print(emaillist)

#Unique Email domain code
with open('/Users/stephenchou/ds/metis/metisgh/prework/dsp/python/faculty.csv') as f:
    reader = csv.DictReader(f, skipinitialspace=True,delimiter=',')
    uniquedomainlist =[]
    rememail = re.compile('^[a-zA-Z0-9_.+-]+@')
    for row in reader:
        emaildom = rememail.sub('',row['email'])
        if emaildom not in uniquedomainlist:
            uniquedomainlist.append(emaildom)
    print(uniquedomainlist)