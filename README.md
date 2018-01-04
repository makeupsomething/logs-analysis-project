# The third project for the FSND by Udacity

## About
This script will query a database for the answers to 3 questions:
1. What are the most popular three articles of all time?

2. Who are the most popular article authors of all time?

3. On which days did more than 1% of requests lead to errors?

It is written in legacy Python (Python 2.7). 

## To Run

### You will need:
- Python2.7
- Vagrant
- VirtualBox

### Setup
1. Install Vagrant And VirtualBox
2. Download and setup the database
3. Clone this repository

### To Run

Launch Vagrant VM by running `vagrant up`, you can the log in with `vagrant ssh`

Download the data and place it in a folder that can be accessed by vagrant. The data can be downloaded from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

To load the data, use the command 
```
psql -d news -f newsdata.sql
```

To run the script use the following command:
```
python script.py
```

The answers will be displayed as plain text, the answers can also be found in `output.txt`
