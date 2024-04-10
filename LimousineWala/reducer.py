#!/usr/bin/env python3
import sys

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


def tokenise(sel):
    global cols
    curArg = ""
    sel_args = []
    for s in sel:
        if (s == ','):
            sel_args += [int(cols[curArg])]
            curArg = ""
        elif s == ' ':
            continue
        else:
            curArg += s
    if curArg != "":
        sel_args += [int(cols[curArg])]
    return sel_args


def reduce(args):
    for line in sys.stdin:
        # split all lines on comma maybe
        if line[0] == '\t':
            continue
        key, val = line.strip(" ").split("\t")
        val = val.split(',')
        for i in args:
            print(val[i], end=" ")
        print("")
        pass


if (sys.argv[1] == "0"):  # select where
    arguments = []
    for arg in sys.argv[2:]:
        arguments.append(int(cols[arg]))
    reduce(args=arguments)

elif (sys.argv[1] == "1"):  # popular pickup locations
    curr_loc = ""
    curr_count = 0
    for line in sys.stdin:
        key, values = line.strip().split('\t')
        if (key == curr_loc or curr_loc == ""):
            curr_loc = key
            curr_count += int(values)
        else:
            print(curr_loc, curr_count)
            curr_count = int(values)
            curr_loc = key

elif (sys.argv[1] == "2"):  # popular dropoff location
    curr_loc = ""
    curr_count = 0
    for line in sys.stdin:
        key, values = line.strip().split('\t')
        if (key == curr_loc or curr_loc == ""):
            curr_loc = key
            curr_count += int(values)
        else:
            print(curr_loc, curr_count)
            curr_count = int(values)
            curr_loc = key
    print(curr_loc, curr_count)

elif (sys.argv[1] == "3"):  # busiest hour
    current_hour = None
    current_count = 0
    hour = None

    for line in sys.stdin:
        line = line.strip()
        hour, count = line.split('\t', 1)
        try:
            count = int(count)
        except ValueError:
            continue

        if current_hour == hour:
            current_count += count
        else:
            if current_hour:
                print(current_hour,current_count)
            current_count = count
            current_hour = hour

    if current_hour == hour:
        print(current_hour,current_count)

elif (sys.argv[1] == "4"):  # revenue vs month
    current_month = None
    current_revenue = 0
    for line in sys.stdin:
        month, revenue = line.strip().split('\t')
        revenue = float(revenue)
        if current_month == month:
            current_revenue += revenue
        else:
            if current_month:
                print(current_month, current_revenue)
            current_revenue = revenue
            current_month = month
    if current_month == month:
        print(current_month, current_revenue)

elif (sys.argv[1] == "5"):  # revenue vs day of the week
    current_day = None
    current_revenue = 0

    for line in sys.stdin:
        day, revenue = line.strip().split('\t')
        revenue = float(revenue)
        if current_day == day:
            current_revenue += revenue
        else:
            if current_day:
                print(current_day,current_revenue)
            current_revenue = revenue
            current_day = day
    if current_day == day:
        print(current_day,current_revenue)

elif (sys.argv[1] == "6"):  # busiest day of the week
    current_day = None
    current_count = 0

    for line in sys.stdin:
        day, count = line.strip().split('\t')
        count = int(count)
        if current_day == day:
            current_count += count
        else:
            if current_day:
                print(current_day, current_count)
            current_count = count
            current_day = day
    if current_day == day:
        print(current_day, current_count)

elif (sys.argv[1] == "7"):  # total trips vs month
    current_month = None
    current_count = 0

    for line in sys.stdin:
        month, count = line.strip().split('\t')
        count = int(count)
        if current_month == month:
            current_count += count
        else:
            if current_month:
                print(current_month,current_count)
            current_count = count
            current_month = month

    if current_month == month:
        print(current_month,current_count)

