from flask import Flask, render_template, request, redirect,jsonify
from main import stats_page1, stats_page2, stats_page3, stats_page4, stats_page5, stats_page6, stats_page7, select_where_query  
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from multiprocessing import Pool, cpu_count

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['CORS_HEADERS'] = 'Content-Type'

select_columns = "" 
query = ""
cols = ""

if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response
    
@app.route("/", methods = ["GET", "POST"])
def index():
    global query, select_columns, cols

    print("INSIDE INDEX")

    # if request.method == "GET":
    #     print("INSIDE GET")
    #     print(request.data)
    #     print(str(request))

    #     if query == "" :
    #         return jsonify({"message": "No query found"})

    #     ret = select_where_query(123,select_columns, where_args = query)
    #     output = [{c:v for c,v in zip(cols,val)} for val in ret]
    #     return jsonify(output)

    if request.method == "POST":
        
        print("Request : ")
        print(request)

        print("INSIDE POST")
        data = json.loads(request.data.decode("utf-8"))
        print("DATA : ")
        print(data)
        cols = data['cols']
        select_columns = " ".join(data['cols'])
        query = "?".join(":".join([str(value) for key,value in x.items()]) for x in data['queries'])
        print(select_columns)
        print(query)

        ret = select_where_query(123,select_columns, where_args = query)

        output = [{c:v for c,v in zip(cols,val)} for val in ret]
        for ele in output:
            print(ele)

        return jsonify(output)

@app.route("/stats", methods = ["GET"])
def stats():
    print("INSIDE STATS")

    # Sequential
    # stats = {
    #     "stats1": stats_page1(1),
    #     "stats2": stats_page2(2),
    #     "stats3": stats_page3(3),
    #     "stats4": stats_page4(4),
    #     "stats5": stats_page5(5),
    #     "stats6": stats_page6(6),
    #     "stats7": stats_page7(7)
    # }

    # Multi-threading
    processes = []
    with ThreadPoolExecutor(max_workers = 7) as executor:
        processes.append ( executor.submit(stats_page1, 1) )
        processes.append ( executor.submit(stats_page2, 2) )
        processes.append ( executor.submit(stats_page3, 3) )
        processes.append ( executor.submit(stats_page4, 4) )
        processes.append ( executor.submit(stats_page5, 5) )
        processes.append ( executor.submit(stats_page6, 6) )
        processes.append ( executor.submit(stats_page7, 7) )

    stats = {}
    for i,_ in enumerate(as_completed(processes),start = 1):
        stats["stats"+str(i)] = _.result()

    return jsonify(stats)
        

if __name__ == "__main__":
    app.run(debug = True)