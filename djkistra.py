from heapq import *

# def djkistra(g,st,dist): #g contains b,dist(a to b) and dist is initiaalised by 10**9 initiallly
#     pq = []
#     dist[st] = 0
#     pq.append([0,st])
#     while(len(pq) != 0):
#         curr = heappop(pq)[1]
#         for i in range(0,len(g[curr])):
#             b = g[curr][i][0]
#             w = g[curr][i][1]
#             if(dist[b] > dist[curr] + w):
#                 dist[b] = dist[curr]+w
#                 pq.append([dist[b],b])


#updated
def djkistra(g,st,dist): #g contains b,dist(a to b) and dist is initiaalised by 10**9 initiallly
    pq = []
    dist[st] = 0
    heappush(pq,(0,st))
    while(len(pq) != 0):
        curr = heappop(pq)[1]
        for i in range(0,len(g[curr])):
            b = g[curr][i][0]
            w = g[curr][i][1]
            if(dist[b] > dist[curr] + w):
                dist[b] = dist[curr]+w
                heappush(pq,(dist[b],b))


n = int(input())
m = int(input())
g = [[] for i in range(n)]
for i in range(m):
    a,b,c = map(int,input().split())
    g[a].append([b,c])
    g[b].append([a,c])
print(g)

dist = [10**9]*(n)
print(djkistra(g,0,dist))

