filename = input('Enter name of postcode file: ')
infile = open(filename,'r')
contents = infile.readlines()
infile.close()

data = []
for i in range (len(contents)):
    infoStr = contents[i]
    infoList = infoStr.split('\t')
    postcode = int(infoList[0])
    locationList = infoList[1].split(',')
    for j in range(len(locationList)):
        locationList[j] = locationList[j].rstrip('\n')
        data.append([postcode,locationList[j]])

print(data)
    
