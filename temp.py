import heapq


def dijkstra(graph, start):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    previous_vertices = {vertex: [] for vertex in graph}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = [current_vertex]
                heapq.heappush(priority_queue, (distance, neighbor))
            elif distance == distances[neighbor]:
                previous_vertices[neighbor].append(current_vertex)

    return distances, previous_vertices


def all_shortest_paths(graph, start, end):
    distances, previous_vertices = dijkstra(graph, start)
    paths = []

    def backtrack(path, current_vertex):
        if current_vertex == start:
            paths.append(path[::-1])
            return
        for previous_vertex in previous_vertices[current_vertex]:
            backtrack(path + [previous_vertex], previous_vertex)

    backtrack([end], end)
    return paths


# 그래프 생성 (인접 리스트 형태)
graph = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 2},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 2, "C": 1, "E": 3},
    "E": {"D": 3, "F": 2},
    "F": {"E": 2, "G": 2},
    "G": {"F": 2},
}


start_vertex = "A"
end_vertex = "G"
all_paths = all_shortest_paths(graph, start_vertex, end_vertex)

print(f"시작 정점: {start_vertex}")
print(f"모든 최단 경로:")
for path in all_paths:
    print(" -> ".join(path))
