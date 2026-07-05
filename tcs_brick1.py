from collections import deque

def expand_row(row_str):
    """Expand compressed row format, e.g. '3R1D' -> ['R','R','R','D']"""
    expanded = []
    num = ""
    for ch in row_str:
        if ch.isdigit():
            num += ch
        else:
            count = int(num)
            expanded.extend([ch] * count)
            num = ""
    return expanded


def min_bricks_to_break(N, wall_input):
    wall = [expand_row(row) for row in wall_input]

    start = dest = None
    for i in range(N):
        for j in range(N):
            if wall[i][j] == 'S':
                start = (i, j)
            elif wall[i][j] == 'D':
                dest = (i, j)

    if not start or not dest:
        print("Error: Missing Source (S) or Destination (D) in input.")
        return -1

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque([(start[0], start[1], 0)])
    visited = [[False] * N for _ in range(N)]
    visited[start[0]][start[1]] = True

    while q:
        x, y, cost = q.popleft()
        if (x, y) == dest:
            return cost
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if wall[nx][ny] == 'G':
                    visited[nx][ny] = True
                    q.append((nx, ny, cost + 1))
                elif wall[nx][ny] == 'D':
                    return cost
    return -1


def main():
    try:
        lines = []
        print("Enter input (press Enter ):")
        while True:
            line = input().strip()
            if line == "":
                break
            lines.append(line)
    except EOFError:
        pass

    
    if not lines:
        print("\n using sample test case.\n")
        lines = [
            "4",
            "3R1D",
            "1R1R1R1G",
            "2G1G1G",
            "2S2R"
        ]

    N = int(lines[0])
    wall_input = lines[1:]
    result = min_bricks_to_break(N, wall_input)
    print("\nMinimum green bricks to break:", result)


if __name__ == "__main__":
    main()

