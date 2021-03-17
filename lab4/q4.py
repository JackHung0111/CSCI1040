# Hung Yiu Pan
# 1155108381
# CSCI1040 Lab4 Q4

def reformat_as_dict(filename):
    try:
        f = open(filename)
    except OSError:
        print("File access error!")
    result = []
    line = f.readline()
    while line != "":
        result.append(eval(line.replace(',\n','')))
        line = f.readline()
    dic = {}
    for x in result:
        dic[x[2]] = []
    for x in result:
        dic2 = {}
        dic2['courseid'] = x[1]
        dic2['attendtime'] = x[0]
        dic[x[2]].append(dic2)
    f.close()
    return dic


data_dict = reformat_as_dict("q4/attendance.txt")

import json

jstr = json.dumps(data_dict, indent=4, sort_keys=True)
with open("attendance.json", "w") as f:
    f.write(jstr)