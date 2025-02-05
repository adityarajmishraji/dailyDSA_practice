#include<stdio.h>
// #include<conio.h>
#define MAX 10

void accept_graph(int G[][MAX], int n)
{
	int i,j;
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			printf("Edge (V%d,V%d) exists? (Yes=1, No=0):",i,j);
			scanf("%d",&G[i][j]);
		  }
	}
}
void disp_adj_mat(int G[][MAX], int n)
{
	int i,j;
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)

		{
			printf("%4d",G[i][j]);
		 }
		 printf("\n");
	  }
}
void calc_degree(int G[][MAX], int n)
{
	int i,j,insum,outsum,totsum;
	for(i=0;i<n;i++)
	{
		insum=0;outsum=0;totsum=0;
		for(j=0;j<n;j++)
		{
			insum=insum+G[j][i];
			outsum=outsum+G[i][j];
			totsum=insum+outsum;
		 }
		 printf("(V%d)=%d\t%d\t%d\n",i,insum,outsum,totsum);
	 }
}
void main()
{
	int G[MAX][MAX],n;
    // clrscr();
	printf("Enter no.of vertices:");
	scanf("%d",&n);
	accept_graph(G,n);
	printf("Adjacency Matrix:\n");
	disp_adj_mat(G,n);
	printf("Degree of graphs:\n");
	printf("Ver=In\tOut\tTot\n");
	calc_degree(G,n);
	// getch();
}