import csv, string, re

#Q6
with open('/Users/stephenchou/ds/metis/metisgh/prework/dsp/python/faculty.csv') as f:
    reader = csv.DictReader(f, skipinitialspace=True,delimiter=',')
    ofbio = re.compile('(\s*)[A-Za-z]{2} Biostatistics(\s*)')
    regexname = re.compile('[A-Za-z]{3,}')
    namelist = []
    infolist =[]
    for row in reader:
        #lastname = 
        name = regexname.findall(row['name'])[-1]
        degree = row['degree'].translate({ord(char): None for char in string.punctuation})
        email = row['email']
        title = ofbio.sub('',row['title'])
        if name in namelist:
            index = namelist.index(name)
            infolist[index].append([degree, title, email])
        else:
            namelist.append(name)
            infolist.append([[degree, title, email]])
    faculty_dict =dict(zip(namelist,infolist))
    for i in range(3):
        print(list(faculty_dict.keys())[i], list(faculty_dict.values())[i])
        
#Q7
with open('/Users/stephenchou/ds/metis/metisgh/prework/dsp/python/faculty.csv') as f:
    reader = csv.DictReader(f, skipinitialspace=True,delimiter=',')
    ofbio = re.compile('(\s*)[A-Za-z]{2} Biostatistics(\s*)')
    regexname = re.compile('[A-Za-z]{3,}')
    namelist = []
    infolist =[]
    for row in reader:
        #
        name = regexname.findall(row['name'])[0], regexname.findall(row['name'])[-1]
        degree = row['degree'].translate({ord(char): None for char in string.punctuation})
        email = row['email']
        title = ofbio.sub('',row['title'])
        if name in namelist:
            index = namelist.index(name)
            infolist[index].append([degree, title, email])
        else:
            namelist.append(name)
            infolist.append([[degree, title, email]])
    professor_dict =dict(zip(namelist,infolist))
    for i in range(3):
        print(list(professor_dict.keys())[i], list(professor_dict.values())[i])
    #example sorted by first name
    for i in sorted(list(professor_dict.keys()))[:3]:
        print(i,professor_dict[i])
    #example sorted by last name
    for i in sorted(list(professor_dict.keys()),key = lambda k: k[1])[:3]:
        print(i,professor_dict[i])
    f.close