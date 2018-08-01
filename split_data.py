#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import sys

args = sys.argv
split_data =[[]]

f = open(args[1])
s = f.read()
f.close()
#data = s.replace(' ', '')

split_data = [s[i: i+180] for i in range(0, len(s), 180)]
print(split_data)

l = args[1].split('.')
name = l[0]+'_signal.'+l[1]

print(split_data[0])

f=open(name, 'w')
for i in range(len(split_data)):
    f.write("\n".join(split_data))
f.close()
