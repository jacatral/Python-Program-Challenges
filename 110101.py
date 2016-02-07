def cycle( x ):
    # assume we are always working with positive numbers
    y = abs(x)
    cnt = 1
    while y != 1:
        cnt = cnt + 1
        if (y % 2 == 0):
            y = y / 2
        else:
            y = 3*y + 1
    return cnt;

# get the file input
f = open("110101.txt","r")
# read each line in the input
for line in f:
    data = line.strip()
    # separate the data into the integer numbers
    l = data.split(" ")
    # go through each number in the range and run the algorithm (brute force)
    mcyc = 0
    for i in range(int(l[0]),int(l[1])):
        cyc_cnt = cycle(i)
        if(cyc_cnt > mcyc):
            mcyc = cyc_cnt
    print(data + " " + str(mcyc))
f.close()

# this program works best with small ranges for input
