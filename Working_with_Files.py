i = 1
f = open('rosalind_ini5.txt')
line=""
for line in f.readlines():
    if i % 2 == 0 :
        print (line)
    i += 1
