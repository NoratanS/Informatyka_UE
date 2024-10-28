import java.util.ArrayList;
public class Main {

    public static void main(String[] args) {
        // zad 1*
        //System.out.println(cycle_task.check_cycle("", ""));

        // zad 2*
        /*
        ArrayList<String> test = new ArrayList<String>();
        test.add("trawa");
        test.add("tratwa");
        test.add("tramwaj");
        System.out.println(prefix_task.find_prefix(test));
        */

        // zad 1
        String s1 = "abcdef";
        String s2 = "defe";
        System.out.println(zad1.my_compare_to(s1, s2));
        System.out.println(zad1.my_ends_with(s1, s2));
        System.out.println(zad1.my_index_of(s2, "e"));
        System.out.println(zad1.my_replace(s2, 'e', 'a'));

    }
}