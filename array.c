// Show Array could contain differrent data types
// Show Array as function parameter
void printArray(array arr){
  int length = lenA(arr);
  
  for(int i = 0; i < length; i++){
    // print elements of array, use %a in format string
    printf("%a\t", arr[i]);     
  }
}

// Show Array indexing and assignment
void reverseArray(array arr){
  // lenA: get an array's length 
  int length = lenA(arr);

  for(int i = 0; i < length/2; i++){
    int tmp = arr[i];
    arr[i] = arr[length-1-i];
    arr[length-1-i] = tmp;
  }
}

// Show Array as return value
// Show Array could assign without initialization with values
array genPrime(int n){
  array primeTable;
  array prime;
  int k = 0;

  for(int i=2; i<=n; i++){
      primeTable[i] = true; 
  }

  for(int i=2; i<=n; i++){
    if(primeTable[i]){
      for(int j=i+i; j<=n; j+=i){
        primeTable[j] = false;
      }
    }
  }

  for(int i=2; i<=n; i++){
    if(primeTable[i] == true){
      prime[k++] = i;
    }
  }

  return prime;
}

int main(){
    array test = {1, 2, 3, true, "hello", "world", '!'};
    
    printf("original: ");
    printArray(test);
    reverseArray(test);
    printf("\nreversed: ");
    printArray(test);

    int n = 100;
    printf("\nprimes <= %d: ", n);
    printArray(genPrime(n));
}

