
print("Welcome to the Love Calculator!")
U = input("What is your name?\n")
H = input("What is their name?\n")
couple=U+H
u=couple.lower()
p1=u.count("t")+u.count("r")+u.count("u")+u.count("e")
p2=u.count("l")+u.count("o")+u.count("v")+u.count("e")
#l=p1*10+p2
print(p1,p2)
l=int(str(p1)+str(p2))
if(l<10 and l>90):
  print(f"your love percentage is {l}% and you both are like coke and mentos..LOL")
elif(l>40 and l<=90):
  print(f"your love percentage is {l}% great pair..")
else:
  print(f"Your love percentage is {l}%")


  