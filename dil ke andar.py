from collections import deque

# Goal state
Goal = "123456780"

# Possible moves for each position of the "0"
moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

# Function to find the neighbours of a given state
def neighbour(S):
    i = S.index("0")  # Find the index of the empty space "0"
    for j in moves[i]:  # For each possible move of "0"
        t = list(S)  # Convert the state to a list
        t[i], t[j] = t[j], t[i]  # Swap "0" with the adjacent tile
        yield "".join(t)  # Yield the new state as a string

# BFS or DFS search function to find the solution
def search(start, use_bfs=True):
    q = deque([start])  # Initialize the queue with the start state
    seen = {start}  # A set to track seen states to avoid revisiting
    parent = {start: None}  # To keep track of the parent of each state

    while q:
        S = q.popleft() if use_bfs else q.pop()  # Pop from front (BFS) or back (DFS)
        
        if S == Goal:
            # If we've reached the goal, reconstruct the solution path
            path = []
            while S != start:
                path.append(S)
                S = parent[S]
            path.append(start)  # Add the start state to the path
            path.reverse()
            return path
        
        for n in neighbour(S):
            if n not in seen:
                seen.add(n)
                parent[n] = S  # Record the parent of state n
                q.append(n)
    
    return None  # If no solution is found

# Function to display a state in a 3x3 grid format
def show(state):
    for i in range(0, 9, 3):
        print([int(x) for x in state[i:i+3]])

# Example usage
start = "123450678"
print("Initial state:")
show(start)

print("\nBFS Solution:")
bfs_solution = search(start, True)
if bfs_solution:
    for state in bfs_solution:
        show(state)
else:
    print("No solution found with BFS.")

print("\nDFS Solution:")
dfs_solution = search(start, False)
if dfs_solution:
    for state in dfs_solution:
        show(state)
else:
    print("No solution found with DFS.")
