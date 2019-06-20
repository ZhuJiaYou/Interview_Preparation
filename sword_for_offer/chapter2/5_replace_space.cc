#include <stdio.h>
#include <stdlib.h>


void replaceSpace(char *str,int length) {
	if(str == nullptr || length <= 0)
		return;
	int originalLen = 0;
	int numOfBlank = 0;
	int i = 0;
	while(str[i] != '\0')
	{
		++originalLen;
		if(str[i] == ' ')
			++numOfBlank;
		++i;
	}
	int newLen = originalLen + numOfBlank * 2;
	if(newLen > length)
		return;
	int indexOfOrigin = originalLen;
	int indexOfNew = newLen;
	while(indexOfOrigin >= 0 && indexOfNew > indexOfOrigin)
	{
		if(str[indexOfOrigin] == ' ')
		{
			str[indexOfNew--] = '0';
			str[indexOfNew--] = '2';
			str[indexOfNew--] = '%';
		}
		else
		{
			str[indexOfNew--] = str[indexOfOrigin];
		}
		--indexOfOrigin;
	}
}

int main(int argc, char* argv[])
{
	const int length = 100;
	char str[length] = "We Are Happy.";
	replaceSpace(str, length);
	printf("%s\n", str);

    return 0;
}


