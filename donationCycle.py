if __name__ == "__main__":
    from collections import deque
    import sys
    if len(sys.argv) < 2:
        print("Error -> No File")
        sys.exit(1)

    input_file = sys.argv[1]

with open(sys.argv[1], 'r') as file:
    content = file.readlines()
recipientNum = int(content[0].strip())
donorNum = int(content[1].strip())
donorAssociated = list(map(int, content[2].strip().split(',')))
hlaMatchScore = []
for i in range(3, 3 + donorNum):
    row = list(map(int, content[i].strip().split(',')))
    hlaMatchScore.append(row)
queryRecipient = int(content[3 + donorNum].strip())
graph = {}

for recipient in range(recipientNum):
    graph[recipient] = {}

for donor, relative in enumerate(donorAssociated):
    for recipientCo in range(recipientNum):
        if hlaMatchScore[donor][recipientCo] >= 60:
            graph[recipientCo][donor] = relative


def bfs(graph, start, target):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node == target and len(graph[node]) > 0:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
    return False


query = bfs(graph, queryRecipient, queryRecipient)

if query:
    print("TRUE")
else:
    print("FALSE")