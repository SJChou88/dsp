#Email code
with open('/Users/stephenchou/ds/metis/metisgh/prework/dsp/python/faculty.csv') as f:
    reader = csv.DictReader(f, skipinitialspace=True,delimiter=',')
    emaillist =[]
    ofile = open('/Users/stephenchou/ds/metis/metisgh/prework/dsp/python/emails.csv','w',newline='')
    writer = csv.writer(ofile)
    for row in reader:
        emaillist.append(row['email'])
        writer.writerow([row['email']])
    print(emaillist)
    ofile.close()
    f.close()