

# election_results.txt

# Election_Analysis

## Project Overview
The Colorado Board of Elections employee has given me the following tast to complete the election audit 
of a recent congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources

* Data Source: election_results.csv 
* Software: Python 3.9.6, Visual Studio Code, 1.59.1

## Summary 
The analysis of the election show that:

* There were 369,711 votes cast in the election.

* The candidates were:

  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane

* The Candidate Results were:

  - Charles Casper Stockham received 23.0% of the vote 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote 272,892 number of votes.
  - Raymon Anthony Doane received 3.1%  of the vote 11,606 number of votes.
  
* The winner of the election was:
  - Diana DeGette who recieved 73.8% of the vote and 272,892 number of votes.

 

# Election-Audit Results

There were 369,711 votes cast in the election.
The county with largest vote turnout: Denver with 306,055 number of votes. 

## The counties were:

- Jefferson: received 10.5% of vote and 38,855 number of total votes
- Denver:received 82.8% of vote and 306,055 number of votes.
- Arapahoe: received 6.7% of vote and 24,801 number of votes.

## The winner of the election and runner ups:

Based you data provided, total number votes cast were 369,711.
We have a clear winner Diana DeGette who won the election by receiving 272,892 votes, which 73.8% of total ballots.
Where runner up are Charles Casper Stockham with 85,213 votes and 23.0% of total ballots followed by
Raymon Anthony with 11,606 votes and 3.1% of total ballots. 

# Election-Audit Summary

Based you data provided, total number votes cast were 369,711.
We have a clear winner Diana DeGette who won the election by receiving 272,892 votes, which 73.8% of total ballots.
Where runner up are Charles Casper Stockham with 85,213 votes and 23.0% of total ballots followed by 
Raymon Anthony with 11,606 votes and 3.1% of total ballots.

# Business Proposal to the Election Commission

This script can be easily modified to fit any type of election. For example;

1. If you wanted to analysis a federal congressional election, all you need to do is
   modify your code from county to state wise elections.
        ~ county_list = []
	      ~ county_votes = {}
 - Replace wherever you have "county" with "state" and
   it can used for state election or any other elections. 



2. We can also modify our code to retrieve the data we are required
   instead of getting entire the consolidated data.
   We can use imput() method to access information needed.
    
    ~ use input() method 
	- for county name, candidates name or just winner details


3. We can also modify the code that candidate will list accounding to their ranking
   in terms of total number of votes they recieved.
	

	~ Initialize a dictionary with "keys" as the names of candidates....
	~ Store the total votes for each candidates as the "values" of the corresponding keys
	~ Sort the dictionary by values in descending order
	
