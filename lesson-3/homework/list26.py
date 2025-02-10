numbers=[1,2,3,4,5,6,7,8,9,10]
length=len(numbers)
middle_odd=(length-1)/2+2 #if odd, middle point
middle1=(length/2+1) #if even, starting point
middle2=(length/2+2) #if even, ending point
if length%2==1:
    print(numbers.index(middle_odd))
else:
    print(numbers.index(middle1), numbers.index(middle2))

#finding middle number, if number of elemets is odd, print middle one.  If number of elements is even, print two middle elements