#include <stdio.h>
#include <stdlib.h>

void input(int arr[10][2], int m) {
    int i;
    for (i = 0; i < m; i++) {
        printf("Enter edge %d (u v): ", i + 1);
        scanf("%d %d", &arr[i][0], &arr[i][1]);
    }
}

void Arr(int arr[10][2], int m) {
    int i;
    printf("\nEdges entered:\n");
    for (i = 0; i < m; i++) {
        printf("%d - %d\n", arr[i][0], arr[i][1]);
    }
}

void createAdjM(int Adj[10][10], int arr[][2], int n, int m) {
    int i, j;

    // Initialize adjacency matrix with 0
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            Adj[i][j] = 0;
        }
    }

    // Fill adjacency matrix based on edges
    for (i = 0; i < m; i++) {
        int x = arr[i][0];
        int y = arr[i][1];

        if (x < n && y < n) {  // Prevent out-of-bounds errors
            Adj[x][y] = 1;
            Adj[y][x] = 1;  // Since it's an undirected graph
        }
    }
}

void printM(int a[10][10], int n) {
    int i, j;
    printf("\nAdjacency Matrix:\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            printf("%d  ", a[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int n, m;
    int arr[10][2];
    int Adj[10][10];

    printf("Enter number of vertices: ");
    scanf("%d", &n);
    printf("Enter number of edges: ");
    scanf("%d", &m);

    input(arr, m);
    createAdjM(Adj, arr, n, m);
    Arr(arr, m);
    printM(Adj, n);

    return 0;
}

//example Input and output:

// Enter number of vertices: 3
// Enter number of edges: 2
// Enter edge 1 (u v): 4
// 3
// Enter edge 2 (u v): 2
// 1

// Edges entered:
// 4 - 3
// 2 - 1

// Adjacency Matrix:
// 0  0  0  
// 0  0  1  
// 0  1  0  