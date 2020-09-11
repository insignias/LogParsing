import re
import csv
from collections import Counter


def parseLog(log):
    pattern = re.compile(r'[a-zA-Z]{3}  \d+ \d{2}:\d{2}')
    matchList = []
    with open(log, 'r') as fp:
        for line in fp:
            matchList.append(pattern.search(line).group())

    return matchList


def counter(matchlist):
    return Counter(matchlist)


def generateCSV(counts):
    with open('output.csv', 'w') as op:
        fieldnames = ["minute", "number_of_messages"]
        writer = csv.DictWriter(op, fieldnames=fieldnames)
        writer.writeheader()
        for data in counts:
            writer.writerow({"minute": data, "number_of_messages": counts[data]})


if __name__ == '__main__':
    generateCSV(counter(parseLog('syslog')))
