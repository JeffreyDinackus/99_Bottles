N = 99
arr = []
for num in reversed(range(N + 1)) : 
  
  arr.append("{} bottles of beer on the wall! {} bottles of beer on the wall!".format(num,num))
  arr.append("Take one down pass it around!")


arr = " ".join(arr)

arr = str(arr)

#save to file

f = open( '99_bottles_polly.txt', 'w')
f.write(arr)
f.close()

