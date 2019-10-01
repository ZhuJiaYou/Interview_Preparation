#include <stdio.h>
#include <stdlib.h>

int coinChange(int* coins, int coinsSize, int amount){
	int min_changes[amount+1];
	min_changes[0] = 0;
	for (int i=1; i<=amount; ++i)
	{
	     min_changes[i] = amount + 1;
	}

	for (int i=1; i<=amount; ++i)
	{
	    for (int j=0; j<coinsSize; ++j)
		{
		     if ((i-coins[j]>=0) && (min_changes[i]>min_changes[i-coins[j]]+1))
		     min_changes[i] = min_changes[i-coins[j]] + 1;
		}
	}

	if (min_changes[amount] <= amount)
	    return min_changes[amount];
	else
		return -1;
}

int main()
{
	int coins[3] = {1, 2, 5};
	printf("%d\n", coinChange(coins, 3, 11));

	return 0;
}
