MAX = 10 ** 10

n = int(input())
pos = [list(map(int,input().split())) for _ in range(n)]
dis = [[0] * n for _ in range(n)]

for p1 in range(n):
    for p2 in range(n):
        x1,y1 = pos[p1]
        x2,y2 = pos[p2]       
        dis[p1][p2] = ((x1-x2)**2 + (y1-y2)**2)**0.5
        dis[p2][p1] = ((x1-x2)**2 + (y1-y2)**2)**0.5
        
minn = MAX
def dfs(cur, d, path): # 현재노드, 거리, 경로
    global minn, answer_path
    
    if len(path) == n:
        if d + dis[cur][0] < minn:
            minn = d + dis[cur][0]
            answer_path = path[:]

    for i in range(n):
        if i in path:
            continue
        path.append(i)
        if d + dis[cur][i] < minn:
            dfs(i, d + dis[cur][i], path)
        path.pop()

dfs(0, 0, [0])

print(minn)
print(answer_path)
