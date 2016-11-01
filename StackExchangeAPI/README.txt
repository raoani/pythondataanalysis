# StackExchangeAPI Plus 5 Analysis

This script accepts a particular search term, requests the stackoverflow for the questions related to the search term depending on the activity and returns a Json file
using which 5 other scripts are written so as to perform certain analysis on the collected data.

 <https://api.stackexchange.com/docs>


## Online Documentation 

This particular project contains scripts which perform the above described objective. This README contains the steps and the requirements for the execution of the scripts.


## Requirements for the Script

This script can be executed on any Unix based OS using command line inputs. Generate a secret key of your own in (http://stackapps.com/questions/3055/is-there-a-limit-of-api-requests).


## Steps to Execute

1. Execute exam.py to obtain data for questions about the term of your choice
	
	python exam.py --search_term your_wish 

2. Execute exam.py and " " to search for multiple tags. Use semi-colon as the seperator. 

3. Execute analysis_1.py as follows,
	
	python analysis_1.py --search_term your_wish

Outputs a CSV which contains top 3 questions according to their badge counts and outputs top 3 questions.

4. Execute analysis_2.py as follows,
	
	python analysis_2.py --search_term your_wish

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