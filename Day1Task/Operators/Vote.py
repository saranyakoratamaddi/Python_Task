#4. Write a program using logical operators to check age eligibility for voting.   


age=int(input("enter your age:"))
vote=(age>=18 and "Elgible for vote") or "Not Elgible"
print(vote)
