## See Owen Notes section at below

# auction-test
This is to test the ability of solving problems in python. 

## The Task
You have been given auction data to process. Your program has to ingest the data and work out which account 
IDs win each auction and log them. The data is not in sequence meaning that you will get recieve the bids in random time order. There are some corrupt bid enteries which need to be filtered out and logged.

## Structure
The project takes the following structure:

```
├── README.md
├── src
│   ├── __init__.py
│   ├── data
│   │   ├── __init__.py
│   │   ├── bid.py
│   │   └── data.csv
│   └── main.py
```

The data handler is housed in the ```__init__.py``` file in the data directory. It loads the data from the 
CSV as soon as it's initialized. Use the ```.data``` property from the data handler to receive bid 
objects to process. You are free to add your own modules in the ```src``` directory and use them as you wish. The program should work by running the ```main.py``` file.  

## Restrictions 
Technically there's nothing stopping you from loading the CSV into pandas and performing data science 
methods to calculate the winner for each auction. However, it's important to demonstrate your problem 
solving skills when developing a system. Your program is supposed to handle the data as it comes in.


###################################### Owen Notes ########################################

## Time taken (breakdown)
Took longer than I should have, have to admit

* Wed Eve - looked at question and explored data ~ 1 hour
* Wed Eve - began drafting plan on paper and in notes, then started code ~ 2 hours
* Thurs Morn - Finishing features ~ 1 hour

** Additional Time **
* Thurs Morn - approx 1 hour - trying to fix input bugs and tie in new bid handling

## Dependencies
1. pandas
2. logging

## Run conditions
1. Just run main.py file and then enter values on input when prompted
2. inspect log files in log directory
3. will have to manually clear out logs between each auction round

## To Do:

1. Add thorough testing to new bid functionality, ran out of time
2. Have separated log directories for each round of auctions
3. fix logging to log all events - fixed 

## Planning Notes

1. Create auction class for storing highest bid state
2. Create auctioneer class for processing bids, seperating into auctions and determining winner
3. Create logging class to log seperate log file for each auction
4. 

* Time param is red herring, should not have any impact on highest bid when compared
* Error handling - negative prices must be filtered from results