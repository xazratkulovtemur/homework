import string
from collections import Counter
with open(r"D:\MAAB academy new\python\homework\lesson-6\homework\sample.txt", 'r', encoding="utf-8") as file: 
    content=file.read()



lower=content.lower()
lower.replace('.', '').replace(',', '').replace('-', '').replace(':', '').replace('"', '').replace("%", '').replace('?', '').replace('!', '')
words=lower.split()

all_words=len(words)

word_counter=Counter(words)
print("We are analyzing the paragraph! Specifically, their counting numebrs.")
n=int(input("Enter number so that I will provide you with this TOP: "))
top5=word_counter.most_common(n)

print(f"Total words : {all_words}")
print(f"Top {n} words: ")
for word, count in top5:
    print(f"{word}  : {count}")

with open(r"D:\MAAB academy new\python\homework\lesson-6\homework\word_count_report.txt", 'w') as file:
    file.write("Word Count Report!\n")
    file.write(f"Total words : {all_words}\n")
    for word, count in top5:
        file.write(f" {word} : {count}\n")
   