from queue import PriorityQueue

board = [['Z','A','E','B','W','$'],
         ['H','F','G','X','F','D'],
         ['*','R','S','#','M','K'],
         ['G','H','T','O','R','L'],
         ['D','I','@','S','C','Y'],
         ['V','W','N','P','Q','X']]
         
         

def get_neighbours(node, r, c):
    neighbours = []
    
    up = [r-1, c]
    dwn = [r+1, c]
    rgt = [r, c+1]
    lft = [r, c-1]

    if up[0] >= 0 and up[0] <= 5 and up[1] >= 0 and up[1] <= 5:
        if up not in neighbours:
            neighbours.append(up)

    if dwn[0] >= 0 and dwn[0] <= 5 and dwn[1] >= 0 and dwn[1] <= 5:
        if dwn not in neighbours:
            neighbours.append(dwn)

    if rgt[0] >= 0 and rgt[0] <= 5 and rgt[1] >= 0 and rgt[1] <= 5:
        if rgt not in neighbours:
            neighbours.append(rgt)

    if lft[0] >= 0 and lft[0] <= 5 and lft[1] >= 0 and lft[1] <= 5:
        if lft not in neighbours:
            neighbours.append(lft)
            
    return neighbours
    
# ----------------------------------------------------------------------------------
    
# fixed cost for ease

def get_cost(node_r, node_c, neighbour):
    
    # up
    if board[node_r-1][node_c] == board[neighbour[0]][neighbour[1]]:
        cost = 4
    
    # down
    if board[node_r+1][node_c] == board[neighbour[0]][neighbour[1]]:
        cost = 1
        
    # right
    if board[node_r][node_c+1] == board[neighbour[0]][neighbour[1]]:
        cost = 2
        
    # left
    if board[node_r][node_c-1] == board[neighbour[0]][neighbour[1]]:
        cost = 3
        
    return cost 
    
# ----------------------------------------------------------------------------------    
    
def get_index(board,node):
    for a in range(len(board)):
        for b in range(len(board[0])):
            if board[a][b] == node:
                r, c = a,b
                return (r,c)
                
#------------------------------------------------------------------------------------  
                
def GBFS(board, src, dest):
    visited_nodes = []
    que = PriorityQueue()
    que.put((0,src))
    t_cost = 0
    
    while que:
        cost, node = que.get()
        
        min_cost = float('inf')
        
        print(cost,node)
        
        if node not in visited_nodes:
            visited_nodes.append(node)
            
            if node == dest:
                print('Total cost:',t_cost,'Node:', node)
                return que
            
            idx = get_index(board,node)
            
            neighbours = get_neighbours(node, idx[0], idx[1])
            print(neighbours)
            
            for i in neighbours:
                if board[i[0]][i[1]] not in visited_nodes:
                    
                    cost = get_cost(idx[0],idx[1],i)
                    if cost < min_cost:
                        min_cost = cost
                        loc = board[i[0]][i[1]]
                        
            que.put((min_cost,loc))
            t_cost = t_cost + min_cost
            
            print('-------------')
            
    return False
    
# ----------------------------------------------------------------------------------

if __name__ == '__main__':
    GBFS(board,'Z','@')


