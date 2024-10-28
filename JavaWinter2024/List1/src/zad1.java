/* Zapisz własne wersje poniższych metod.
int compareTo(String anotherString) – porównanie dwóch
łańcuchów : 0 równe. wart. ujemna - String mniejszy od zadanego,
np. aaa i aab; wart. dodatnia - String większy od zadanego;
boolean endsWith (String suffix) – podajemy łańcuch i sprawdzamy,
czy kończy się na wybrany podłańcuch/literę;
int indexOf(String str) – udostępnia miejsce wystąpienia
podłańcucha str w łańcuchu;
String replace (char oldChar, char newChar);
String substring (int beginindex) – udostępnia podciąg danego
łańcucha od wybranego indeksu do końca. */


public class zad1 {

    // Returns length of the shorter string
    public static int find_shorter_len(String s1, String s2) {
        if (s1.length() < s2.length()){
            return s1.length();
        }
        return s2.length();
    }


    public static int my_compare_to(String s1, String s2) {
        // comparing characters
        for (int i = 0; i < find_shorter_len(s1, s2); i++) {
            if (s1.charAt(i) > s2.charAt(i)){
                return 1;
            }
            else if (s1.charAt(i) < s2.charAt(i)){
                return -1;
            }
        }

        // if one word is a prefix of the other we check for lengths
        if (s1.length() == s2.length()){
            return 0;
        }
        else if (s1.length() > s2.length()){
            return 1;
        }
        else return -1;
    }

    public static boolean my_ends_with(String s, String suff) {
        int s_len = s.length();
        int suff_len = suff.length();

        if (suff_len > s_len){
            return false;
        }

        for (int i = 0; i < suff_len; i++) {
            if (s.charAt(s_len - suff_len + i) != suff.charAt(i)){
                return false;
            }
        }
        return true;
    }

    public static int my_index_of(String s, String sub) {
        if (sub.length() > s.length()){
            return -1;
        }

        int pos = -1; // stores current sub_string position
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == sub.charAt(0)){  // if we step on a char equal to start of sub we set the position to i
                pos = i;
                for (int j = 1; j < sub.length(); j++) { // check rest of sub
                    if (s.charAt(i + j) != sub.charAt(j)){ // if we step on a different char reset position and stop checking
                        pos = -1;
                        break;
                    }
                }
                if (pos != -1) { // if we didn't reset position it means we found it
                    return pos;
                }
            }
        }

        return -1;
    }

    public static String my_replace(String s, Character old_c, Character new_c) {
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == old_c){
                res.append(new_c);
            }
            else {
                res.append(s.charAt(i));
            }
        }
        return res.toString();
    }
}