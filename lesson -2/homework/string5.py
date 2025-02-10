word=str(input("Enter a sentence: "))
vowels='aeiuoAEIUO'
vowel_count=0
constant_count=0
for char in word: 
    if char.isalpha(): 
        if char in vowels: 
            vowel_count += 1
        else: 
            constant_count +=1
print(f"Number of vowels in sentence:  {vowel_count} . Number of constants in sentence:  {constant_count}") 

        