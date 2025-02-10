#Joining first letters of each word. Example WTO
sentence=str(input("Enter the word: "))
first_letters=[word[0] for word in sentence.split()]  #split separates sentence into words. and [word[0] for word in sentence.split()]  extracts first char of each words
acronym="".join(first_letters) #joins the first letters
print(acronym)