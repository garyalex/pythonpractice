#!/usr/bin/env python3

import csv

with open('iplist.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count != 0:
            print(f'Country: {row[0]} \tCity: {row[1]} \tIPv4 Addr: {row[2]}')
        line_count += 1
