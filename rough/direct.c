#include<stdio.h>
#include<conio.h>

void createadjmatrix(int Adj[50][50],int arr[50][2],int v,int e)
{
	int i=0,j=0;
	for(i=1;i<=v;i++)
	{
		for(j=1;j<=v;j++)
		Adj[i][j]=0;
	}

	for(i=0;i<e;i++)
	{
		int x=arr[i][0];
		int y=arr[i][1];
		Adj[x][y]=1;
		//Adj[y][x]=1;
	}

}

void printadjmatrix(int Adj[50][50],int v)
{
	int i=0,j=0;
	for (i=1;i<=v;i++)
	{
		for(j=1;j<=v;j++)
		{
			printf("%d",Adj[i][j]);

		}
		printf("\n");
	}
}

void main()
{
	int v=0,i=0,j=0,e=0;
	int arr[5][2];
	int Adj[50][50];
	clrscr();
	printf("ENTER THE NO. OF VERTICES AND EDGES:");
	scanf("%d%d",&v,&e);

	printf("ENTER THE PATH");
	for(i=0;i<e;i++)
	{
		for(j=0;j<2;j++)
		scanf("%d",&arr[i][j]);
		printf("\n");
	}

createadjmatrix(Adj,arr,v,e);
printadjmatrix(Adj,e);
getch();
}