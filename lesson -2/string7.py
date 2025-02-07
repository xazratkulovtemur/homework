sentence=str(input("Enter the sentence: "))
word1=str(input("Enter the word to replace: "))
if word1 in sentence: 
    
    word2=str(input("Which word do you want to replace with?"))
    print(sentence.replace(word1, word2))