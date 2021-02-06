import java.util.*;

class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
	String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
    System.out.println(input);
    vaultDoor.reversePassword();

	if (vaultDoor.checkPassword(input)) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
        }
    }

    // Our security monitoring team has noticed some intrusions on some of the
    // less secure doors. Dr. Evil has asked me specifically to build a stronger
    // vault door to protect his Doomsday plans. I just *know* this door will
    // keep all of those nosy agents out of our business. Mwa ha!
    //
    // -Minion #2671
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];

        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        //i=8
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        System.out.println(buffer);
        return s.equals("jU5t_a_sna_3lpm18gb41_u_4_mfr340");
        //jU5t_a_slmpl3_an _4u__m1f4rb3g480
        //jU5t_a_sna_3lpml 84g_bm4f1r_3u4_0
        //jU5t_a_slmpl3_an 4
        //jU5t_a_sna_3lpm1 8gb41_u_4_mfr340
        //jU5t_a_slmpl3_an_4u__m1f4rb3g480
        //_4u__m1f4rb3g480
        //jU5t_a_s
        //na_3lpm1
        //8gb41_u_4_mfr340
        //
    }
    public void reversePassword() {
        String password="jU5t_a_sna_3lpm18gb41_u_4_mfr340";
        char[] buffer = new char[32];

        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        //i=8
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            //buffer[i] = password.charAt(46-i);
            buffer[46-i]=password.charAt(i);
        }
        for (i=31; i>=17; i-=2) {
            //buffer[i] = password.charAt(i);
            buffer[i] = password.charAt(i);

        }
        String s = new String(buffer);
        System.out.println(buffer);
        //return s.equals("jU5t_a_sna_3lpm18gb41_u_4_mfr340");
        //jU5t_a_slmpl3_an _4u__m1f4rb3g480
        //jU5t_a_sna_3lpml 84g_bm4f1r_3u4_0
        //jU5t_a_slmpl3_an 4
        //jU5t_a_sna_3lpm1 8gb41_u_4_mfr340
        //jU5t_a_slmpl3_an_4u__m1f4rb3g480
        //_4u__m1f4rb3g480
        //jU5t_a_s
        //na_3lpm1
        //8gb41_u_4_mfr340
        //
    }
}