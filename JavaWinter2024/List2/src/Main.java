import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        // zadanie Kadane
        int[] arr = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        int[] arr_pali = {1, 2, 3, 2, 1};
        int[] arr_zad4_1 = {1, 2, 3, 4, 5, 6};
        int[] arr_zad4_2 = {3, 4, 5, 6, 7};
        int[] arr_zad5 = {1,1,0,0,0,1,1,0,0,1,1,0};
        int[] arr_zad7 = {1,2,4,5,6};
        System.out.println(Kadane.Kadane(arr));
        System.out.println(Arrays.toString(zad1.reverse_arr(arr)));
        System.out.println(zad3.is_palindrome(arr_pali));
        System.out.println(Arrays.toString(zad4.combine_two_arrays(arr_zad4_1, arr_zad4_2)));
        System.out.println(Arrays.toString(zad5.zero_one_sort(arr_zad5)));
        System.out.println(zad7.missing_number(arr_zad7));


    }
}