#include <stdio.h>

void isPalindrome(char input[]) {
    int len = strlen(input);

	for (int i=0; i < len; i++) {
		if (input[i] != input[len-i-1]) {
			printf("False");
			return;
		}
	}

    printf("True");
    return;
}

int main() {
	char input[100];

	printf("input a string: ");
	gets(input);
	isPalindrome(input);
	printf("\n");

	return 0;
}