import queue
import sys
def DFS_Traversal(cost,start_point,goals,l,visited):
    l.append(start_point)
    visited[0]=[1]
    visited[start_point]=1
    n=start_point
    if start_point in goals:
        return l   
    min_ind=0
    while len(l)>0 :
        minimum=sys.maxsize   #initialize all distance to infinity
        for i in range(1,len(cost)):              
            if cost[n][i]>0 and visited[i]==0:
                if cost[n][i]<minimum:         #find best node
                    minimum=cost[n][i]
                    min_ind=i
        if min_ind==l[-1]:
            l.pop()
            if(len(l)>0):
                n=l[-1]
            min_ind=n
        elif min_ind not in goals:
            l.append(min_ind)
            visited[min_ind]=1
            n=min_ind
        elif min_ind in goals:
            l.append(min_ind)
            visited[min_ind]=1
            break
    if len(l)!=0:
        return l
            

def UCS_Traversal(cost,start_point, goals, visited):
    visited.append(start_point)
    frontier = queue.PriorityQueue()
    l=[]
    gn=[0 for i in range(len(cost))]
    backtrack=[0 for i in range(len(cost))]
    frontier.put((0,start_point))
    temp=[start_point]
    if start_point in goals:
        l.append(start_point)
        return l
    while frontier.empty()==False:
        p,node=frontier.get()
        temp.remove(node)
        visited.append(node)
        for i in range(1,len(cost)):
            #temp=[lis[1] for lis in frontier]
            if i!=node and cost[node][i]>0:
                if i in visited:
                    if gn[i]>gn[node]+cost[node][i]:
                        gn[i]=gn[node]+cost[node][i]
                        backtrack[i]=node
                elif i not in visited and i not in temp:
                    
                    temp.append(i)
                    gn[i]=gn[node]+cost[node][i]
                    frontier.put((gn[i],i))
                    backtrack[i]=node

                
                elif i in temp and gn[i]>gn[node]+cost[node][i]:
                    #frontier.put((cost[node][i],i))
                    gn[i]=gn[node]+cost[node][i]
                    backtrack[i]=node
    dict_of_minimum={i:gn[i] for i in goals}
    min_cost=min(dict_of_minimum.values())
    for z in dict_of_minimum.items():
        if z[1]==min_cost and z[1]>0:
            min_goal=z[0]
    if min_goal!=start_point:
        l.append(min_goal)
  
    while min_goal!=start_point:
        l.append(backtrack[min_goal])
        min_goal=backtrack[min_goal]  
    l=l[::-1]  
    return l

    
def A_star_Traversal(cost,start_point, goals, visited, heuristic):
    visited.append(start_point)
    frontier = queue.PriorityQueue()
    l=[]
    fn=[0 for i in range(len(cost))]
    gn=[0 for i in range(len(cost))]
    backtrack=[0 for i in range(len(cost))]
    frontier.put((0,start_point))
    temp=[start_point]
    if start_point in goals:
        l.append(start_point)
        return l
    while frontier.empty()==False:
        p,node=frontier.get()
        temp.remove(node)
        visited.append(node)
        for i in range(1,len(cost)):
            #temp=[lis[1] for lis in frontier]
            if i!=node and cost[node][i]>0:
                if i in visited:
                    if gn[i]>gn[node]+cost[node][i]:
                        gn[i]=gn[node]+cost[node][i]
                        backtrack[i]=node
                elif i not in visited and i not in temp:
                    
                    gn[i]=gn[node]+cost[node][i]
                    backtrack[i]=node
                    fn[i]=gn[i]+heuristic[i]
                    frontier.put((fn[i],i))
                    temp.append(i)
                
                elif i in temp and gn[i]>gn[node]+cost[node][i]:
                    #frontier.put((cost[node][i],i))
                    gn[i]=gn[node]+cost[node][i]
                    backtrack[i]=node
    dict_of_minimum={i:gn[i] for i in goals}
    min_cost=min(dict_of_minimum.values())
    for z in dict_of_minimum.items():
        if z[1]==min_cost and z[1]>0:
            min_goal=z[0]
    if min_goal!=start_point:
        l.append(min_goal)
  
    while min_goal!=start_point:
        l.append(backtrack[min_goal])
        min_goal=backtrack[min_goal]  
    l=l[::-1]  
    return l


'''
Function tri_traversal - performs DFS, UCS and A* traversals and returns the path for each of these traversals 

n - Number of nodes in the graph
m - Number of goals ( Can be more than 1)
1<=m<=n
Cost - Cost matrix for the graph of size (n+1)x(n+1)
IMP : The 0th row and 0th column is not considered as the starting index is from 1 and not 0. 
Refer the sample test case to understand this better

Heuristic - Heuristic list for the graph of size 'n+1' 
IMP : Ignore 0th index as nodes start from index value of 1
Refer the sample test case to understand this better

start_point - single start node
goals - list of size 'm' containing 'm' goals to reach from start_point

Return : A list containing a list of all traversals [[],[],[]]
1<=m<=n
cost[n][n] , heuristic[n][n], start_point, goals[m]

NOTE : you are allowed to write other helper functions that you can call in the given fucntion
'''

def tri_traversal(cost, heuristic, start_point, goals):
    l = []
    visited=[0 for i in range(len(cost))]
    #visited2=[0 for i in range(len(cost))]
    t1 = DFS_Traversal(cost,start_point,goals,[],visited
    #send whatever parameters you require 
)
    t2 = UCS_Traversal(cost,start_point,goals, []
    #send whatever parameters you require 
)
    t3 = A_star_Traversal(cost,start_point,goals,[],heuristic
    #send whatever parameters you require 
)

    l.append(t1)
    l.append(t2)
    l.append(t3)
    return l
