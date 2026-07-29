n = int(input("How many characters to read?"))
file = open("notes.txt","r")
print(file.read(n))
file.close()
print()

file = open("notes.txt","r")
odd = file.readlines()
file.close()
print(f"total line: ",len(odd))
for i in range(len(odd)):
    print(i + 1,'->',odd[i].strip())
print()    

word = input("Skip the lines starting with: ")
file = open("notes.txt","r")
for odd in file:
    if odd.startswith(word):
        print("skip->",odd.strip())
    else:   
        print("keep->",odd.strip())
file.close()        
print()

file = open("notes.txt","r")
lines = file.readlines()
file.close()
even = open("odd-file.txt","w")
for i in range(0, len(lines), 2):
    even.write(lines[i])
even.close()
print("Odd lines saved to odd-file.txt")