rectangles = [[1,0,2,3],[1,0,3,1]]

# plane = [[0]*pow(10,9)]*pow(10,9) [0,0,2,2],

plane = [[0]*4]*4

for x0, y0, x1, y1 in rectangles:
    
    for i in range(x0, x1+1):
        for j in range(y0, y1+1):
            
            print(i, j)
            plane[i][j] = 1
    break

print(plane)
