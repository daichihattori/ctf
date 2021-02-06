#include<stdio.h>
#include<gmp.h>
#define cipher_text_str "2205316413931134031074603746928247799030155221252519872650073010782049179856976080512716237308882294226369300412719995904064931819531456392957957122459640736424089744772221933500860936331459280832211445548332429338572369823704784625368933"

int main(){
    mpz_t cipher_text,message,rem;
    int e=3;

    mpz_init(cipher_text);
    mpz_init(message);
    mpz_init(rem);
    mpz_set_str(cipher_text,cipher_text_str,10);

    mpz_rootrem(message,rem,cipher_text,3);
    gmp_printf("message: %Zx\n",message);
    gmp_printf("rem: %Zd\n",rem);


    mpz_t debug;
    mpz_init(debug);
    mpz_pow_ui(debug,message,3);
    int flag=mpz_cmp(debug,cipher_text);


    //flag = mpz_perfect_power_p(cipher_text);
    printf("flag=%d",flag);
    return 0;
}