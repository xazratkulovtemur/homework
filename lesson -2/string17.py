word=str(input("Enter the sentence: "))
vowels= 'aoiueAOIUE'
for vowel in vowels:   #for each vowel in vowels
    word=word.replace(vowel, "*")
print(word)