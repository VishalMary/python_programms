a = [[0, 1, 0, 0, 1],
     [1, 0, 0, 1, 1],
     [0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0],
     [1, 0, 0, 0, 1]]

n = len(a)
area=1
def fun(i, j):
    if i < 0 or j < 0 or i >= n or j >= n or a[i][j] != 1:
        return 0
    a[i][j] = 0
    area=1
    area=area+fun(i-1, j)  
    area=area+fun(i+1, j)  
    area=area+fun(i, j-1)  
    area=area+fun(i, j+1)  
    return area
def count_islands(grid):
    islands_count = 0
    max_area=0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                islands_count += 1
                curr_area=fun(i, j)
                max_area=max(max_area,curr_area)
    return islands_count,max_area
num_islands = count_islands(a)

print( num_islands)