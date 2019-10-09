#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int longestSubstring(char *s, int k){
	return search(s, 0, strlen(s)-1, k);

}

int search(char *s, int low, int high, int k)
{
	int mp[26] = {0};
	for (int i=low; i<=high; ++i)
		++mp[s[i]-'a'];

	int flag = 1;
	for (int i=0; i<26&&flag==1; ++i)
		if (mp[i]>0 && mp[i]<k)
		{
			flag = 0;
			break;
		}
	
	if (flag == 1)
		return high-low+1;

	int i=low, max_dist=0;
	for (int j=low; j<=high; ++j)
	{
		if (mp[s[j]-'a']>0 && mp[s[j]-'a']<k)
		{
			flag = search(s, i, j-1, k);
			if (flag > max_dist)
				max_dist = flag;
			i = j + 1;
		}
	}

	flag = search(s, i, high, k);
	return max_dist >= flag ? max_dist : flag;
}

int main()
{
	char *s = "aaabb";
	printf("%d\n", longestSubstring(s, 3));

	return 0;
}
