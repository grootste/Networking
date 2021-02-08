#include <iostream>
using namespace std;

struct node
{
    int dist[20];
    int from[20];
}routing[10];

int main()
{

    int cost[20][20];
    int n, i , j, k, count= 0;
    cin>>n;
    cin>>"Enter the cost matrix of nodes in the network";
    for(i= 0; i< n; i++)
        for(i= 0; i< n; i++)
    {
        cin>>cost[i][j];
        cost[i][i]=0;
       routing[i].dist[j]=cost[i][j];
            routing[i].from[j]=j;
        }
    }
        do
        {
            count=0;
            for(i=0;i<n;i++)
            for(j=0;j<n;j++)
            for(k=0;k<n;k++)
                if(routing[i].dist[j]>cost[i][k]+routing[k].dist[j])
                {
                    routing[i].dist[j]=routing[i].dist[k]+routing[k].dist[j];
                    routing[i].from[j]=k;
                    count++;
                }
        }while(count!=0);
        for(i=0;i<n;i++)
        {
            printf("\n\n For router %d\n",i+1);
            for(j=0;j<n;j++)
            {
                printf("\t\nnode %d via %d Distance %d ",j+1,routing[i].from[j]+1,routing[i].dist[j]);
            }
        }
    printf("\n\n");
    getch();
}
