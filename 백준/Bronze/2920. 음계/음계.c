#include<stdio.h>

int main()
{
	int arr[8] = { 1,2,3,4,5,6,7,8 };
	int arr2[8];
	int check;
	for (int i = 0; i < 8; i++)
		scanf("%d", &arr2[i]);
	
	for (int i = 0; i < 8; i++)
	{
		if (arr[i] != arr2[i])
		{
			check = 3;
			break;
		}
		check = 1;
	}
	if (check == 1)
	{
		printf("ascending");
		return 0;
	}
	for (int i = 0; i < 8; i++)
	{
		if (arr[i] != arr2[7 - i])
		{
			check = 3;
			break;
		}
		check = 2;
	}
	
	if (check == 2)
		printf("descending");
	else
		printf("mixed");

	return 0;
}	