mode = int(input("enter mode number\n "))
#mode in this case is a variable, and input asks for input from a user,
#and can have text before it ("enter mode number") in this case
def grog():
#functions makes callable sets of code, so only parts get executed at 
#once so you can make more dynamic code
	print("hello\"world\"")
#basic print function
#backslashes literally interpret symbol (in all cases , not just print)

def ggog(): 
	fav_mc_blocks = ["brown Bricks","Grass block","glass block","Grass block"]
	todolist = ["cactus farm","Mixed Farm","walls"]
#basic functionless lists
	print(fav_mc_blocks)
	fav_mc_blocks.append(todolist)
#adds 2nd list to first
	print(fav_mc_blocks)
	fav_mc_blocks.append("1")
#directly adding something to the list
	print(fav_mc_blocks)
	fav_mc_blocks.remove("glass block")
#removes a specific element from a list
	print(fav_mc_blocks)
	fav_mc_blocks.pop()
#removes the last added element in a list
	print(fav_mc_blocks)
	print(fav_mc_blocks.index("Grass block"))
#indexes where an element is on a list
	print(fav_mc_blocks.count("Grass block"))
#counts the amount of times something has been listed in a list
	fav_mc_blocks.clear()
	print(fav_mc_blocks)
#removes all emements from a list
	the = [("nonce"),(12,23),(25,50)]
#tuples are lists that cannot be modified and can be put in lists using
#() instead of []
	print(the)

def defining():
	def cube(num):
		return num*num*num
		print("this will never do anything")
	#return function gives back information to whatever calls a the
	#function its in and effectivly ends off a function (any code below
	#wont do anything)
	gabba = cube(18)
	print(gabba)
		
def atlus():
	def max_num(num1,num2,num3):
		if num1 != num2 and num1 >=num3:
                #not equal op    #greater than operator
			return num1
		elif num2 >= num1 and num2 >= num3:
			return num2
		else:
			return num3
	print(max_num(input("num1 "),input("num2 "),input("num3 ")))
	
def calculator_boogloo():
	num1 = int(input("First Number "))
	op = input("Operator ")
	num2 = int(input("Seccond Number "))
	if op == ("*"):
		print(num1 * num2)
	elif op == ("/"):
		print(num1 / num2)
	elif op == ("+"):
		print == (num1 + num2)
	elif op == ("-"):
		print == (num1 - num2)
	else:
		print("Failure")

def living_failure():
	MonthConversions = {
		"jan": "january",
		"feb": "febuary",
		"mar": "march",
		"apr": "april",
		"may": "may",
		"jun": "june",
		"jul": "july",
		"aug": "august",
		"sep": "september",
		"oct": "october",
		"nov": "november",
		"dec": "december",
	}
	print(MonthConversions.get(input("Month Shorthand Extender Input "),print("Invalid!")))

def sanity():
	i = 10
	while i >= 1:
		print(i)
		i -= 1
	print("if i werent insane already i would be now")

def cool():
	S_Word = "knack"
	guess = ""
	guess_count = 3
	while guess != S_Word and guess_count >= 0:
		guess = input("Enter Guess")
		guess_count -= 1
	if guess == S_Word:
		print("Winner!")
	else:
		print("failure!")

def loop_de_swoop():
	troop = ["fred","greg","gorb","fyred","gyreg","gyorb","fdred","ggreg","ggorb","satan"]
	for unit in range(len(troop)):
		print(unit)
	for unit in troop:
		print(unit)

def hardass():
	def power_raising(base_num, pow_num):
		result = 1
		for index in range(pow_num):
			result = result * base_num
		return result
	print(power_raising(int(input("num1 ")), int(input("num2 "))))

def two_dimentional():
	number_grid =[
	[1,2,3],
	[4,5,6],
	[7,8,9],
	[0]
	]
	print(number_grid[1][2])
	print(" ")
	for row in number_grid:
		for col in row:
			print(col)

def gogogg():
	def translation(phrase):
		translation = ""
		for letter in phrase:
			if letter.lower() in "AEIOUaeiou":
				if letter.isupper():
					translation = translation + "G"
				translation = translation + "g"
			else:
				translation = translation + letter
		return translation
	print(translation(input("Enter words ")))

def pizza():
	emp = open("employees.txt")
	print(emp.readlines())
	emp.close()
	ermp = open("employees.txt")
	#seprate name because same causes issues
	for employ in ermp.readlines():
		print(employ)
	ermp.close()

def pasta():
	print("Start")
	fking_emp = open("employees.txt", "a")
	fking_emp.write("\nadded this thru magic!")
	fking_emp.close()

def fixit():
	empl = open("employees.txt", "w")
	empl.write("gregorry\nseff\ngeoff\nnuman\nhuman\ngoo-man (kill)")
	empl.close()

def def_sprawl():
	import other
	print(other.roll_dice(100))

def omeg():
	mobde = int(input("Enter mode number "))
	def mode1 ():
		print("worked")
	def mode2 ():
		num1 = int(input("Number 1 "))
		op = input("Input Operator")
		num2 =int(input("Number 2 "))
		if op == "*":
			print(num1 * num2)
		elif op =="+":
			print(num1 + num2)
		elif op == "/":
			print(num1 / num2)
		elif op == "-":
			print(num1 - num2)
		else:
			print("Invalid!")
	def mode3():
		phonedial =[
		[1,2,3],
		[4,5,6],
		[7,8,9],
		[0]]
		print(phonedial[1][2])



	if mobde == 1:
		mode1()
	elif mode == 2:
		mobde2()
	elif mode == 3:
		mobde3()




	else:
		print("failure!")

def prison():
	from Hell_or_maybe_purgatory import prisoners
	prisoner1 = prisoners("jhonson", 158, "kill", True)
	prisoner2 = prisoners("hhgregg", 1, "jaywalking", False)
	print(prisoner1.time)
	print(prisoner2.reason)
	print(prisoner1.on_bail())
	print(prisoner2.on_bail())

def jailer_und_gaurd():
	from Hell_or_maybe_purgatory import jailer

def quiz():
	from Hell_or_maybe_purgatory import question
	question_prompts = [
		"what colour are peaches?\npink(a)\ngreen(b)\nblue(c)\n\n",
		"what colour is 00ff00?\nred(a)\nblue(b)\ngreen(c)\n\n",
		"what does vtol stand for\nvideo to offsite lamda(a)\nvertical take off and landing(b)\nverge take offlandrover(c)\n\n"
	]
	questions = [
		question(question_prompts[0], "a"),
		question(question_prompts[1], "c"),
		question(question_prompts[2], "b"),
	]
	def testing_initiative(questions):
		score = 0
		for question in questions:
			answer = input(question.prompt)
			if answer == question.answer:
				score += 1
		print("you got " + str(score) + "/" + str(len(questions)) + " correct")
	testing_initiative(questions)



		
if int(mode) == 1:
#if functions check *if* a statement is true then executes if true
	grog() #grog() is calling a variable
	
elif int(mode) == 2:
#elif is similar to if but checks like a list, ex: if theres an umbrella,
#grab that otherwise(elif) grab a jacket, else stay inside
		ggog()

elif mode == 3:
	defining()
elif mode == 4:
	atlus()
elif mode == 5:
	calculator_boogloo()
elif mode == 6:
	living_failure()
elif mode == 7:
	sanity()
elif mode == 8:
	cool()
elif mode == 9:
	loop_de_swoop()
elif mode == 10:
	hardass()
elif mode == 11:
	two_dimentional()
elif mode == 12:
	gogogg()
elif mode == 13:
	pizza()
elif mode == 14:
	pasta()
elif mode == 15:
	fixit()
elif mode == 16:
	def_sprawl()
elif mode == 17:
	omeg()
elif mode == 18:
	prison()
elif mode == 19:
	quiz()



else:
	print("not available! quitting program!")
