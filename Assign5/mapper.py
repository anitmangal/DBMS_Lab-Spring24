#!/usr/bin/env python3

import sys
from collections import defaultdict

cols = {'VendorID': "0",
        'tpep_pickup_datetime': "1",
        'tpep_dropoff_datetime': "2",
        'passenger_count': "3",
        'trip_distance': "4",
        'RatecodeID': "5",
        'store_and_fwd_flag': "6",
        'PULocationID': "7",
        'DOLocationID': "8",
        'payment_type': "9",
        'fare_amount': "10",
        'extra': "11",
        'mta_tax': "12",
        'tip_amount': "13",
        'tolls_amount': "14",
        'improvement_surcharge': "15",
        'total_amount': "16",
        'congestion_surcharge': "17",
        'airport_fee': "18"
        }


def map_select_where(args):
    for l in sys.stdin:
        # split all lines on comma maybe
        if len(l) == 0:
            continue

        line = (l.strip(" ")).split(",")
        take = True

        for arg in args:
            if arg[1] == '!':
                if line[arg[0]] == arg[2]:
                    take = False
                    break
            elif arg[1] == '<':
                if line[arg[0]] >= arg[2]:
                    take = False
                    break
            elif arg[1] == '>':
                if line[arg[0]] <= arg[2]:
                    take = False
                    break
            elif arg[1] == '=':
                if line[arg[0]] != arg[2]:
                    take = False
                    break
        if take:
            key = line[0]
            val = l
            print(f"{key}\t{val}")
            with open("mapper_log.txt", "a") as f:
                f.write(f"{key}\t{val}->Taken\n")


if (sys.argv[1] == "0"):
    arguments = (sys.argv[2]).split('?')
    for idx, a in enumerate(arguments):
        a = list(a.split(':'))
        a[0] = int(cols[a[0]])
        arguments[idx] = a
    map_select_where(args=arguments)

elif (sys.argv[1] == "1"):  # popular pickup locations
    for line in sys.stdin:
        # Split the line into fields
        fields = line.strip().split(',')
        # Extract pick-up ocations
        pickup = fields[7]
        # Emit key-value pairs
        with open("check.txt", "a") as f:
            f.write(f"{pickup} {1}")
        print(f"{pickup}\t{1}")

elif (sys.argv[1] == "2"):  # popular dropoff location
    for line in sys.stdin:
        # Split the line into fields
        fields = line.strip().split(',')
        # Extract drop-off locations
        dropoff = fields[8]
        # Emit key-value pairs
        print(f"{dropoff}\t{1}")

elif (sys.argv[1] == "3"):  # busiest hour
    for line in sys.stdin: # 2023-02-13 17:11:02
        fields = line.strip().split(',')
        pickup_datetime = fields[1]
        pickup_hour = pickup_datetime.split(':')[0][-2:]
        print(f"{pickup_hour}\t1")

elif (sys.argv[1] == "4"):  # revenue vs month
    for line in sys.stdin:
        fields = line.strip().split(',')
        pickup_datetime = fields[1]
        pickup_month = pickup_datetime.split('-')
        if len(pickup_month) > 1:
            month = pickup_month[1]
            revenue = float(fields[16])
            print(f"{month}\t{revenue}")

elif (sys.argv[1] == "5"):  # revenue vs day
    for line in sys.stdin:
        fields = line.strip().split(',')
        pickup_datetime = fields[1]
        pickup_day = pickup_datetime.split('/')[0]
        if fields[16] == "total_amount":
            continue
        revenue = float(fields[16])
        print(f"{pickup_day}\t{revenue}")

elif (sys.argv[1] == "6"):  # busiest day 
    for line in sys.stdin:
        fields = line.strip().split(',')
        pickup_datetime = fields[1]
        pickup_day = pickup_datetime.split('/')[0]
        print(f"{pickup_day}\t1")

elif (sys.argv[1] == "7"):  # total trips vs month
    for line in sys.stdin:
        fields = line.strip().split(',')
        pickup_datetime = fields[1]
        pickup_month = pickup_datetime.split('-')
        if len(pickup_month) <= 1:
            continue
        month = pickup_month[1]
        print(f"{month}\t1")
