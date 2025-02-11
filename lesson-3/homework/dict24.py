tuple1=('name', 'lastname', 'age')
tuple2=('Temur', 'Xazratqulov', 17)
joined={}

joined=dict(zip(tuple1, tuple2)) # i use zip() to pair element in tuple
print(joined)