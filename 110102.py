'''
    Description:
To solve the problem, the program starts with reading the dimensions of
the field, then initiates a bunch of Point objects that holds the value
read at the point and count of neighbouring mines. Going through each
line of the input of the map, it finds any mines and marks it on the
new map, and increments surrounding points by one. After the input is
completely read, the map we created is then printed as the answer

This program can be modified to dismiss the use of a point class
'''

class Point:
    # upon creation have a value to read, one to count surrounding mines
    def __init__(self):
        self.readval = '0'
        self.count = 0
    # This setVal function will either set mines (string) or counters (ints)
    def setVal(self, val):
        if(type(val) == str):
            self.readval = val
        elif(self.readval != '*'):
            self.count = self.count + val
            self.readval = str(self.count)     

# get the file input
f = open("110102.txt","r")
# read each line methodically
line = f.readline().strip()
cnt = 0
while (line != ''):
    # Given the dimensions of the table in the first line, read the rest
    dime = line.split(" ")
    h = int(dime[0])
    l = int(dime[1])
    # if either dimension is 0, move on
    if( h == 0 or l == 0 ):
        line = f.readline().strip()
        continue
    cnt = cnt + 1
    # create an M x N matrix based on the data
    grid = [[Point() for x in range(l)]for y in range(h)]
    for y in range(h):
        line = f.readline().strip()
        for x in range(l):
            if(line[x]=='*'):
                grid[y][x].setVal('*')
                # go around the mine and increase surrounding counters
                for sy in range(y-1,y+2):
                    for sx in range(x-1,x+2):
                        if (sy >= 0 and sy < h and sx >= 0 and sx < l):
                            pnt = grid[sy][sx]
                            pnt.setVal(1)

    print('Field #'+str(cnt)+':')
    for row in grid:
        ln = ''
        for column in row:
            ln = ln + column.readval
        print(ln)
    print('') 
    # given our 
    
    line = f.readline().strip()

f.close()
