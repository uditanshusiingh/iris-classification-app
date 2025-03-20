#Create a tuple
tuple = (10,20,30,40,50)
print("Initial tuple: ",tuple)

# Slicing tuple
slice = tuple[2:5]
print("Sliced tuple: ",slice)

# Length of the tuple
print("Length of tuple: ",len(tuple))

# concatenating tuple
tuple2 = (60,70,80,90)
print("Combined tuple: ",tuple + tuple2)

# Nested tuple
tuple3 = ((10,20),30,(40,50))
print("Nested tuple: ",tuple3)

# Unpacking tuple
a,b,c,d,e = tuple
print("Unpacked tuple: ",a,b,c,d,e)