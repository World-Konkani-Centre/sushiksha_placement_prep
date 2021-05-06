This repo is created for devlelopment purpose.

#include <stdio.h>
int main(void) {
	int t;
	int n;
	int arr[100];
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
	    scanf("%d",&n);
	    for(int i=0;i<n;i++)
	    {
	        scanf("%d",&arr[i]);
	    }
	    
	    int min = arr[0];
	    int idx = 0;
	    for(int i=1;i<n;i++){
	        if(arr[i]<min)
	        {
	            min = arr[i];
	            idx = i;
	        }
	    }
	    printf("%d",idx);
	}
	return 0;
}
