def bmi():
	
	try:
		height=input("Enter in your height in feet and inches. Make sure to put comma between feet and inches: ")
		feet,inches=map(int,height.split(","))
		weight=input("Enter in weight: ")
		weight=float(weight)
		
		total_height=(feet * 12) + inches
		calc=round((weight * 703) / (total_height ** 2), 2)
		
		print(total_height)
		
		print(f"What is your BMI: {calc}")
		
		if calc > 25.1:
			prin("You are over BMI")
		
		elif calc < 18.5:
			print("You are under BMI")
			
		else:
			print("Your BMI is normal")
		
	expect ValueError:
		print("Invalid arguments. Please enter in feet and inches")
bmi()