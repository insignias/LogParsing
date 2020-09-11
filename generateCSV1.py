import re
import csv
from collections import Counter

fieldList= []
d = {}

def parseLog(log):

    pattern = re.compile(r'(.*? \d+ \d{2}:\d{2}):\d{2} \w+ ([\w.\s]+)')
    matchList = []
    with open(log, 'r') as fp:
        for line in fp:
            gp = pattern.search(line)
            matchList.append(gp.group(1))
            if gp.group(2) not in fieldList:
                fieldList.append(gp.group(2))
            if gp.group(1) not in d:
                d[gp.group(1)] = {}
            if gp.group(2) not in d[gp.group(1)]:
                d[gp.group(1)][gp.group(2)] = 1
            else:
                d[gp.group(1)][gp.group(2)] += 1

    return matchList


def counter(matchlist):
    return Counter(matchlist)


def generateCSV(counts=None):
    with open('output1.csv', 'w') as op:
        fieldnames = ["minute", "number_of_messages"] + fieldList
        writer = csv.DictWriter(op, fieldnames=fieldnames)
        writer.writeheader()
        for k,v in d.items():
            da = {"minute": k, "number_of_messages": counts[k]}
            for key,val in v.items():
                da.update({key: val})
            writer.writerow(da)

if __name__ == '__main__':
    generateCSV(counter(parseLog('syslog')))