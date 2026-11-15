#5. Word Counter Program 
#A writer saves an article in a file called article.txt. Write a Python program that: 
#● Opens and reads the file 
#● Counts the number of words, lines, and characters in the file 
#● Displays the results. 



file=open("article.txt","r")
content=file.read()
print(content)
words=len(content.split())
file.seek(0)
lines=len(file.readlines())
chars=len(content)
print("word count:",words)
print("LineCount:",lines)
print("Character count:",chars)
file.close()
