n = 10
guess = input("Double loop at n=10 checks n x n pairs.How Many?")
input("Formula: One calculation,done. Press ENTER to run.")
steps = 1
print("Steps =" ,steps , "-> O(1) Constant Time -> steps never change")
input("Loop: One step at a time. Press ENTER to run.")
steps = 0
for i in range(n):
    steps += 1
print("Steps =" ,steps , "-> O(n) Linear Time -> steps grow with n")
input("Double Loop: Checks every pair. Press ENTER to run.")
steps = 0
for i in range(n):
    for j in range(n):
       steps += 1
print("Steps =" ,steps ,"your guess:", guess, "-> O(n^2) Quadratic Time")  
input("Two more notations. Press ENTER.")
print(" Big Omega -> best-case lower bound")     
print(" Big Theta -> exact bound (worst=best)")