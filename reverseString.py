
line = "What is the meaning of Life 4"
words = line.split()
o = " "
index = words[len(words) -1]
print index
for num in range(0, len(words) - 1):
  if(num == (int(index) - 1)):
    r = words[num]
    print r
    o = o + " " + r[::-1]
  else:
    o = o + " " + words[num]
print o