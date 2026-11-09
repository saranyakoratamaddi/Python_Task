#Given a tuple `(10, 20, 30, 40, 50)`, write a program to print the first, last, and middle elements.





tp=(10,20,30,40,50)
print(tp)
print("The first Element in the Tuple is:",tp[0])
print("The Last Element in the Tuple is:",tp[-1])
tplen=len(tp)//2
midtp=tp[tplen]
print("Middle Element in the Tuple is:",midtp)
