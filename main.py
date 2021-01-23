# import re
import os

# -------------------------------------------------------------------------

desiredregex = re.compile(r'chess', re.IGNORECASE)
inputFile = '2021-01-08.csv' # 2021-01-08.csv
outputFile = 'output.txt'

subCountFile = 'filtered_output.txt'
noMinSubCount = 200

midFile = 'midfile.txt' #this can be used to search for other queries
saveMidFile = True #if set to false the midFile will be deleted

# -------------------------------------------------------------------------

lineStart = re.compile(r'^[a-zA-Z0-9]+,') # match real_name,
lineEnd = re.compile(r',\d{4}-\d{2}-\d{2},\d+$') # match ,created_date,subs
subcount = re.compile(r'\d+$')

def isEmpty(listname):
    if len(listname) == 0: #if list is empty
        return True
    else:
        return False

def fixFile():
    linelist = []
    with open(inputFile,'r', encoding='utf-8') as f:
        for line in f:
            currentline = line.rstrip('\n')
            linelist.append(currentline)

            match = lineEnd.findall(currentline) #returns list containing the match, I'm sure there is a better way

            if isEmpty(match) == False: # if match occurs join the linelist together and write to midFile
                my_lst_str = ' '.join(map(str, linelist))

                with open(midFile,'a', encoding='utf-8') as mid:
                    mid.write(my_lst_str)
                    mid.write('\n')

                linelist = [] #clear list for further use

def fixHeader(filename): #TODO: note;strings are immutabe
     #todo: fix header thingy: real_name,desc,created_date,subs
     with open(filename, "a+") as f:
        f.seek(-10)
        f.write("appended text")


def findAndOutRegex():
    with open(midFile,'r', encoding='utf-8') as f:
        for line in f:
            currentline = line.rstrip('\n')
            match = desiredregex.findall(currentline)

            if isEmpty(match) == False:
                with open(outputFile,'a', encoding='utf-8') as out:
                    out.write(currentline)
                    out.write('\n')

def saveMidF():
    if saveMidFile == False:
        os.remove(midFile)

def minSubcount():
     with open(outputFile,'r', encoding='utf-8') as f:
        for line in f:
            currentline = line.rstrip('\n')
            match = subcount.findall(currentline)
            if int(match[0]) > noMinSubCount:
                with open(subCountFile,'a', encoding='utf-8') as subc:
                    subc.write(currentline)
                    subc.write('\n')

def getSubNames(): #can be done more nicely
    with open(outputFile,'r', encoding='utf-8') as f:
        for line in f:
            currentline = line.rstrip('\n')
            aa = re.compile(r'^[a-zA-Z0-9]+')
            match = aa.findall(currentline)
            with open('subnames.txt','a', encoding='utf-8') as f:
                f.write(str(match))
                f.write('\n')

def deleteduplicate(inputfilename, outputfilename):
    lines_seen = set() # holds lines already seen
    with open(outputfilename, "w") as output_file:
        for line in open(inputfilename, "r"):
            if line not in lines_seen: # check if line is not duplicate
                output_file.write(line)
                lines_seen.add(line)


if __name__ == '__main__':
    # fixFile()
    # findAndOutRegex()
    # saveMidF()
    # minSubcount()
    # deleteduplicate("subnames.txt", "subnames_a.txt")


