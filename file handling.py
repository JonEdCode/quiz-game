#file = open("very good file.txt ","w")
#file.write("this is the best file it is very good ")
#file.close()
file = open("very good file.txt ","r")
reading = file.readlines()
print(reading)
file.close()

