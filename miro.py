def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

        if graph[nx][ny] == 0:
            continue 
        if graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, xy))

    return graph[n - 1][m - 1]

from collections import deque

n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의 (상,하,좌,우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# BFS를 수행한 결과 출력 
print(bfs(0,0))