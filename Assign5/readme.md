### Roman's Taxi Service

#### Installation

1. Install the necessary packages as specified in `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

2. Follow the [Hadoop installation guide](https://medium.com/@abhikdey06/apache-hadoop-3-3-6-installation-on-ubuntu-22-04-14516bceec85).

3. Switch to the Hadoop user and navigate to the directory containing the Roman's Taxi Service directory:
    ```bash
    su - hadoop
    cd /path/to/RomansTaxiService
    ```

4. Download the dataset from [NYC Taxi TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) and store it in the `taxi` directory inside the Roman's Taxi Service directory.

5. Generate the required dataset using the Python script:
    ```bash
    python pqtocsv_dataset_concat.py
    ```

6. Load the dataset into HDFS using the following commands:
    ```bash
    hdfs dfs -mkdir /user
    hdfs dfs -mkdir /user/hadoop
    hdfs dfs -mkdir /user/hadoop/data
    hdfs dfs -copyFromLocal /path/to/directory/taxi/yellow_tripdata_2023_feb_to_dec_2024_jan_10percent.csv /user/hadoop/data
    start-all.sh
    ```

7. SSH into the localhost:
    ```bash
    ssh localhost
    ```

8. Switch to the Hadoop user:
    ```bash
    su - hadoop
    ```

9. Start running the server using:
    ```bash
    python app.py
    ```

10. Once done using the server, stop Hadoop services:
    ```bash
    stop-all.sh
    ```

#### Client Setup

1. Navigate to the client directory:
    ```bash
    cd /path/to/RomansTaxiService/client
    ```

2. Install required dependencies: 
    ```bash
    npm install
    ```

3. Start the client to access the provided services:
    ```bash
    npm start
    ```

---

This `README.md` provides step-by-step instructions for setting up and running Roman's Taxi Service on both the server and client sides. It includes commands for installing packages, setting up Hadoop, downloading datasets, running the server, and starting the client application. Adjust paths and commands as per your specific setup.
