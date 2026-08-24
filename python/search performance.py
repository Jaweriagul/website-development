scores = [1,3,4,6,7,9,10,2,5,8]
input("List:" + str(scores) + "n=9 Linear search - checks left to right. Press ENTER.")
target = int(input("Enter a number to search for:"))
input("searching for:" + str(target) + ". Press ENTER to run")
steps = 0
for score in scores:
    steps += 1
    if score == target:
       break
print("target = ", target, "found at position:", steps, "checks = ",steps)
input("compare with best and worst case. Press ENTER.")
mid = len("scores")//2
print("Best: 1 check -> O(1) Average:",mid,"checks -> O(n) worst:9 checks -> O(n) Yours:",steps)
input("All Three cases. Press ENTER.")
print("Best O(1) Average O(n) Worst o(n) -> Big-O = Worst case = O(n).")