/* Napisz program, który sprawdza, czy jeden łańcuch znaków może być
uzyskany poprzez cykliczne przesunięcie drugiego łańcucha. Oznacza to,
że ciąg znaków ”abcde” może być przekształcony na ”deabc” poprzez
kilka obrotów. Na przykład: dla ”abcdef” i ”defabc” program powinien
zwrócić true, natomiast dla ”abc” i ”acb” program zwróci false. */

import java.util.ArrayList;

public class prefix_task {
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
