f = open('QnA.txt')	#Open accompanying txt file and read conents into	[🧑‍💻️]
fullText = f.read()	#the 'fullText' string variable.

cats = []		#A list which will contain lists of the questions grouped by category.
catNames = []		#A seperate list to track corresponding category names.


expected = 0	#The correct answer for each question using 1 to signify a yes response and 2 for a no
answer = 0

runningScore = 0	#How many points the subject has gained, one for each right answer in the given category.
scores = []

j = -1		#Tracks how many categories have been created thus far.


#########################################################################
#				SECTION  1				#
#########################################################################
#For reading in the entirety of the QnA.txt file and dividing it up into 
#seperate categories and questions.
#

for i in range (0, len(fullText)):	#First FOR Loop will make nested arrays containing all categories and questions
	if (fullText[i:(i+5)] == 'CAT: '):	
		catNames.append(fullText[ (i+5) : (fullText.find('\n', (i+5))) ])
		cats.append([])
		
		j += 1
		i += 5		#Should be an easy way for the category markers not to count as ':'s when looking for questions

	elif (fullText[i:(i+2)] == ':\n'):

		cats[j].append( fullText[ (i+2) : fullText.find('\n', (i+3) ) ] )	#(i+3) should be the character just after the linebreak following
											#the ':' meaning it should be the one at the end of the question





#########################################################################
#				SECTION  2				#
#########################################################################
#For displaying the different questions out to the end user and storing 
#point total scores for each completed category.
#

for i in range (0, len(cats)):
	print ('\n========================================')
	print ('\n\nSection ', (i+1), ' :\t', catNames[i], '\n')	#Print the category name at the start of the category
	
	for question in cats[i]:
		expected = int(question[ ( question.find('[')+1 ) : ( question.find('[')+2 ) ])		#Find the marker for the correct answer (1 or 2)
		question = question[  : question.find('[') ]			#Strip the marked answer out of the question before displaying

		
		print ('\n---------------------------\n' + question)
		while (answer != 1 and answer != 2):		#Repeat prompting question until a valid answer is received
			answer = int(input ('Please enter 1 for [YES] or 2 for [NO].' + '\n') )
			
		if (answer == expected): runningScore += 1	#Compare the given answer to the expected answer and add a point if a match is found
		answer = 0	#Reset answer before next question.
	
	scores.append( (runningScore / len(cats[i]))*100 )	#Turn scores into a percentage for that category
	runningScore = 0



#########################################################################
#				SECTION  3				#
#########################################################################
#For displaying out a table of scores as percentages alongside the names
#of their relevant categories.
#
	
print ('\n\n\n-----------------------\n\tSCORES\n-----------------------')
for j in range (0, len(catNames)):
	print(catNames[j], '\t-->  ', round(scores[j] , 1), '%')
	
	print ( round( (scores[j] / 100)*len(cats[j])) , '\t/\t', len(cats[j]))
	if (scores[j] < 40.0): print ('Please advise.')
	print ('\n\n')


print ('_______________________\nTOTAL SCORE :\t', ( round( sum(scores)/len(scores), 1 ) ), '%')




















