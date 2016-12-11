# **Table of Contents** 

- [IPL](#)
- [IPL DATA ANALYSIS AND PLOTTING THE ANALYSED DATA](#)
	- [Online Documentation](.#online-documentation)
	- [Requirements for the Script](.#requirements-for-the-script)
- [Data Extraction](.#data-extraction)
- [Steps to Execute](.#steps-to-execute)
	- [Analysis 1](.#analysis-1)
		- [How many wickets have fallen in each over through all the seasons for a particular team?](.#how-many-wickets-have-fallen-in-each-over-through-all-the-seasons-for-a-particular-team)
	- [Analysis 2](.#analysis-2)
		- [What percentage of runs scored by a team have come from boundaries(4s and 6s seperately), extras and by other ways for each season?](.#what-percentage-of-runs-scored-by-a-team-have-come-from-boundaries4s-and-6s-seperately-extras-and-by-other-ways-for-each-season)
	- [Analysis 3](.#analysis-3)
		- [Arrange the Batsmen according to their rank based on the total runs scored in all seasons. What is their contribution to the total runs scored by their team in each season?](.#arrange-the-batsmen-according-to-their-rank-based-on-the-total-runs-scored-in-all-seasons-what-is-their-contribution-to-the-total-runs-scored-by-their-team-in-each-season)
	- [Analysis 4](.#analysis-4)
		- [Calculate the WINRATE in percentage of a particular team in all seasons when they have scored above a certain score?](.#calculate-the-winrate-in-percentage-of-a-particular-team-in-all-seasons-when-they-have-scored-above-a-certain-score)
	- [Analysis 5](.#analysis-5)
		- [For a particular team, what is the average runs scored during and after powerplay in each season?](.#for-a-particular-team-what-is-the-average-runs-scored-during-and-after-powerplay-in-each-season)


# IPL 

![IPL](<https://cricfrog.com/wp-content/uploads/2016/01/Indian-Premier-League-IPL-Today-Match-Prediction.jpg>)


# IPL DATA ANALYSIS AND PLOTTING THE ANALYSED DATA
2 data sets of the IPL tournament which is played in india every year was downloaded from the below link and using the 2 data sets, data analysis was done and the output can be seen as both a CSV file as well as a graph in PNG format. I have written 5 scripts which perform the analysis and whereas 1 script that divides the obtained dataset into the required format.  

[Kaggle IPL dataset] (<https://www.kaggle.com/manasgarg/ipl>)


## Online Documentation 

This particular project contains scripts which perform the above described objective. This README contains the steps and the requirements for the execution of the scripts. The output of each file can be seen in the output folder. I have shown for only 1 team. Output can be obtained for any team using the below commands. 


## Requirements for the Script
Choice of Programming : Python.

These scripts can be executed on any bash which has python pre-installed or any UNIX-based operating systems using the below commands. 
Download the 2 data sets from the above link. 



# Data Extraction

Execute collect_data.py. This particular script combines the 2 datasets (matches,deliveries) into 1 file. Creates a folder with the name Seasons and a subfolder with the name combined. Stores the combined dataset as combined.csv inside combined subfolder and then splits the merged data into different seasons, stored the split data into different CSVs inside the Seasons folder. Below is the command line to execute the script.

    python collect_data.py
 
 Link to program : [collect_data.py](<https://github.com/raoani/pythondataanalysis/blob/master/IPLAnalysis/PythonAnalysis/InitialStep.ipynb>)
 
 matches.csv
 
 id  |  season  |  city        |  date       |  team1                  |  team2                        |  toss_winner                  |  toss_decision  |  result  |  dl_applied  |  winner                 |  win_by_runs  |  win_by_wickets  |  player_of_match  |  venue                                       |  umpire1    |  umpire2         |  umpire3
----|----------|--------------|-------------|-------------------------|-------------------------------|-------------------------------|-----------------|----------|--------------|-------------------------|---------------|------------------|-------------------|----------------------------------------------|-------------|------------------|---------
1   |  2008    |  Bangalore   |  4/18/2008  |  Kolkata Knight Riders  |  Royal Challengers Bangalore  |  Royal Challengers Bangalore  |  field          |  normal  |  0           |  Kolkata Knight Riders  |  140          |  0               |  BB McCullum      |  M Chinnaswamy Stadium                       |  Asad Rauf  |  RE Koertzen     |
2   |  2008    |  Chandigarh  |  4/19/2008  |  Chennai Super Kings    |  Kings XI Punjab              |  Chennai Super Kings          |  bat            |  normal  |  0           |  Chennai Super Kings    |  33           |  0               |  MEK Hussey       |  Punjab Cricket Association Stadium, Mohali  |  MR Benson  |  SL Shastri      |
3   |  2008    |  Delhi       |  4/19/2008  |  Rajasthan Royals       |  Delhi Daredevils             |  Rajasthan Royals             |  bat            |  normal  |  0           |  Delhi Daredevils       |  0            |  9               |  MF Maharoof      |  Feroz Shah Kotla                            |  Aleem Dar  |  GA Pratapkumar  |
 
 
 Link : [matches.csv] (<https://github.com/raoani/pythondataanalysis/blob/master/IPLAnalysis/matches.csv>)
 
 
 deliveries.csv (Preview)
 
 match_id  |  inning  |  batting_team           |  bowling_team                 |  over  |  ball  |  batsman      |  non_striker  |  bowler   |  is_super_over  |  wide_runs  |  bye_runs  |  legbye_runs  |  noball_runs  |  penalty_runs  |  batsman_runs  |  extra_runs  |  total_runs  |  player_dismissed  |  dismissal_kind  |  fielder
----------|----------|-------------------------|-------------------------------|--------|--------|---------------|---------------|-----------|-----------------|-------------|------------|---------------|---------------|----------------|----------------|--------------|--------------|--------------------|------------------|---------
1         |  1       |  Kolkata Knight Riders  |  Royal Challengers Bangalore  |  1     |  1     |  SC Ganguly   |  BB McCullum  |  P Kumar  |  0              |  0          |  0         |  1            |  0            |  0             |  0             |  1           |  1           |                    |                  |
1         |  1       |  Kolkata Knight Riders  |  Royal Challengers Bangalore  |  1     |  2     |  BB McCullum  |  SC Ganguly   |  P Kumar  |  0              |  0          |  0         |  0            |  0            |  0             |  0             |  0           |  0           |                    |                  |
1         |  1       |  Kolkata Knight Riders  |  Royal Challengers Bangalore  |  1     |  3     |  BB McCullum  |  SC Ganguly   |  P Kumar  |  0              |  1          |  0         |  0            |  0            |  0             |  0             |  1           |  1           |                    |                  |
 
 
 
 Link : [deliveries.csv] (<https://github.com/raoani/pythondataanalysis/blob/master/IPLAnalysis/deliveries.csv>)
 
 
 season_x.csv
 
 season  |  match_id  |  season  |  city       |  date       |  team1           |  team2                |  toss_winner          |  toss_decision  |  result  |  dl_applied  |  winner          |  win_by_runs  |  win_by_wickets  |  player_of_match  |  venue     |  umpire1      |  umpire2      |  umpire3  |  inning  |  batting_team    |  bowling_team         |  over  |  ball  |  batsman        |  non_striker    |  bowler   |  is_super_over  |  wide_runs  |  bye_runs  |  legbye_runs  |  noball_runs  |  penalty_runs  |  batsman_runs  |  extra_runs  |  total_runs  |  player_dismissed  |  dismissal_kind  |  fielder
--------|------------|----------|-------------|-------------|------------------|-----------------------|-----------------------|-----------------|----------|--------------|------------------|---------------|------------------|-------------------|------------|---------------|---------------|-----------|----------|------------------|-----------------------|--------|--------|-----------------|-----------------|-----------|-----------------|-------------|------------|---------------|---------------|----------------|----------------|--------------|--------------|--------------------|------------------|---------
2009    |  59        |  2009    |  Cape Town  |  4/18/2009  |  Mumbai Indians  |  Chennai Super Kings  |  Chennai Super Kings  |  field          |  normal  |  0           |  Mumbai Indians  |  19           |  0               |  SR Tendulkar     |  Newlands  |  BR Doctrove  |  K Hariharan  |           |  1       |  Mumbai Indians  |  Chennai Super Kings  |  1     |  1     |  ST Jayasuriya  |  SR Tendulkar   |  MS Gony  |  0              |  0          |  0         |  0            |  0            |  0             |  1             |  0           |  1           |                    |                  |
2009    |  59        |  2009    |  Cape Town  |  4/18/2009  |  Mumbai Indians  |  Chennai Super Kings  |  Chennai Super Kings  |  field          |  normal  |  0           |  Mumbai Indians  |  19           |  0               |  SR Tendulkar     |  Newlands  |  BR Doctrove  |  K Hariharan  |           |  1       |  Mumbai Indians  |  Chennai Super Kings  |  1     |  2     |  SR Tendulkar   |  ST Jayasuriya  |  MS Gony  |  0              |  0          |  0         |  0            |  0            |  0             |  0             |  0           |  0           |                    |                  |
2009    |  59        |  2009    |  Cape Town  |  4/18/2009  |  Mumbai Indians  |  Chennai Super Kings  |  Chennai Super Kings  |  field          |  normal  |  0           |  Mumbai Indians  |  19           |  0               |  SR Tendulkar     |  Newlands  |  BR Doctrove  |  K Hariharan  |           |  1       |  Mumbai Indians  |  Chennai Super Kings  |  1     |  3     |  SR Tendulkar   |  ST Jayasuriya  |  MS Gony  |  0              |  0          |  0         |  0            |  0            |  0             |  0             |  0           |  0           |
 
 
 Link : [season_1.csv] (<https://github.com/raoani/pythondataanalysis/blob/master/IPLAnalysis/Seasons/season_1.csv>)
 
 
# Steps to Execute

## Analysis 1
 
### How many wickets have fallen in each over through all the seasons for a particular team?

	Execute analysis_1.py as follows,
	
	python analysis_1.py --Team your_wish

Link to code : [analysis_1] (<https://github.com/raoani/pythondataanalysis/blob/master/IPLAnalysis/PythonAnalysis/analysis_1.ipynb>)

Link to .csv : [analysis_1.csv] ( <https://github.com/raoani/pythondataanalysis/blob/master/IPLAnalysis/Output/Royal%20Challengers%20Bangalore/analysis_1.csv>)



When the above line is executed, the script first creates 1 folder on the desktop named output and a subfolder with the team's name. The script calculates the fall of wickets for each over in all the seasons and plots a histogram showing how many wickets have fallen during each over through all the seasons. The picture below shows a sample of the output. The output PNG can be found in the output and team name subfolder with its corresponding CSV.
Use Quotes to write the team name ("Royal Challengers Bangalore") and use full name of the team with spaces.


![analysis_1](https://github.com/raoani/pythondataanalysis/blob/master/IPLAnalysis/Output/Royal%20Challengers%20Bangalore/analysis_1.jpg)




## Analysis 2

### What percentage of runs scored by a team have come from boundaries(4s and 6s seperately), extras and by other ways for each season?
   
	Execute analysis_2.py as follows,
	
	python analysis_2.py --Team your_wish
   
Link to code : [analysis_2] (<https://github.com/raoani/pythondataanalysis/blob/master/IPLAnalysis/PythonAnalysis/analysis_2.ipynb>)
 
Link to .csv : [analysis_2.csv] (<https://github.com/raoani/pythondataanalysis/blob/master/IPLAnalysis/Output/Royal%20Challengers%20Bangalore/analysis_2.csv>)

The above command line performs the following function, it first checks if an output folder exsists and if the team name subfolder is present. If not present, it will create respective folders. The script calculates the runs scored by boundaries(4s and 6s), extras and by other means. Plots the percentage of each of these towards the total score at the end of each season. The below image can be seen for better understanding. 


![analysis_2](https://github.com/raoani/pythondataanalysis/blob/master/IPLAnalysis/Output/Royal%20Challengers%20Bangalore/analysis_2.jpg)


## Analysis 3
 
### Arrange the Batsmen according to their rank based on the total runs scored in all seasons. What is their contribution to the total runs scored by their team in each season?

 	Execute analysis_3.py as follows,

	python analysis_3.py --number your_wish
   
Link to csv : [analysis_3.csv] (<https://github.com/raoani/pythondataanalysis/blob/master/IPLAnalysis/Output/V%20Kohli/analysis_3.csv>)
 
Link to code : [analysis_3] (<https://github.com/raoani/pythondataanalysis/blob/master/IPLAnalysis/PythonAnalysis/analysis_3.ipynb>)

The above command line performs the following function, it first checks if an output folder exsists and if the player name subfolder is present. If not present, it will create respective folders. The above script initally calculates the total runs scored by each players over all the season and arranges them according to descending order. Accepts a rank from the user and performs analysis on the player. The output is a PNG with the his contribution of runs towards that of the total teams runs per season. The below graph can be seen for better understanding. Eg : python analysis_3.py --number 1

![analysis_3](https://github.com/raoani/pythondataanalysis/blob/master/IPLAnalysis/Output/V%20Kohli/analysis_3.jpg)

## Analysis 4

### Calculate the WINRATE in percentage of a particular team in all seasons when they have scored above a certain score?
	
	Execute analysis_4.py as follows,

	python analysis_4.py --Team your_wish --Score your_wish
	
Link to Csv : [analysis_4] (<https://github.com/raoani/pythondataanalysis/blob/master/IPLAnalysis/Output/Royal%20Challengers%20Bangalore/analysis_4.csv>)

Link to code : [analysis_4.csv] (<https://github.com/raoani/pythondataanalysis/blob/master/IPLAnalysis/PythonAnalysis/analysis_4.ipynb>)

The above command line performs the following function, it first checks if an output folder exsists and if the team name subfolder is present. If not present, it will create respective folders. The script calculates how many times a particular team has won when they have scored above a particular score and then calculates the win rate in percentage vs each season. Plots it on a Bar graph accordingly. 
Below is a sample output.

![analysis_4](https://github.com/raoani/pythondataanalysis/blob/master/IPLAnalysis/Output/Royal%20Challengers%20Bangalore/analysis_4.jpg)


## Analysis 5 

### For a particular team, what is the average runs scored during and after powerplay in each season?

	Execute analysis_5.py as follows,

	python analysis_5.py --Team your_wish

Link to csv : [analysis_5.csv]
(<https://github.com/raoani/pythondataanalysis/blob/master/IPLAnalysis/Output/Royal%20Challengers%20Bangalore/analysis_5.csv>)

Link to code : [analysis_5]
(<https://github.com/raoani/pythondataanalysis/blob/master/IPLAnalysis/PythonAnalysis/analysis_5.ipynb>)



The above command line performs the following function, it first checks if an output folder exsists and if the team name subfolder is present. If not present, it will create respective folders. The script calculates an average runs scored during and after powerplay of all the matches of a particular team for all the seasons and then plots it using point plot to give a fair idea about each of the teams performance in each season. The below graph can be reffered for better understanding,


![analysis_5](https://github.com/raoani/pythondataanalysis/blob/master/IPLAnalysis/Output/Royal%20Challengers%20Bangalore/analysis_5.jpg)


