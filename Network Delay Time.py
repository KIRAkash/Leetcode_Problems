""" There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1."""
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        traversed=[0]*N
        time=[6001]*N
        current=[K]
        time[K-1]=0
        traversed[K-1]=1
        while(1):
            newcurrent=[]
            change=False
            for path in times:
                if path[0] in current:
                    if(traversed[path[1]-1]==0):
                        newcurrent.append(path[1])
                        traversed[path[1]-1]=1
                        time[path[1]-1]=time[path[0]-1]+path[2]
                        change=True
                    elif time[path[1]-1]>(time[path[0]-1]+path[2]):
                        time[path[1]-1]=time[path[0]-1]+path[2]
                        change=True
                        newcurrent.append(path[1])
            if(change==False):
                break
            else:
                current=newcurrent
        if 0 in traversed:
            return -1
        else:
            return max(time)
        
