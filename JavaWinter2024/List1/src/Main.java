import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        System.out.println(check_cycle("", ""));
        ArrayList<String> test = new ArrayList<String>();
        test.add("trawa");
        test.add("tratwa");
        test.add("tramwaj");
        System.out.println(find_prefix(test));

    }


    public static Boolean check_cycle(String a, String b){
        if (a.length() != b.length()) return false;
        ArrayList<Character> a_l = new ArrayList<Character>();
        for (int i = 0; i < a.length(); i++) {
            a_l.add(a.charAt(i));
        }

        for (int i = 1; i < a_l.size(); i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = 0 ; j < a_l.size(); j++) {
                sb.append(a_l.get((j + i) % a_l.size()));
            }
            if (sb.toString().equals(b)) return true;
        }
        return false;
    }

    public static String find_shortest(ArrayList<String> words){
        String min = words.getFirst();
        for (int i = 1; i < words.size(); i++) {
            if (words.get(i).length() < min.length()) {
                min = words.get(i);
            }
        }
        return min;
    }

    public static String find_prefix(ArrayList<String> words){
       String shortest = find_shortest(words);

       StringBuilder sb = new StringBuilder();
       Boolean flag;
       for (int i = 0; i < shortest.length(); i++) {
           flag = true;
           for (int j = 0; j < words.size(); j++) {
               if (words.get(j).charAt(i) != shortest.charAt(i)) {
                   flag = false;
               }
           }
           if (flag) {
               sb.append(shortest.charAt(i));
           }
           else {
               break;
           }
       }
       return sb.toString();
    }
}