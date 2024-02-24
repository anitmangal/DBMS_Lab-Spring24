import psycopg2
from tabulate import tabulate

# Connect to the database with the appropriate credentials
conn = psycopg2.connect(host="localhost", database="21CS10005", user="21CS10005", password="21CS10005")

# Use a cursor for the connection object 
with conn.cursor() as cur:
	# Program Loop
    while True:
        qnum = int(input("\n\nEnter the query number (0 to exit): "))		# Input for the query number
        print()
        # For each query:
        #	print the query in english.
        #	use the execute() function for the cursor to run the query, which was already used in assignment-2
        #	use the fetchall() function to get all the result records of the query and store in "data" object.
        #	print the results in proper format using tabulate() function
        if qnum == 0:
            break
        elif qnum == 1:
            print("Query1: Roll number and name of all the students who are managing the \"Megaevent\"")
            print()
            cur.execute("SELECT STUDENT.Roll, STUDENT.Name FROM STUDENT JOIN MANAGE ON STUDENT.Roll = MANAGE.Roll JOIN EVENT ON EVENT.EID = MANAGE.EID WHERE EVENT.EName = 'Megaevent';")
            data = cur.fetchall();
            print(tabulate(data, headers=["Roll", "Name"]))
        elif qnum == 2:
            print("Query2: Roll number and name of all the students who are managing \"Megevent\" as a \"Secretary\"")
            print()
            cur.execute("SELECT STUDENT.Roll, STUDENT.Name FROM STUDENT JOIN MANAGE ON STUDENT.Roll = MANAGE.Roll JOIN EVENT ON EVENT.EID = MANAGE.EID JOIN ROLE ON ROLE.RID = STUDENT.RID WHERE EVENT.EName = 'Megaevent' AND ROLE.RName = 'Secretary';")
            data = cur.fetchall();
            print(tabulate(data, headers=["Roll", "Name"]))
        elif qnum == 3:
            print("Query3: Name of all the participants from the college \"IITB\" in \"Megaevent\"")
            print()
            cur.execute("SELECT PARTICIPANT.Name FROM PARTICIPANT JOIN EVENT_PART ON PARTICIPANT.PID = EVENT_PART.PID JOIN EVENT ON EVENT.EID = EVENT_PART.EID WHERE EVENT.EName = 'Megaevent' AND PARTICIPANT.College_Name = 'IITB';")
            data = cur.fetchall();
            print(tabulate(data, headers=["Name"]))
        elif qnum == 4:
            print("Query4: Name of all the colleges who have at least one participant in \"Megaevent\"")
            print()
            cur.execute("SELECT DISTINCT PARTICIPANT.College_Name FROM PARTICIPANT JOIN EVENT_PART ON PARTICIPANT.PID = EVENT_PART.PID JOIN EVENT ON EVENT.EID = EVENT_PART.EID WHERE EVENT.EName = 'Megaevent';")
            data = cur.fetchall();
            print(tabulate(data, headers=["College Name"]))
        elif qnum == 5:
            print("Query5: Name of all the events which are managed by a \"Secretary\"")
            print()
            cur.execute("SELECT DISTINCT EVENT.EName FROM EVENT JOIN MANAGE ON EVENT.EID = MANAGE.EID JOIN STUDENT ON STUDENT.Roll=MANAGE.Roll JOIN ROLE ON ROLE.RID = STUDENT.RID WHERE ROLE.RName = 'Secretary';")
            data = cur.fetchall();
            print(tabulate(data, headers=["Event Name"]))
        elif qnum == 6:
            print("Query6: Name of all the \"CSE\" department student volunteers of \"Megaevent\"")
            print()
            cur.execute("SELECT STUDENT.Name FROM STUDENT JOIN VOLUNTEER ON STUDENT.Roll=VOLUNTEER.Roll JOIN EVENT_VOL ON EVENT_VOL.Vol_Roll = VOLUNTEER.Roll JOIN EVENT ON EVENT.EID = EVENT_VOL.EID WHERE STUDENT.Dept = 'CSE' AND EVENT.EName = 'Megaevent';")
            data = cur.fetchall();
            print(tabulate(data, headers=["Name"]))
        elif qnum == 7:
            print("Query7: Name of all the events which have at least one volunteer from \"CSE\"")
            print()
            cur.execute("SELECT DISTINCT EVENT.EName FROM EVENT JOIN EVENT_VOL ON EVENT.EID=EVENT_VOL.EID JOIN VOLUNTEER ON EVENT_VOL.Vol_Roll=VOLUNTEER.Roll JOIN STUDENT ON STUDENT.Roll=VOLUNTEER.Roll WHERE STUDENT.Dept = 'CSE';")
            data = cur.fetchall();
            print(tabulate(data, headers=["Event Name"]))
        elif qnum == 8:
            print("Query8: Name of the college with the largest number of participants in \"Megaevent\"")
            print()
            cur.execute("SELECT PARTICIPANT.College_Name FROM PARTICIPANT JOIN EVENT_PART ON EVENT_PART.PID=PARTICIPANT.PID JOIN EVENT ON EVENT.EID=EVENT_PART.EID WHERE EVENT.EName='Megaevent' GROUP BY PARTICIPANT.College_Name ORDER BY COUNT(PARTICIPANT.PID) DESC LIMIT 1;")
            data = cur.fetchall();
            print(tabulate(data, headers=["College Name"]))
        elif qnum == 9:
            print("Query9: Name of the college with largest number of participant overall")
            print()
            cur.execute("SELECT College_Name From PARTICIPANT GROUP BY College_Name ORDER BY COUNT(PID) DESC LIMIT 1;")
            data = cur.fetchall();
            print(tabulate(data, headers=["College Name"]))
        elif qnum == 10:
            print("Query10:Name of the department with the largest number of volunteers in all the events which has at least one participant from \"IITB\"")
            print()
            cur.execute("SELECT STUDENT.Dept FROM STUDENT JOIN VOLUNTEER ON STUDENT.Roll=VOLUNTEER.Roll JOIN EVENT_VOL ON EVENT_Vol.Vol_Roll=VOLUNTEER.Roll JOIN EVENT_PART ON EVENT_PART.EID=EVENT_VOL.EID JOIN PARTICIPANT ON PARTICIPANT.PID=EVENT_PART.PID WHERE PARTICIPANT.College_Name = 'IITB' GROUP BY STUDENT.Dept ORDER BY COUNT(DISTINCT VOLUNTEER.Roll) DESC LIMIT 1;")
            data = cur.fetchall();
            print(tabulate(data, headers=["Department"]))
        elif qnum == 11:
            eventname = input("Enter the event name: ")		# Get the name of the event from user
            cur.execute("SELECT STUDENT.Roll, STUDENT.Name FROM STUDENT JOIN MANAGE ON STUDENT.Roll = MANAGE.Roll JOIN EVENT ON EVENT.EID = MANAGE.EID WHERE EVENT.EName = %s;", (eventname,))		# Use %s to enter variable values into the query
            data = cur.fetchall();
            print("Query11: Roll number and name of all the students who are managing the " + eventname)
            print()
            print(tabulate(data, headers=["Roll", "Name"]))
        else:
            print("Invalid query number")

conn.close()
