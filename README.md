A large group of friends from the town of Nocillis visit the vineyards of Apan to taste wines. The vineyards produce many fine wines and the friends decide to buy as many as 3 bottles of wine each if they are available to purchase. Unfortunately, the vineyards of Apan have a peculiar restriction that they can not sell more than one bottle of the same wine. So the vineyards come up with the following scheme: They ask each person to write down a list of up to 10 wines that they enjoyed and would be happy buying. With this information, please help the vineyards maximize the number of wines that they can sell to the group of friends.

Input A two-column TSV file with the first column containing the ID (just a string) of a person and the second column the ID of the wine that they like. Here are three input data sets of increasing sizes. Please send us solutions even if it runs only on the first file.
https://s3.amazonaws.com/br-user/puzzles/person_wine_3.txt 
https://s3.amazonaws.com/br-user/puzzles/person_wine_4.txt.zip 
https://s3.amazonaws.com/br-user/puzzles/person_wine_5.txt.zip


SOLUTION:
	The code breakdown

	step 1: list of all bottles and count, list of people and the wine wish list, each bottle list with how many people wating

	step 2: bottle with count 1 is directly supplied to the person wanting and his final list is started creating

	step 3: bottle with highest count
		step a: check for the people wanting it
		step b: check if their list has atleast 3 unique bottles
		step c: if not add the bottle to person, delete the bottle from list and update the final list

	step 4: check person with maximum of 4 bottles and remove from list