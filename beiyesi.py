#!usr/bin/env python
# -*- coding: UTF-8 -*-
#@author by blue
#time 2018
#----------------------

import re
import sys

DataLength = 100
Attr_num = 10
Val_num = 5
tr_data = []
test_data = []
tr_lg = ts_lg = 0
attrs = [0 for i in range(DataLength)]
wd = 0  ### the number of attributes,  included   category{yes,no}
values = [set() for i in range(2)]

val_ls = []
pro_p = [[0 for i in range(Val_num)] for j in range(Attr_num)]
pro_n = [[0 for i in range(Val_num)] for j in range(Attr_num)]
pos = neg = 0


def naive_bayes(ls):
    res = [0 for i in range(len(val_ls[wd - 1]))]
    # print wd
    # print res
    p = q = 1.0
    for i in range(wd - 1):
        k = val_ls[i].index(ls[i])
        p *= float(pro_p[i][k]) / (pro_p[i][k] + pro_n[i][k])
        q *= float(pro_n[i][k]) / (pro_p[i][k] + pro_n[i][k])
    res[0] = p
    res[1] = q
    # print res
    return val_ls[wd - 1][res.index(max(res))]


if __name__ == '__main__':
    # for a in sys.argv:
    #    print a
    train = "data/bayes_train.txt"
    test = "data/bayes_test.txt"
    if len(sys.argv) > 1:
        train = sys.argv[1]
        test = sys.argv[2]
    fp1 = open(train, "r")
    fp2 = open(test, "r")
    i = 0
    for line in fp1:
        line = re.sub(r"\n\r", "", line)
        if i == 0:
            attrs = line.split()[1:]
            wd = len(attrs)
            i += 1
            values = [set() for j in range(wd)]
            val_ls = [0 for j in range(wd)]
            continue
        tr_data.append(line.split()[1:])
        for j in range(wd):
            values[j].add(tr_data[tr_lg][j])
        tr_lg += 1

    for i in range(wd):
        val_ls[i] = list(values[i])
        # print val_ls#,'here'

    for i in range(tr_lg):
        for j in range(wd - 1):
            k = val_ls[j].index(tr_data[i][j])
            if tr_data[i][wd - 1] == 'Yes':
                pro_p[j][k] += 1
                pos += 1
            else:
                pro_n[j][k] += 1
                neg += 1
    pos = pos / (wd - 1)
    neg = neg / (wd - 1)
    # print pos,neg
    for line in fp2:
        line = re.sub(r"\n\r", "", line)
        test_data.append(line.split())
        ts_lg += 1
    fp1.close()
    fp2.close()
    # print tr_lg,ts_lg,attrs,wd,tr_data[0:2]
    # for i in range(wd-1):
    #     print 'pos:',pro_p[i][0:len(val_ls[i])],"neg:",pro_n[i][0:len(values[i])]
    # print test_data
    for ls in test_data:
        print ls, '\t\ttypes:', naive_bayes(ls)