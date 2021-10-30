#python 3.7.1

# Import
import time
import random

# Question 1
print("\nSIMPLE QUIZ\n")
time.sleep(0.6)
otp = random.randint(1111,9999)
player_name = input("Enter your name:")
time.sleep(0.6)
print("Human Verification process")
time.sleep(1)
print("Your code is",otp)
time.sleep(1)
print("Enter above code to continue")
typed_code = int(input())
if typed_code == otp :
  time.sleep(1)
  print("Code accepted")
  time.sleep(0.4)
  print("\nWELCOME")
  time.sleep(0.6)
  line = ("_"*35)
  star = ("*"*35)
  time.sleep(0.6)
  print(line)
###########################################
  # Question 1
  print(star)
  print("[*] Question 1\n>>> Who is the CEO of Facebook?\n")
  time.sleep(1)
  print("a,Jeff Bezos  b,Mark Zuckerberg\nc,Elon Musk   d,Jawed Karim")
  time.sleep(0.6)
  qn1 = input("Answer:")
  print("")
  time.sleep(0.6)
  if qn1 == "a":
    print("Wrong answer")
    time.sleep(0.4)
    print("You got 0 points")
    p1 = 0
  elif qn1 == "b":
    print("Correct answer")
    time.sleep(0.4)
    print("You got 10 points")
    p1 = 10
  elif qn1 == "c":
    print("Wrong answer")
    time.sleep(0.4)
    print("You got 0 points")
    p1 = 0
  elif qn1 == "d":
    print("Wrong answer")
    time.sleep(0.4)
    print("You got 0 points")
    p1 = 0
  else :
    print("wrong input")
    time.sleep(0.4)
    print("You got 0 points")
    p1 = 0
  print(line)
###########################################
  # Question 2
  print(star)
  time.sleep(0.6)
  print("\n[*] Question 2\n>>> Who is the founder SpaceX?\n")
  time.sleep(1)
  print("a,Walt Disney  b,Narendra Modi\nc,Elon Musk    d,Mukesh Ambani")
  time.sleep(0.6)
  qn2 = input("Answer:")
  time.sleep(0.6)
  print("")
  if qn2 == "a":
    print("Wrong answer")
    time.sleep(0.4)
    print("You got 0 points")
    p2 = 0
  elif qn2 == "b":
    print("Wrong answer")
    time.sleep(0.4)
    print("You got 0 points")
    p2 = 0
  elif qn2 == "c":
    print("Correct answer")
    time.sleep(0.4)
    print("You got 10 points")
    p2 = 10
  elif qn2 == "d":
    print("Wrong answer")
    time.sleep(0.4)
    print("You got 0 points")
    p2 = 0
  else :
    print("wrong input")
    time.sleep(0.4)
    print("You got 0 points")
    p2 = 0
  print(line)
###########################################  
  # Question 3
  print(star)
  time.sleep(0.6)
  print("\n[*] Question 3\n>>> Shape of Milky way Galaxy?\n")
  time.sleep(1)
  print("a,Circular      b,Square\nc,Elliptical    d,Spiral")
  time.sleep(0.6)
  qn3 = input("Answer:")
  time.sleep(0.6)
  print("")
  if qn3 == "a":
    print("Wrong answer")
    time.sleep(0.4)
    print("You got 0 points")
    p3 = 0
  elif qn3 == "b":
    print("Wrong answer")
    time.sleep(0.4)
    print("You got 0 points")
    p3 = 0
  elif qn3 == "c":
    print("Wrong answer")
    time.sleep(0.4)
    print("You got 0 points")
    p3 = 0
  elif qn3 == "d":
    print("Correct answer")
    time.sleep(0.4)
    print("You got 10 points")
    p3 = 10
  else :
    print("wrong input")
    time.sleep(0.4)
    print("You got 0 points")
    p3 = 0
  print(line)
###########################################    
  # Question 4
  print(star)
  time.sleep(0.6)
  print("\n[*] Question 4\n>>> Which of the following is not a \nform of Carbon?\n")
  time.sleep(1)
  print("a,Hematite    b,Diamond\nc,Graphite    d,Charcoal")
  time.sleep(0.6)
  qn4 = input("Answer:")
  time.sleep(0.6)
  print("")
  if qn4 == "a":
    print("Correct answer")
    time.sleep(0.4)
    print("You got 10 points")
    p4 = 10
  elif qn4 == "b":
    print("Wrong answer")
    time.sleep(0.4)
    print("You got 0 points")
    p4 = 0
  elif qn4 == "c":
    print("Wrong answer")
    time.sleep(0.4)
    print("You got 0 points")
    p4 = 0
  elif qn4 == "d":
    print("Wrong answer")
    time.sleep(0.4)
    print("You got 0 points")
    p4 = 0
  else :
    print("wrong input")
    time.sleep(0.4)
    print("You got 0 points")
    p4 = 0
    print(line)
###########################################
  # Question 5
  print(star)
  time.sleep(0.6)
  print("\n[*] Question 5\n>>> Alfa-toxins are produced by...?\n")
  time.sleep(1)
  print("a,Bacteria   b,Algae\nc,Viruses    d,Fungi")
  time.sleep(0.6)
  qn5 = input("Answer:")
  time.sleep(0.6)
  print("")
  if qn5 == "a":
    print("Wrong answer")
    time.sleep(0.4)
    print("You got 0 points")
    p5 = 0
  elif qn5 == "b":
    print("Wrong answer")
    time.sleep(0.4)
    print("You got 0 points")
    p5 = 0
  elif qn5 == "c":
    print("Wrong answer")
    time.sleep(0.4)
    print("You got 0 points")
    p5 = 0
  elif qn5 == "d":
    print("Correct answer")
    time.sleep(0.4)
    print("You got 10 points")
    p5 = 10
  else :
    print("wrong input")
    time.sleep(0.4)
    print("You got 0 points")
    p5 = 0
  print(line)
 ###########################################
  # Question 6
  print(star)
  time.sleep(0.6)
  print("\n[*] Question 6\n>>> Speed of light?\n")
  time.sleep(1)
  print("a,100 m/s         b,299792458 m/s\nc,11111111 m/s    d,698708547 m/s")
  time.sleep(0.6)
  qn6 = input("Answer:")
  time.sleep(0.6)
  print("")
  if qn6 == "a":
    print("Wrong answer")
    time.sleep(0.4)
    print("You got 0 points")
    p6 = 0
  elif qn6 == "b":
    print("Correct answer")
    time.sleep(0.4)
    print("You got 10 points")
    p6 = 10
  elif qn6 == "c":
    print("Wrong answer")
    time.sleep(0.4)
    print("You got 0 points")
    p6 = 0
  elif qn6 == "d":
    print("Wrong answer")
    time.sleep(0.4)
    print("You got 0 points")
    p6 = 0
  else :
    print("wrong input")
    time.sleep(0.4)
    print("You got 0 points")
    p6 = 0
  print(line)
###########################################
  # Question 7
  print(star)
  time.sleep(0.6)
  print("\n[*] Question 7\n>>> Sun is a ____?\n")
  time.sleep(1)
  print("a,Planet  b,Blanet\nc,Star    d,Lightning rock")
  time.sleep(0.6)
  qn7 = input("Answer:")
  time.sleep(0.6)
  print("")
  if qn7 == "a":
    print("Wrong answer")
    time.sleep(0.4)
    print("You got 0 points")
    p7 = 0
  elif qn7 == "b":
    print("Wrong answer")
    time.sleep(0.4)
    print("You got 0 points")
    p7 = 0
  elif qn7 == "c":
    print("Correct answer")
    time.sleep(0.4)
    print("You got 10 points")
    p7 = 10
  elif qn7 == "d":
    print("Wrong answer")
    time.sleep(0.4)
    print("You got 0 points")
    p7 = 0
  else :
    print("wrong input")
    time.sleep(0.4)
    print("You got 0 points")
    p7 = 0
  print(line)
###########################################
  # Question 8
  print(star)
  time.sleep(0.6)
  print("\n[*] Question 8\n>>> 1000 + 100 + 1000 + 200 + 1000 + 300\n + 1000 + 400?\n")
  time.sleep(1)
  print("a,4500    b,0\nc,3800    d,5000")
  time.sleep(0.6)
  qn8 = input("Answer:")
  time.sleep(0.6)
  print("")
  if qn8 == "a":
    print("Wrong answer")
    time.sleep(0.4)
    print("You got 0 points")
    p8 = 0
  elif qn8 == "b":
    print("Wrong answer")
    time.sleep(0.4)
    print("You got 0 points")
    p8 = 0
  elif qn8 == "c":
    print("Wrong answer")
    time.sleep(0.4)
    print("You got 0 points")
    p8 = 0
  elif qn8 == "d":
    print("Correct answer")
    time.sleep(0.4)
    print("You got 10 points")
    p8 = 10
  else :
    print("wrong input")
    time.sleep(0.4)
    print("You got 0 points")
    p8 = 0
  print(line)
########################################### 
  # Question 9
  print(star)
  time.sleep(0.6)
  print("\n[*] Question 9\n>>> Google was founded in which year?\n")
  time.sleep(1)
  print("a,1998    b,2007\nc,1990    d,2012")
  time.sleep(0.6)
  qn9 = input("Answer:")
  time.sleep(0.6)
  print("")
  if qn9 == "a":
    print("Correct answer")
    time.sleep(0.4)
    print("You got 10 points")
    p9 = 10
  elif qn9 == "b":
    print("Wrong answer")
    time.sleep(0.4)
    print("You got 0 points")
    p9 = 0
  elif qn9 == "c":
    print("Wrong answer")
    time.sleep(0.4)
    print("You got 0 points")
    p9 = 0
  elif qn9 == "d":
    print("Wrong answer")
    time.sleep(0.4)
    print("You got 0 points")
    p9 = 0
  else :
    print("wrong input")
    time.sleep(0.4)
    print("You got 0 points")
    p9 = 0
  print(line)
###########################################
  # Question 10
  print(star)
  time.sleep(0.6)
  print("\n[*] Question 10\n>>> Which one of the following\nis not a Blood group?\n")
  time.sleep(1)
  print("a,O.   b,B\nc,A    d,X")
  time.sleep(0.6)
  qn10 = input("Answer:")
  time.sleep(0.6)
  print("")
  if qn10 == "a":
    print("Wrong answer")
    time.sleep(0.4)
    print("You got 0 points")
    p10 = 0
  elif qn10 == "b":
    print("Wrong answer")
    time.sleep(0.4)
    print("You got 0 points")
    p10 = 0
  elif qn10 == "c":
    print("Wrong answer")
    time.sleep(0.4)
    print("You got 0 points")
    p10 = 0
  elif qn10 == "d":
    print("Correct answer")
    time.sleep(0.4)
    print("You got 10 points")
    p10 = 10
  else :
    print("wrong input")
    time.sleep(0.4)
    print("You got 0 points")
    p10 = 0
  print(line)
###########################################
  # Total Score
  total = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10
  print("\nTotal score:",total)
  if total == 0 :
    print("Go to school")
  elif total < 20 :
    print("Ohh Damn... ",player_name.lower()," lost the game")
  elif total < 50:
    print("Hmm... NICE TRY",player_name.upper())
  elif total > 50 :
    print("Yeah...",player_name.upper()," WON")
  elif total == 100 :
    print("Excellent...",player_name.lower(),"is a Genius")
  print("\nRate my Quiz (1 to 5)")
  rate = int(input("Rating:"))
  if rate == 1:
    print("Okay,I will try to fix it further")
  elif rate == 2:
    print("Thanks,I will try my best next time")
  elif rate == 3:
    print("Really appreciate that ;)")
  elif rate == 4:
    print("Thanks a lot :)")
  elif rate == 5:
    print("I'm feeling great :)")
  else:
    print("Thank you for your Rating :)")
  time.sleep(0.6)
  print("If you like this project,Give me a Star\nInstagram:@flynn_bait")
else:
  time.sleep(0.6)
  print("\nCode not Matching")
  time.sleep(0.6)
  print("It seems like",player_name,"is an Alien")
  time.sleep(0.6)
  print("Sorry,Unable to start Quiz with an Alien")
