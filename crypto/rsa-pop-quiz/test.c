#include<stdio.h>
#include<gmp.h>
void rsa_crypto(mpz_t ans,mpz_t a,mpz_t e,mpz_t n){
    mpz_powm(ans,a,e,n);
}
void rsa_decrypto(mpz_t ans,mpz_t a,mpz_t d,mpz_t n){
    mpz_powm(ans,a,d,n);
}
int main(){
    //n set
    //char n_char[10000]="12738162802910546503821920886905393316386362759567480839428456525224226445173031635306683726182522494910808518920409019414034814409330094245825749680913204566832337704700165993198897029795786969124232138869784626202501366135975223827287812326250577148625360887698930625504334325804587329905617936581116392784684334664204309771430814449606147221349888320403451637882447709796221706470239625292297988766493746209684880843111138170600039888112404411310974758532603998608057008811836384597579147244737606088756299939654265086899096359070667266167754944587948695842171915048619846282873769413489072243477764350071787327913";
    char n_char[10000]="187";
    mpz_t n;
    mpz_init(n);
    mpz_set_str(n,n_char,10);
    gmp_printf("n=%Zd\n",n);

    //e set
    mpz_t e;
    mpz_init(e);
    mpz_set_ui(e,3);

    //message
    mpz_t m;
    mpz_init(m);
    mpz_set_ui(m,2);

    //crypto
    rsa_crypto(m,m,e,n);
    gmp_printf("m=%Zd\n",m);

    //decrypto
    mpz_t d;
    mpz_init(d);
    mpz_invert(d,e,n);
    gmp_printf("d=%Zd\n",d);
    rsa_decrypto(m,m,d,n);
    gmp_printf("m=%Zd\n",m);

    //decrypto test
    mpz_t d_true;
    mpz_t nn;

    mpz_init(d_true);
    mpz_init(nn);
    mpz_set_ui(nn,160);

    mpz_invert(d_true,e,nn);
    gmp_printf("d_true=%Zd\n",d_true);
    rsa_decrypto(m,m,d_true,n);
    gmp_printf("m=%Zd\n",m);

    return 0;
}