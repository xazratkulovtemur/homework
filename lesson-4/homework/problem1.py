list1=input("Enter elements for list1: ").split()
list2=input("ENter elements for list2: ").split()

set1=set(list1)
set2=set(list2)
print("Uncommon elements in lists:", set1 ^ set2)