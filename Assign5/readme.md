### Roman's Taxi Service

Install the necessary packages as specified in 'requirements.txt'

For the server (let hadoop be the user that is going to develop the DFS) :

Use 'https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html' for hadoop installation

1) Use `su - hadoop` and login to that user
2) Go the directory containing the Roman's Taxi Service directory using `cd`
3) Download the dataset from 'https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page' and store it in the directory `taxi` inside the root directory
4) Use `python pqtocsv_dataset_concat.py` to generate the required dataset
5) To load the dataset into HDFS use the following set of commands
   1) `hdfs dfs -mkdir /user`
   2) `hdfs dfs -mkdir /user/hadoop`
   3) `hdfs dfs -mkdir /user/hadoop/data`
   4) `hdfs dfs -copyFromLocal <path-to-directory></path-to-directory>/taxi/yellow_tripdata_2023_feb_to_dec_2024_jan_10percent.csv /user/hadoop/data`
   5) `start-all.sh`
6) Start running the server using `python app.py`


For the client :

1) Go to the directory containing the Roman's Taxi Service directory and use `cd client`
2) First do `npm install` and finally `npm start` to access the provided services






