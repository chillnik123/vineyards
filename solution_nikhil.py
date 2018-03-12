import os

input_filename = "person_wine_4.txt"
textfile = open(input_filename, 'r')
winelist = {}
personlist = {}
wine_interest_person_list = {}
persons_final_list = {}

for line in textfile:
	(person,wine) = line.split()
	person = person.replace("person","")
	wine = wine.replace("wine","")
	if wine in winelist:
		winelist[wine] = winelist[wine]+1
	else:
		winelist[wine] = 1
	
	if person in personlist:
		personlist[person].append(wine)
	else:
		personlist[person] = [wine]

	if wine in wine_interest_person_list:
		wine_interest_person_list[wine].append(person)
	else:
		wine_interest_person_list[wine] = [person]
textfile.close()

'''
/*if condition
/* unique wine count and assign it to the person
/* update the final list
/* remove the wine bottle from wine list
/* reduce the count
'''

'''
/* else condtion
/* condition to check when the same bottle is desired by more then 1 person
/* checking if he has any 3 unique bottles
/* checking for the final list
/* assigning the bottles accordingly
'''

def assignWine():
	update = True
	while update:
		update = False
		for wine in list(winelist):
			if winelist[wine] == 1:
				person = wine_interest_person_list[wine][0]
				if person in personlist:
					if person in persons_final_list:
						persons_final_list[person].append(wine)
					else:
						persons_final_list[person] = [wine]
					personlist[person].remove(wine)
					if len(persons_final_list[person]) == 3:
						update = True
						for update_wine in personlist[person]:
							winelist[update_wine] = winelist[update_wine] - 1
							wine_interest_person_list[update_wine].remove(person)
						personlist.pop(person)
				winelist.pop(wine)
			else:
				w_intrest = wine_interest_person_list[wine]
				for prsn in w_intrest:
					unique_wine = []

					if prsn in persons_final_list and len(persons_final_list[prsn]) == 3:
						continue

					if prsn in persons_final_list:
						unique_wine.append(len(persons_final_list[prsn]))
					try:
						for n_wine in personlist[prsn]:
							if winelist[n_wine] == 1:
								unique_wine.append(1)
						if sum(unique_wine)<3 and winelist[n_wine] != 1 and winelist[n_wine] > 0:
							if prsn in persons_final_list:
								persons_final_list[prsn].append(n_wine)
							else:
								persons_final_list[prsn] = [n_wine]
							personlist[prsn].remove(n_wine)
							winelist[n_wine] = 0
						else:
							continue
					except:
						print("error occured")


'''
/* reading the persons_final_list and writing in a file
'''

def outputResult():
	input_file_tagname = os.path.splitext(os.path.basename(input_filename))[0]
	output_filename = input_file_tagname+"_output.txt"
	textfile = open(output_filename, 'w')
	for person in persons_final_list:
		for winenumber in persons_final_list[person]:
			textfile.write("person"+person+"\t"+"wine"+winenumber+"\n")
	textfile.close()

assignWine()
outputResult()
