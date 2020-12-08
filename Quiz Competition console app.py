X1 =""" What is 's' stands for in brics?
a.srilanka
b.southafrica
c.southkorea
d.south america
"""

X2 =""" Where will the 2020 Olympics will take place?
a.rusia
b.sweden
c.japan
d.australia
"""

X3 ="""Who was the player of the tournament in ICC world cup 2019?
a. aaron finch
b.Kane Williamson
c.joe root
d.jason roy
"""

X4 = """Which of the following is not the concept of python?
a.list
b.dictionary
c.pointer
d.function
"""

questions = {X1:"b", X2:"c", X3:"b",X4:"c"}

name = input("Enter your name:")
print("hello", name, "Welcome to the Quiz Competition")
score =0
for i in questions:
    
    print(i)
    flag1 =input("Do you want to skip the question (yes/no)?")
    if(flag1 == "yes"):
      continue
    ans = input("Enter your choice(a/b/c/d)")
    if(ans == questions[i]):
      print("Correct answer you got one point")
      score= score+1
      print("Your current score is :",score)
    else:
         print("Wrong answer you loose one point")
         score= score-1
         print("your current score is:", score)
    flag2 = input("Do you want to quit the quiz(yes/no)?")
    if(flag2 == "yes"):
      break
print("Your final score is :", score)

      
