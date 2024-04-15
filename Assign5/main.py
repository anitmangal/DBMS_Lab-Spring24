import os
import time
# SELECT VendorID, tpep_pickup_datetime, RatecodeID FROM table WHERE RatecodeID > 100 AND fare_amount < 10;

inputDir = "data/yellow_tripdata_2023_feb_to_dec_2024_jan_10percent.csv"
outputFolder = "/output"
queryNo = 0


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

output_filename = "tem.txt"
# with open(output_filename, "w") as f:
#         pass

def process_output(output_filename):
    output = []
    with open(output_filename, 'r') as f:
        for line in f:
            row = line.strip().split(' ')
            output.append(row)
            # print(row)

    if os.path.exists(output_filename):
        os.remove(output_filename)

    print(output)
    output = output[:min(5,len(output))]
    return output


def select_where_query(queryNo, sel_args = None, where_args = None):
    # sel_args = "VendorID tpep_pickup_datetime"
    # where_args = "VendorID:=:2?passenger_count:=:3.0"

    print("sel_args", sel_args)
    print("where_args", where_args)

    mapDir = f"\'./mapper.py 0 {where_args}\'"
    reduceDir = f"\'./reducer.py 0 {sel_args}\'"
    outputDir = f"{outputFolder}/output{queryNo}"

    output_filename = "0.txt"
    with open(output_filename, "w") as f:
        pass

    cmd = f"hadoop jar ./hadoop-streaming-3.3.4.jar -input {inputDir} -output {outputDir} -mapper {mapDir} -reducer {reduceDir}"
    os.system(cmd)
    #time.sleep(1)
    getOutput = f"hdfs dfs -cat {outputDir}/* > {output_filename}"
    os.system(getOutput)
    cleanUp = f"hdfs dfs -rm -r {outputDir}"
    os.system(cleanUp)
    return process_output(output_filename)


def myFunc(e):
#   print(e[1])
    return -float(e[1])

def stats_page1(queryNo):

    print("popular pickup locations")

    mapDir = f"\'./mapper.py 1\'"
    reduceDir = f"\'./reducer.py 1\'"
    outputDir = f"{outputFolder}/output{queryNo}"

    output_filename = "1.txt"
    with open(output_filename, "w") as f:
        pass
        
    cmd = f"hadoop jar ./hadoop-streaming-3.3.4.jar -input {inputDir} -output {outputDir} -mapper {mapDir} -reducer {reduceDir}"
    os.system(cmd)
    #time.sleep(1)
    getOutput = f"hdfs dfs -cat {outputDir}/* > {output_filename}"
    os.system(getOutput)
    cleanUp = f"hdfs dfs -rm -r {outputDir}"
    os.system(cleanUp)
    final_output = process_output(output_filename)
    # print(final_output)
    final_output.sort(key=myFunc)
    # print(final_output)
    return {
        'Title': "Popular Pickup Locations",
        'Count': [x[1] for x in final_output],
        'Location': [x[0] for x in final_output]
    }
    

def stats_page2(queryNo):
    print("popular dropoff location")

    mapDir = f"\'./mapper.py 2\'"
    reduceDir = f"\'./reducer.py 2\'"
    outputDir = f"{outputFolder}/output{queryNo}"

    output_filename = "2.txt"
    with open(output_filename, "w") as f:
        pass
        
    cmd = f"hadoop jar ./hadoop-streaming-3.3.4.jar -input {inputDir} -output {outputDir} -mapper {mapDir} -reducer {reduceDir}"
    os.system(cmd)
    #time.sleep(1)
    getOutput = f"hdfs dfs -cat {outputDir}/* > {output_filename}"
    os.system(getOutput)
    cleanUp = f"hdfs dfs -rm -r {outputDir}"
    os.system(cleanUp)
    final_output = process_output(output_filename)
    # print(final_output)if os.path.exists(output_filename):
    # print(final_output)
    final_output.sort(key=myFunc)
    # print(final_output)

    return {
        'Title': 'Popular Dropoff Locations',
        'Location': [x[0] for x in final_output],
        'Count': [x[1] for x in final_output]
    }

def stats_page3(queryNo):
    print("busiest hour")
    mapDir = f"\'./mapper.py 3\'"
    reduceDir = f"\'./reducer.py 3\'"
    outputDir = f"{outputFolder}/output{queryNo}"

    output_filename = "3.txt"
    with open(output_filename, "w") as f:
        pass
        
    cmd = f"hadoop jar ./hadoop-streaming-3.3.4.jar -input {inputDir} -output {outputDir} -mapper {mapDir} -reducer {reduceDir}"
    os.system(cmd)
    #time.sleep(1)
    getOutput = f"hdfs dfs -cat {outputDir}/* > {output_filename}"
    os.system(getOutput)
    cleanUp = f"hdfs dfs -rm -r {outputDir}"
    os.system(cleanUp)
    final_output = process_output(output_filename)
    # print(final_output)
    final_output.sort(key=myFunc)
    # print(final_output)

    return {
        'Title': 'Busiest Hour',
        'Hour': [x[0] for x in final_output],
        'Count': [x[1] for x in final_output]
    }

def stats_page4(queryNo):
    print("revenue vs month")
    mapDir = f"\'./mapper.py 4\'"
    reduceDir = f"\'./reducer.py 4\'"
    outputDir = f"{outputFolder}/output{queryNo}"

    output_filename = "4.txt"
    with open(output_filename, "w") as f:
        pass
        
    cmd = f"hadoop jar ./hadoop-streaming-3.3.4.jar -input {inputDir} -output {outputDir} -mapper {mapDir} -reducer {reduceDir}"
    os.system(cmd)
    #time.sleep(1)
    getOutput = f"hdfs dfs -cat {outputDir}/* > {output_filename}"
    os.system(getOutput)
    cleanUp = f"hdfs dfs -rm -r {outputDir}"
    os.system(cleanUp)
    final_output = process_output(output_filename)
    # print(final_output)
    final_output.sort(key=myFunc)
    # print(final_output)
    
    return {
        'Title': 'Revenue vs Month',
        'Month': [x[0] for x in final_output],
        'Revenue': [x[1] for x in final_output]
    }


def stats_page5(queryNo):
    print("revenue vs day")
    mapDir = f"\'./mapper.py 5\'"
    reduceDir = f"\'./reducer.py 5\'"
    outputDir = f"{outputFolder}/output{queryNo}"

    output_filename = "5.txt"
    with open(output_filename, "w") as f:
        pass
        
    cmd = f"hadoop jar ./hadoop-streaming-3.3.4.jar -input {inputDir} -output {outputDir} -mapper {mapDir} -reducer {reduceDir}"
    os.system(cmd)
    #time.sleep(1)
    getOutput = f"hdfs dfs -cat {outputDir}/* > {output_filename}"
    os.system(getOutput)
    cleanUp = f"hdfs dfs -rm -r {outputDir}"
    os.system(cleanUp)
    final_output = process_output(output_filename)
    # print(final_output)
    final_output.sort(key=myFunc)
    # print(final_output)

    return {
        'Title': 'Revenue vs Day',
        'Day': [x[0] for x in final_output],
        'Revenue': [x[1] for x in final_output]
    }

def stats_page6(queryNo):
    print("busiest day ")
    mapDir = f"\'./mapper.py 6\'"
    reduceDir = f"\'./reducer.py 6\'"
    outputDir = f"{outputFolder}/output{queryNo}"

    output_filename = "6.txt"
    with open(output_filename, "w") as f:
        pass
        
    cmd = f"hadoop jar ./hadoop-streaming-3.3.4.jar -input {inputDir} -output {outputDir} -mapper {mapDir} -reducer {reduceDir}"
    os.system(cmd)
    #time.sleep(1)
    getOutput = f"hdfs dfs -cat {outputDir}/* > {output_filename}"
    os.system(getOutput)
    cleanUp = f"hdfs dfs -rm -r {outputDir}"
    os.system(cleanUp)
    final_output = process_output(output_filename)
    # print(final_output)
    final_output.sort(key=myFunc)
    # print(final_output)

    return {
        'Title': 'Busiest Day',
        'Day': [x[0] for x in final_output],
        'Count': [x[1] for x in final_output]
    }

def stats_page7(queryNo):
    print("total trips per month")
    mapDir = f"\'./mapper.py 7\'"
    reduceDir = f"\'./reducer.py 7\'"
    outputDir = f"{outputFolder}/output{queryNo}"

    output_filename = "7.txt"
    with open(output_filename, "w") as f:
        pass
        
    cmd = f"hadoop jar ./hadoop-streaming-3.3.4.jar -input {inputDir} -output {outputDir} -mapper {mapDir} -reducer {reduceDir}"
    os.system(cmd)
    #time.sleep(1)
    getOutput = f"hdfs dfs -cat {outputDir}/* > {output_filename}"
    os.system(getOutput)
    cleanUp = f"hdfs dfs -rm -r {outputDir}"
    os.system(cleanUp)
    final_output = process_output(output_filename)
    # print(final_output)
    final_output.sort(key=myFunc)
    # print(final_output)

    return {
        'Title': 'Total Trips per Month',
        'Month': [x[0] for x in final_output],
        'Count': [x[1] for x in final_output]
    }


# while(True):
#     data = int(input("\nmyMapReduce> "))
#     if data == -1:
#        print("Bye!")
#        break
#     queryNo = queryNo + 1
#     if data == 0:
#         select_where_query(queryNo)
#     elif data == 1:
#         stats_page1(queryNo)
#     elif data == 2:
#         stats_page2(queryNo)
#     elif data == 3:
#         stats_page3(queryNo)
#     elif data == 4:
#         stats_page4(queryNo)
#     elif data == 5:
#         stats_page5(queryNo)
#     elif data == 6:
#         stats_page6(queryNo)
#     elif data == 7:
#         stats_page7(queryNo)
    