if __name__ == "__main__":
    n = int(input())
    outputGraph = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        inputGraph = list(map(int, input().split()))

        j = 2
        while j < len(inputGraph):
            outputGraph[i][inputGraph[j] - 1] = 1
            j += 1
    for i in range(n):
        print(*outputGraph[i])
