from datetime import date
today=date.today() #provides today's date
print(today)
print("Welcome to the Python Adventure Park.")
print("\n Here are the admission ticket prices:")
print("\n\tAdult........£20")
print("\tChild........£12")
print("\tSenior.......£11")
print("\n")


#The while loop will validate the user input which
#must be a number value. If not, then the message
#to input a numeric value will be continuously displayed
  
adultnum=input("Please enter no. of adult tickets required ")
while adultnum.isnumeric() == False:
    
       print("WRONG TYPE OF VALUE!")
       adultnum=input("Please input a numeric values")

adultnum=eval(adultnum)        
print(adultnum)

childnum=input("Please enter no. of child tickets required ")
while childnum.isnumeric() == False:
    
       print("WRONG TYPE OF VALUE!")
       childnum=input("Please input a numeric value ")
childnum=eval(childnum)        
print(childnum)

seniornum=input("Please enter no. of senior tickets required ")
while seniornum.isnumeric() == False:
    
       print("WRONG TYPE OF VALUE!")
       seniornum=input("Please input a numeric value ")
seniornum=eval(seniornum)        
print(seniornum)

leadbooker=input("Please input the surname of the lead booker ")

def printpass():
   print("Here is your parking pass")
   print("*********************")
   
   print("* FREE PARKING PASS *")
   print(f"* Date: {today}  *")
   print("*********************")

parkingpass= input("Do you require parking (y/n)?")
if(parkingpass=="y" or parkingpass=="Y"):
   printpass()

elif(parkingpass=="n" or parkingpass=="N"):
   print("You have chosen not to select a parking pass") 
else:
   while parkingpass.lower() != "y" and parkingpass.lower() !="n":
        parkingpass=input("You must enter y or n")
        if (parkingpass.lower() == "y"):
           printpass()
def getdate():
   print(date())


def calcTicketCost():
   
   tot= adultnum*20+childnum*12+seniornum*11
   print(f"The total cost of your tickets is: £{tot}")

calcTicketCost()

def printTicket():
   d2 = today.strftime("%B %d, %Y")#put the date in a nicer format
   print("*******************************")
   print("**********ENTRY TICKET*********")
   print(" Name of Lead Booker:"+leadbooker)
   print(f"ADMIT ADULTS: {adultnum}")
   print(f"ADMIT CHILD:  {childnum}")
   print(f"ADMIT SENIOR: {seniornum}")
   print(f"Valid for :{d2}")
   print("*******************************")
   print("\nThankyou for your purchase")

printTicket()
