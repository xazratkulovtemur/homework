"""
txt=str(input("Enter the text: "))
new_txt=''



seen_chars=['a', 'b', 'c', 'e', 'i', 'A', 'I', 'U', 'O', 'E']


count=0
valid_count=0

for i in range(len(txt)):
    if txt[i] not in seen_chars: 
        valid_count+=1
        new_txt+=txt[i]

    if txt[i] in seen_chars:
        pass
        
    if valid_count%3==0 and valid_count!=0:
        seen_chars.append(txt[i])
        new_txt+='_'
        valid_count+=1
    
print(new_txt)

"""

txt = input("Enter the text: ")
new_txt = ''
 

seen_chars = ['a', 'b', 'c', 'e', 'i', 'A', 'I', 'U', 'O', 'E']
pending_underscore = False
valid_count = 0

for i in range(len(txt)):
    if txt[i] in seen_chars: 
      new_txt += txt[i]
      continue
    if pending_underscore:
      new_txt += '_'
      pending_underscore = False

    valid_count += 1
    new_txt +=txt[i]
    if valid_count % 3 == 0:
      new_txt += '_'
      
      pending_underscore = True
    
print(new_txt)




    

