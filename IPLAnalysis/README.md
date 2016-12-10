# IPL DATA ANALYSIS AND PLOTTING THE ANALYSED DATA
2 data sets of the IPL tournament which is played in india every year was downloaded from the below link and using the 2 data sets, data analysis was done and the output can be seen as both a CSV file as well as a graph in PNG format. I have written 5 scripts which perform the analysis and whereas 1 script that divides the obtained dataset into the required format.  

 <https://www.kaggle.com/manasgarg/ipl>


## Online Documentation 

This particular project contains scripts which perform the above described objective. This README contains the steps and the requirements for the execution of the scripts. The output of each file can be seen in the output folder. I have shown for only 1 team. Output can be obtained for any team using the below commands. 


## Requirements for the Script
Choice of Programming : Python
These scripts can be executed on any bash which has python pre-installed or any UNIX-based operating systems using the below commands. 
Download the 2 data sets from the above link. 


## Steps to Execute

1. Execute collect_data.py. This particular script combines the 2 datasets (matches,deliveries) into 1 file. Creates a folder with the name Seasons and a subfolder with the name combined. Stores the combined dataset as combined.csv inside combined subfolder and then splits the merged data into different seasons, stored the split data into different CSVs inside the Seasons folder. Below is the command line to execute the script.

	python collect_data.py


2. Execute analysis_1.py as follows,
	
	python analysis_1.py --Team your_wish
	

When the above line is executed, the script first creates 1 folder on the desktop named output and a subfolder with the team's name. The script calculates the fall of wickets for each over in all the seasons and plots a histogram showing how many wickets have fallen during each over through all the seasons. The picture below shows a sample of the output. The output PNG can be found in the output and team name subfolder with its corresponding CSV.
Use Quotes to write the team name ("Royal Challengers Bangalore") and use full name. 



4. Execute analysis_2.py as follows,
	
	python analysis_2.py --Team your_wish

Outputs a CSV containing questions arranged in the reputation of the each user in the data you collected in the 1st/2nd step.

5. Execute analysis_4.py as follows,

	python analysis_4.py --search_term your_wish

Outputs a CSV containing users and the badges they are awarded, percentage of awards they have. 

6. Execute analysis_5.py as follows,

	python analysis_5.py --search_term your_wish

Outputs a CSV containing total number of questions answered by each of the user who questioned and the number of the answers they got right.

7. Execute analysis_6.py as follows,

	python analysis_6.py --search_term your_wish

Outputs a CSV containing the username of the user of the one who answered the particular question and the score they have been awarded for that answer. 
