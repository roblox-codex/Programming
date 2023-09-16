# F as a goal

def dfs(graph, start, goal):
    stack = [(start, [start])] 
    
    while stack:
        current_node, path = stack.pop() 
        
        if current_node == goal:
            return path 
        
        for neighbor in graph[current_node]:
            if neighbor not in path: 
                new_path = path + [neighbor]  
                stack.append((neighbor, new_path))  
    
    return None  

# Example usage:
graph = {
    'S': ['A', 'D'],
    'A': ['H', 'B'],
    'H': [],
    'B': ['I', 'F', 'G'],
    'I': [],
    'F': [],
    'G': [],
    'D': ['F', 'P', 'Q'],
    'P': [],
    'Q': []
}

start_node = 'S'
goal_node = 'F'

result = dfs(graph, start_node, goal_node)

if result:
    print("Path found:", result)
else:
    print("Goal not reached.")
