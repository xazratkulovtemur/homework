def convert_cel_to_far(far): #this take argument far
    """Converting Farangeit to Celcius"""
    return (far-32)*5/9
far=float(input("Enter a temperature in degrees F: ")) #ask user to write 

cel = convert_cel_to_far(far) #equals cel to argument
print(f"{far} degrees of F = {cel:.2f} degrees C")



def convert_cel_to_far(cel): #this take argument cel
    """Converting celcius to farangeit"""
    return cel*9/5 +32  #calculation
cel=float(input("Enter a temperature in degrees C: "))

far=convert_cel_to_far(cel)  #equalling far to argument

print(f"{cel} degrees in C = {far:.2f} degrees in F")  #printing