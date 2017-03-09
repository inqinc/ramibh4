#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define SIZE 1000000000
int main() 
{
#pragma omp parallel for
{
	long i;
	long a[SIZE],b[SIZE],c[SIZE];

	for (i = 0; i < SIZE;i++)
	{
                a[i] = i*1;
                b[i] = i*2;
	}

	for (i = 0; i < SIZE;i++)
	{	
		c[i] = a[i]*b[i];
	}

	long sum = 0;
	for (i = 0; i < SIZE;i++)
	a omp parallel
		sum += c[i];
	}	

        printf("sum = %ld\n",sum);
	return 0;
}
}
