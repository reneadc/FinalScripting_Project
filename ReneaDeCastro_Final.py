#Renea De Castro Final Assignment for CIS 303
#REPL LINK: 
# https://repl.it/@reneadc/ReneaDeCastroFinalCIS303Project

#Here is my changes 
#here
#changes 

import time;
import subprocess; 
#To clear screen on Windows/Linux/MacOSx Systems
clear = lambda: subprocess.call('cls||clear', shell=True);

#birthMonth -dictionary
birthMonths = {
  "1":"January",
  "2":"February",
  "3":"March",
  "4":"April",
  "5":"May",
  "6":"June",
  "7": "July",
  "8": "August",
  "9": "September",
  "10": "October",
  "11": "November",
  "12": "December"
}

def checkName(string):
  while(True):
    if(not string.isalpha()):
      print("Umm... That is not a valid name! \n");
      string = input("Please re-enter your name WITH CHARACTERS Only: ");
    else:
      return string;
      break;
  
def checkMonth(string):
  while(True):
      
      if(not string in ('1', '2','3','4','5','6','7','8','9','10','11','12') or  not string.isnumeric()):
        print("That is a invalid input!");
        string =  input("Enter the month of your birth date AS A NUMBER:  ");
        
      else:
        return string;
        break;

def checkInput(string):
  while(True):
      string = string.strip();
      if(not string in ('0', '1')):
        print("That is a invalid input!");
        string =  input("Re-Enter 1 for 'yes' or 0 for 'no':  ");
      else:
        return string;
        break;

def printCard1():
  print("\n")
  print("Is your birthday in Card 1 ?: ")
  print( "| 1 | 3  | 5  | 7  |");
  print( "| 9 | 11 | 13 | 15 |");
  print( "| 17| 19 | 21 | 23 |");
  print( "| 25| 27 | 29 | 31 |");
  
  print("\n");

def printCard2():
  print("\n");
  print("Is your birthday in Card 2 ?: ");
  print( "| 2  | 3  | 6  | 7  |");
  print( "| 10 | 11 | 14 | 15 |");
  print( "| 18 | 19 | 22 | 23 |");
  print( "| 26 | 27 | 30 | 31 |");
  
  print("\n")

def printCard3():
  print("\n");
  print("Is your birthday in Card 3 ?: ");
  print( "| 4  | 5  | 6  | 7  |");
  print( "| 12 | 13 | 14 | 15 |");
  print( "| 20 | 21 | 22 | 23 |");
  print( "| 28 | 29 | 30 | 31 |");
  
  print("\n")

def printCard4():
  print("\n");
  print("Is your birthday in Card 4 ?: ");
  print( "| 8  | 9  | 10 | 11 |");
  print( "| 12 | 13 | 14 | 15 |");
  print( "| 24 | 25 | 26 | 27 |");
  print( "| 28 | 29 | 30 | 31 |");
  
  print("\n")

def printCard5():
  print("\n");
  print("Is your birthday in Card 5 ?: ");
  print( "| 16 | 17 | 18 | 19 |");
  print( "| 20 | 21 | 22 | 23 |");
  print( "| 24 | 25 | 26 | 27 |");
  print( "| 28 | 29 | 30 | 31 |");
  
  print("\n")

def binaryToDecimal(binaryNum):
  decimal = 0;
  i = 0;
  
  while(binaryNum != 0): 
    #Get the end of the binary number using modolus operator
    digit = binaryNum % 10;
    #Multiply the digit with 2^ith power
    #Store that value to decimal calculation
    decimal = decimal + digit * pow(2, i) 

    #Divide the binary Num to get the next digit 
    #and multiply with the next 2^ith power
    binaryNum = binaryNum//10;
    i += 1;
  return decimal;

def main():
  userName = "";
  userMonth = "";

  userInput = "";
  binaryNum =  "";

  i = 0;
  print("Welcome to the Birthday Guessing Program! \n");
  print("Let me guess the DAY in your birth date! \n")
  time.sleep(3);
  print("Please follow the prompts! ");
  time.sleep(2);
  clear();
  userName = input("What is your name?: ");
  userName = checkName(userName);
  print("Thank you! Welcome " + userName + "!");

  userMonth = input("What is your BIRTH MONTH as a NUMBER?: ");
  month = checkMonth(userMonth);
  print("Your birth month is:  " ,birthMonths[month]);


  #print(birthMonths[1]);
  

  while (i < 5):

        #Show each set of numbers
        printCard1();
        userInput =  input("Enter 1 for 'yes' or 0 for 'no':  ");
        userInput = checkInput(userInput);
        clear();
        #concatenate the input into the binary number
        binaryNum = userInput +binaryNum;

        i = i + 1;

        printCard2();
        userInput = input("Enter 1 for 'yes' or 0 for 'no':  ");
        userInput = checkInput(userInput);
        clear();
        binaryNum = userInput +binaryNum;
        userInput = checkInput(userInput);
        i = i + 1;
      
        printCard3();
        userInput = input("Enter 1 for 'yes' or 0 for 'no':  ");
        userInput = checkInput(userInput);
        clear();
        binaryNum = userInput +binaryNum;
        i = i + 1;

      
        printCard4();
        userInput = input("Enter 1 for 'yes' or 0 for 'no':  ");
        userInput = checkInput(userInput);
        clear();
        binaryNum = userInput +binaryNum;
        i = i + 1;
      
        printCard5();
        userInput = input("Enter 1 for 'yes' or 0 for 'no':  ");
        userInput = checkInput(userInput);
        clear();
        binaryNum = userInput +binaryNum;
        i = i + 1;
     
  

   
  #Test for the Binary Number if its correct!
  #print(binaryNum);
  print("Thank you for answering the prompts! \n");
  
  time.sleep(0.75);
  print("Hmmm.. Now let me guess your the day of your birthdate! \n")

  print("Guessing...");
  time.sleep(1);

  print("Almost there...");
  time.sleep(0.75);

  print("AHA!! ...");
  time.sleep(0.75);

  clear();
  print(userName + " , your birthday is...");

  

  time.sleep(0.50);
  
  
  decimal = "";
  decimal =  str(binaryToDecimal(int(binaryNum)));
  if(decimal == "0"):
    print("You've entered all 0s ... So I can't perform my magic :( \n");
    print("Restart the program if you would like to try again!")
  else:
    print(birthMonths[month] + " " +  decimal + " !" );
  

  print("Thank you for playing!");


main();