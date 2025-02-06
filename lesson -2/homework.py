#Datatype questions


#problem1 
"""
a=float(input("Enter decimal number:"))
print(f"{a:.2f}")

"""

#problem2
"""
a=int(input("Enter the first number: "))
b=int(input("ENter second number: "))
c=int(input("ENter third number: "))

if a<b and b<c: 
    print(f"{c} is the largest, and {a} is the smallest")
if a>b and b>c:
    print(f"{a} is the largest, and {c} is the smallest")
if a<c and c<b:
    print(f"{b} is the largest, {a} is the smallest")
if b<c and c<a:
    print(f"{a} is largest, and {b} is smallest")
if c<a and a<b:
    print(f"{b} is the largest, and {c} is the smallest")
if b<a and a<c:
    print(f"{c} is largest, and {b} is smallest")

"""

#problem3
"""
a=float(input("Enter distance in meters: "))
k=a/1000
c=a*1000
print(f"{a} meters are: \n {k} kilometers and {c} centimeters")

"""

#problem 4
"""
a=int(input("Enter the number: "))
b=int(input("Enter the divisor: "))
x,y=divmod(a,b)
print(f"Answer is  {x} and remainder is {y}") 
"""
#problem5
"""
a=float(input("Enter degree in Celsius: "))
f=a*9/5+32
print(f"Temprature in Faranheit is {f}")
"""
#problem6

"""
a=str(input("Enter the number: "))
print(f"Last digit is {a[-1]}")
"""

#problem7
"""
a=int(input("Enter the number: "))
if a%2==0:
    print("EVen number")
else: 
    print("Odd number")
"""

#STring questions

#problem1
"""
a=str(input("Enter your name: "))
b=int(input("Enter your year of birth:"))
age=2025-b
print("Hey,  {} . You are {} years old".format(a, age) )
"""

#problem2 
"""
txt = 'LMaasleitbtui'
print(txt[::2])
"""
#problem3
"""
word=str(input("Enter the word: "))
print(len(word))
print(word.upper())
print(word.lower())
"""

#problem4

"""
word=str(input("Enter the word; "))
if word==word[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
    """

#problem5





#problem6
"""
string1=str(input("Enter the word: "))
string2=str(input("Enter second word: "))
if string2 in string1:
    print("True")
else:
        print("False")
"""

#problem7
"""
sentence=str(input("Enter the sentence: "))
word1=str(input("Enter the word to replace: "))
if word1 in sentence: 
    
    word2=str(input("Which word do you want to replace with?"))
    print(sentence.replace(word1, word2))
"""

#problem8
"""
word=str(input("Enter the word: "))
print(f"First letter is {word[0]}, and last letter is {word[-1]}")
"""

#problem9
"""
word=str(input("Enter the word: "))
print(word[::-1])
"""

#problem10
"""
sentence=str(input("Enter the entence: "))
word_count=len(sentence.split())
print(word_count)
"""

#problem11
"""
sentence=str(input("Enter the sentence: "))
if any(char.isdigit() for char in sentence):
    print("True")
else:
    print("False" )
    """
#problem12
"""
sentence=str(input("Enter the words :"))
separator=str(input("choose the separator. Eg: , - ;"))
print(separator.join(sentence.split()))
"""

#problem13
"""
word=str(input("Enter the sentence: "))
print(word.replace(" ", ""))

"""

#problem14 
"""
st1=str(input("Enter the first word: "))
st2=str(input("Enter second word: "))
if st1==st2:
    print("Equal")
else:
    print("Not equal")
    """

    #problem15
"""
sentence=str(input("Enter the word: "))
first_letters=[word[0] for word in sentence.split()]  #split separates sentence into words. and [word[0] for word in sentence.split()]  extracts first char of each words
acronym="".join(first_letters) #joins the first letters
print(acronym)
"""

#problem16
"""
word=str(input("Enter the sentence: "))
char=str(input("Enter the character: "))
print(word.replace(char, ""))
"""

#problem17
"""
word=str(input("Enter the sentence: "))
vowels= 'aoiueAOIUE'
for vowel in vowels:   #for each vowel in vowels
    word=word.replace(vowel, "*")
print(word)
"""

#print18
"""
word=str(input("Enter the sentence: "))
words=word.split()
print(f"Sentence begin with {words[0]}, and ends with {words[-1]}")
"""
#problem1

print("Hello world")
a='men'