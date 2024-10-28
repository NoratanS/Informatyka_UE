/*
Napisz program, który znajdzie najdłuższy wspólny prefiks dla zestawu
łańcuchów znaków. Prefiks to początkowa część łańcucha, która jest taka
sama dla wszystkich łańcuchów w zbiorze. Na przykład: dla tablicy
łańcuchów ”trawa”, ”tratwa”, ”tramwaj” program powinien zwrócić
”tra”.
 */

import java.util.ArrayList;

public class cycle_task {
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
}
