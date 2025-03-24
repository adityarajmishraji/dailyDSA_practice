#include <stdio.h>

#define MAX 10

void accept_graph(int G[][MAX], int n) {
    int i, j;
    printf("\nEnter adjacency matrix (0 for no edge, 1 for edge):\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            printf("Edge (V%d, V%d) exists? (Yes=1, No=0): ", i, j);
            scanf("%d", &G[i][j]);

            // Ensure the user does not input invalid values
            while (G[i][j] != 0 && G[i][j] != 1) {
                printf("Invalid input! Enter 1 for edge, 0 for no edge: ");
                scanf("%d", &G[i][j]);
            }
        }
    }
}

void disp_adj_mat(int G[][MAX], int n) {
    int i, j;
    printf("\nAdjacency Matrix:\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            printf("%3d", G[i][j]);
        }
        printf("\n");
    }
}

void calc_degree(int G[][MAX], int n) {
    int i, j, insum, outsum, totsum;

    printf("\nDegree of Graph:\n");
    printf("Vertex | In-Degree | Out-Degree | Total Degree\n");
    printf("-----------------------------------------------\n");

    for (i = 0; i < n; i++) {
        insum = 0;
        outsum = 0;

        for (j = 0; j < n; j++) {
            insum += G[j][i];  // Count incoming edges
            outsum += G[i][j]; // Count outgoing edges
        }

        totsum = insum + outsum; // Total degree
        printf("  V%-3d |     %-6d |     %-8d |      %-6d\n", i, insum, outsum, totsum);
    }
}

int main() {
    int G[MAX][MAX], n;

    printf("Enter number of vertices: ");
    scanf("%d", &n);

    // Check if n exceeds MAX
    if (n > MAX) {
        printf("Error: Number of vertices exceeds MAX (%d).\n", MAX);
        return 1;
    }

    accept_graph(G, n);
    disp_adj_mat(G, n);
    calc_degree(G, n);

    return 0;
}


// Input as:
// Enter number of vertices: 4

// Enter adjacency matrix (0 for no edge, 1 for edge):
// Edge (V0, V0) exists? (Yes=1, No=0): 1
// Edge (V0, V1) exists? (Yes=1, No=0): 0
// Edge (V0, V2) exists? (Yes=1, No=0): 1
// Edge (V0, V3) exists? (Yes=1, No=0): 1
// Edge (V1, V0) exists? (Yes=1, No=0): 1
// Edge (V1, V1) exists? (Yes=1, No=0): 1
// Edge (V1, V2) exists? (Yes=1, No=0): 1
// Edge (V1, V3) exists? (Yes=1, No=0): 1
// Edge (V2, V0) exists? (Yes=1, No=0): 0
// Edge (V2, V1) exists? (Yes=1, No=0): 0
// Edge (V2, V2) exists? (Yes=1, No=0): 1
// Edge (V2, V3) exists? (Yes=1, No=0): 0
// Edge (V3, V0) exists? (Yes=1, No=0): 0
// Edge (V3, V1) exists? (Yes=1, No=0): 1
// Edge (V3, V2) exists? (Yes=1, No=0): 0
// Edge (V3, V3) exists? (Yes=1, No=0): 01

// Output:

// Adjacency Matrix:
//   1  0  1  1
//   1  1  1  1
//   0  0  1  0
//   0  1  0  1

// Degree of Graph:
// Vertex | In-Degree | Out-Degree | Total Degree
// -----------------------------------------------
//   V0   |     2      |     3        |      5     
//   V1   |     2      |     4        |      6     
//   V2   |     3      |     1        |      4     
//   V3   |     3      |     2        |      5 