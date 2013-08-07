#include <stdio.h>
#include <math.h>
#include <string.h>

#define N 800
int prime[N] = {
2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797
};
int prime_num_of_base[N];
int prime_num_of_factorial[N];
int prime_of_base[N];

int main() {
  long long n, b, tb;
  long long min, i, ti, j, k;
  long long zeroNum;
  double dsum;
  double digitNum;

  while (scanf ("%lld%lld", &n, &b) != EOF) {
    memset (prime_num_of_factorial, 0, sizeof(int)*N);
    memset (prime_num_of_base, 0, sizeof(int)*N);

    /* find prime factor of base */
    tb = b;
    i = j = 0;
    while (prime[i] != 797) {
      if (tb % prime[i] == 0) {
        prime_of_base[j] = prime[i];
        while (tb % prime[i] == 0) {
          tb /= prime[i];
          prime_num_of_base[j]++;
        }
        j++;
      }
      i++;
    }

    /* calculate trailing zero */
    for (i=1; i<=n; i++) {
      k = 0; ti=i;
      while (k < j) {
        while (ti%prime_of_base[k] == 0) {
          prime_num_of_factorial[k]++;
          ti /= prime_of_base[k];
        }
        k++;
      }
    }

    min = prime_num_of_factorial[0]/prime_num_of_base[0];
    for (k=1; k<j; k++)
      if (prime_num_of_factorial[k]/prime_num_of_base[k] < min) 
        min = prime_num_of_factorial[k]/prime_num_of_base[k];

    zeroNum = min;

    /* calculate digit number */
    dsum = 0;
    for (i=1; i<=n; i++)
      dsum += log10(i);
    digitNum = (dsum/log10(b)) ;

    if (digitNum - floor(digitNum) < 1e-10)
        digitNum ++;
    else
        digitNum = floor(digitNum + 1);
    

    printf ("%lld %.0f\n", zeroNum, digitNum);
  }

  return 0;
}
