# Module 5 Lab-5
# Christopher Robles Serrano
#10/24/2024
# This program recieves inputs of the number of bottles collected, calculates the payout for said bottles, and prints the information to the terminal.

#Function to calculate the number of bottles collected over a week.
def getBottles():
    counter = 0
    totalBottles = 0
    NBR_OF_DAYS = 7
    #Iterates 7 times
    while counter < NBR_OF_DAYS:
        todayBottles = int(input(f"Enter number of bottles returned for day #{counter + 1}:  "))
        counter += 1
        #Adding todays bottles to total bottles over 7 iterations
        totalBottles += todayBottles
    return totalBottles

#Function to calculate the payout.
def calcPayout(myBottles):
    totalPayout = 0

    #Calculating and returning total payout
    totalPayout = myBottles * .10
    return totalPayout

#Main function to run our previous functions/methods
def main():
    keepGoing = 'y'
    #Keeps looping until our input is anything but 'y'.
    while keepGoing == 'y':
        #Calling getBottles() method and assigning to totalBottles
        totalBottles = getBottles()
        
        #Calling calcPayout() method and assingging it to totalPayout
        totalPayout = calcPayout(totalBottles)

        #Print statements
        print(f"The total number of bottles collected is {totalBottles}")
        print(f"The total paid out is ${totalPayout:.2f}")

        #Assining user input to keepGoing
        keepGoing = input("Do you want to enter another week's worth of data?\n(Enter y or n): ")

        #While loop for input validation of keepGoing. 
        while keepGoing not in ['y', 'Y', 'n', 'N']:
            print("Error. Please enter a valid character")
            keepGoing = input("Do you want to enter another week's worth of data?\n(Enter y or n): ")

        #Converting keepGoing to lowercase to ensure that 'Y' and 'y' are both valid for our while loop on line 31.
        keepGoing = keepGoing.lower()


#Calling the main function
main()