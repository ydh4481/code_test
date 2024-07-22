#include<stdio.h>
#include<memory.h>

int main()
{
	int arr[10];
	int arr2[10] = { 42,42,42,42,42,42,42,42,42,42 };
	int i, j = 0 , k = 0;
	int cnt, max;

	for (i = 0; i < 10; i++)
	{
		scanf("%d", &j);
		arr[i] = j % 42;
	}
	
	arr2[0] = arr[0];

	for (i = 0; i < 10; i++)
	{
		cnt = 0;
		for (j = 0; j < 10; j++)
			if (arr[i] != arr2[j])
				cnt++;
		if (cnt == 10)
			arr2[++k] = arr[i];
	}
	cnt = 0;
	for (i = 0; i < 10; i++)
	{
		if (arr2[i] != 42)
			cnt++;
	}

	printf("%d", cnt);
	return 0;
}	