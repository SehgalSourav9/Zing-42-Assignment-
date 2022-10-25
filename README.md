# Assignment for Zing 42 Technologies
Following tasks were to be implemented in this Assignment:

**Acquire Data**:

1. Programatically fetch “Securities available for Equity segment (.csv)” file From the URL: https://www.nseindia.com/market-data/securities-available-for-trading
2. Programatically get the latest “bhavcopy” csv file from the following URL - https://www.nseindia.com/all-reports
3. Construct a (relational) database with normalized tables & insert both the data files into it
4. In addition to step 2, programmatically get bhavcopies of the last 30 days instead of just the latest one.

**Query**:

1. Write a SQL query to fetch the top 25 gainers of the day sorted in the order of their gains. Gains is defined as [(close - open) / open] for the day concerned as per point 2 above.
2. Get datewise top 25 gainers for last 30 days as per point 4 above.
3. Alternatively, you can also get a single list of top 25 gainers based on open of oldest day and close of latest day of those 30 days as per point 4.

# Required Python Libraries
1. Pandas
2. Os
3. Datetime
4. Zipfile
5. Requests
6. Pandas.io
7. Sqlalchemy

# How to run the assignment
```bash
    python main.py
 ```
