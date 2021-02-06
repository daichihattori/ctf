#include<stdio.h>
#include<gmp.h>
int isPrime(mpz_t a){
    if(mpz_probab_prime_p(a,25)==0){

        return 0;
    }
    return 1;
}
int is2Mod3(mpz_t a){
    mpz_mod()
}
int main(){
    return 0;
}