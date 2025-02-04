#include <stdio.h>

void createAdjMatrix(int Adj[50][50], int earr[50][2], int v, int e) {
    int i, j;
    
    // Initialize adjacency matrix with 0
    for(i = 0; i < v; i++) {
        for(j = 0; j < v; j++) {
            Adj[i][j] = 0;
        }
    }

    // Fill adjacency matrix using edge list
    for(i = 0; i < e; i++) {
        int x = earr[i][0];
        int y = earr[i][1];
        Adj[x][y] = 1;
        Adj[y][x] = 1;  // Since it's an undirected graph
    }
}

void printAdjMatrix(int Adj[50][50], int v) {
    int i, j;
    
    printf("Adjacency Matrix:\n");
    for(i = 0; i < v; i++) {
        for(j = 0; j < v; j++) {
            printf("%d ", Adj[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int v, e, i, j;
    int earr[50][2];
    int Adj[50][50];

    printf("Enter the number of vertices & edges: ");
    scanf("%d %d", &v, &e);

    printf("Enter the edges (u v):\n");
    for(i = 0; i < e; i++) {
        scanf("%d %d", &earr[i][0], &earr[i][1]);
    }

    // Create and print adjacency matrix
    createAdjMatrix(Adj, earr, v, e);
    printAdjMatrix(Adj, v);

    return 0;
}
// Sample input and expected out put

// Enter the number of vertices & edges: 4 3
// Enter the edges (u v):
// 0 1
// 1 2
// 2 1
// Adjacency Matrix:
// 0 1 0 0 
// 1 0 1 0 
// 0 1 0 0 
// 0 0 0 0 