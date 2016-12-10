# IPL DATA ANALYSIS AND PLOTTING THE ANALYSED DATA
2 data sets of the IPL tournament which is played in india every year was downloaded from the below link and using the 2 data sets, data analysis was done and the output can be seen as both a CSV file as well as a graph in PNG format. I have written 5 scripts which perform the analysis and whereas 1 script that divides the obtained dataset into the required format.  

 <https://www.kaggle.com/manasgarg/ipl>


## Online Documentation 

This particular project contains scripts which perform the above described objective. This README contains the steps and the requirements for the execution of the scripts. The output of each file can be seen in the output folder. I have shown for only 1 team. Output can be obtained for any team using the below commands. 


## Requirements for the Script
Choice of Programming : Python.

These scripts can be executed on any bash which has python pre-installed or any UNIX-based operating systems using the below commands. 
Download the 2 data sets from the above link. 


## Steps to Execute

1. Execute collect_data.py. This particular script combines the 2 datasets (matches,deliveries) into 1 file. Creates a folder with the name Seasons and a subfolder with the name combined. Stores the combined dataset as combined.csv inside combined subfolder and then splits the merged data into different seasons, stored the split data into different CSVs inside the Seasons folder. Below is the command line to execute the script.

    python collect_data.py


2. Execute analysis_1.py as follows,
	
    python analysis_1.py --Team your_wish
	

When the above line is executed, the script first creates 1 folder on the desktop named output and a subfolder with the team's name. The script calculates the fall of wickets for each over in all the seasons and plots a histogram showing how many wickets have fallen during each over through all the seasons. The picture below shows a sample of the output. The output PNG can be found in the output and team name subfolder with its corresponding CSV.
Use Quotes to write the team name ("Royal Challengers Bangalore") and use full name of the team with spaces.


![analysis_1](https://cloud.githubusercontent.com/assets/22183540/21072094/363d3116-be85-11e6-9e0d-5ad75fba4972.jpg)




3. Execute analysis_2.py as follows,
	
   python analysis_2.py --Team your_wish

The above command line performs the following function, it first checks if an output folder exsists and if the team name subfolder is present. If not present, it will create respective folders. The script calculates the runs scored by boundaries(4s and 6s), extras and by other means. Plots the percentage of each of these towards the total score at the end of each season. The below image can be seen for better understanding. 

![analysis_2](https://cloud.githubusercontent.com/assets/22183540/21072137/5552a8e6-be86-11e6-8434-e16cedab0f5f.jpg)



5. Execute analysis_3.py as follows,

   python analysis_3.py --number your_wish

The above command line performs the following function, it first checks if an output folder exsists and if the player name subfolder is present. If not present, it will create respective folders. The above script initally calculates the total runs scored by each players over all the season and arranges them according to descending order. Accepts a rank from the user and performs analysis on the player. The output is a PNG with the his contribution of runs towards that of the total teams runs per season. The below graph can be seen for better understanding. Eg : python analysis_3.py --number 1

![analysis_3](https://cloud.githubusercontent.com/assets/22183540/21072176/65fa7c86-be87-11e6-8319-ac7c939412a7.jpg)

6. Execute analysis_4.py as follows,

	python analysis_4.py --Team your_wish --Score your_wish

The above command line performs the following function, it first checks if an output folder exsists and if the team name subfolder is present. If not present, it will create respective folders. The script calculates how many times a particular team has won when they have scored above a particular score and then calculates the win rate in percentage vs each season. Plots it on a Bar graph accordingly. 
Below is a sample output.

![analysis_4](https://cloud.githubusercontent.com/assets/22183540/21072209/84a02586-be88-11e6-9669-223d534834b0.jpg)


7. Execute analysis_5.py as follows,

	python analysis_5.py --Team your_wish

The above command line performs the following function, it first checks if an output folder exsists and if the team name subfolder is present. If not present, it will create respective folders. The script calculates an average runs scored during and after powerplay of all the matches of a particular team for all the seasons and then plots it using point plot to give a fair idea about each of the teams performance in each season. The below graph can be reffered for better understanding,


![analysis_5](https://cloud.githubusercontent.com/assets/22183540/21072230/5cb50d92-be89-11e6-85bf-3dd9ddbd6bc3.jpg)


