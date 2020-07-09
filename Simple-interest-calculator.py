principle = int(input("Enter the principle amount: "))
rate = int(input("Enter interest %: "))
time = (float(input("Enter years/months/days: ")))
Total = principle * rate / 100 * time
print("You will get interest: " + str(Total) + " \n for the principle amount: " + str(principle) +" for " + str(time)+ " years")
