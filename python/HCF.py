numberLargest = int(input("Enter your largest number:"))
numberSmallest = int(input("Enter your smallest number:"))

while (numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print("HCF is: ",numberLargest)    