grid = [[10, 3,  4,  6,  23],
        [9,  32, 12, 2,  34],
        [7,  8,  0,  21, 11],
        [18, 67, 55, 89, 90],
        [22, 33, 14, 44, 50]]
        
        
def hill_climbing(grid):
    r, c = 2, 2
    current = grid[r][c]
    
    found = False
    max_val = []
    neighbor = 0
    
    while found is False:
        vals = []
        
        up = [r-1, c]
        dwn = [r+1, c]
        rgt = [r, c+1]
        lft = [r, c-1]
        
        if up[0] >= 0 and up[0] <= 4 and up[1] >= 0 and up[1] <= 4:
            print('up',up)
            vals.append(['up',up])
        
        if dwn[0] >= 0 and dwn[0] <= 4 and dwn[1] >= 0 and dwn[1] <= 4:
            print('dwn',dwn)
            vals.append(['dwn',dwn])
            
        if rgt[0] >= 0 and rgt[0] <= 4 and rgt[1] >= 0 and rgt[1] <= 4:
            print('rgt',rgt)
            vals.append(['rgt',rgt])
        
        if lft[0] >= 0 and lft[0] <= 4 and lft[1] >= 0 and lft[1] <= 4:
            print('lft',lft)
            vals.append(['lft',lft])
            
        
        for i in vals:
            a, b = i[1][0], i[1][1]
            if grid[a][b] > neighbor:
                neighbor = grid[a][b]
                r, c = a, b
                
        print('neighbor',neighbor,'r=',r,'c=',c)
        
        
        if neighbor <= current:
            return (r, c)
        
        current = grid[r][c]
        
            
            
if __name__ == '__main__':

    state = hill_climbing(grid)
    print('Now state is:',state)


