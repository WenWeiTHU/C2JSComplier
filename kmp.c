#include <stdio.h>

int getNext(char s[],int length,int next[]) {
	int j = -1;
	int len = length;

	next[0] = -1;

	for (int i=1;i < len; i++) {
		while(j >= 0 && s[j+1] != s[i]) {
			j = next[j];
		}

		if (s[j+1] == s[i]){
			j = j+1;
		}

		next[i] = j;
	}

	return 0;
}

int KMP(char P[],char T[]) {
	int n = strlen(T);
	int m = strlen(P);

	int next[100];
	getNext(P, m, next);

	int q = 0;

	// print next array
	printf("Next array: ");
	for (int i=0; i < m; i++) {
		printf("[%d]%d ", i, next[i]);
	}
	printf("\n");

    int flag = 0;
	for (int i=0; i < n; i++) {
		while (q >= 0 && P[q+1] != T[i]) {
			q = next[q];
		}

		if (P[q+1] == T[i]) {
			q = q+1;
		}

		if (q == m - 1) {
		    flag = 1;
			printf("Pattern occurs at %d\n", i-m+1);
			q = next[q];
		}
	}

	if(flag == 0){
	    printf("False\n");
	}

	return 0;
}

int main() {
	char P[100];
	char T[200];

    printf("Input pattern: ");
    gets(P);
    printf("Input text: ");
    gets(T);

    KMP(P,T);

	return 0;
}