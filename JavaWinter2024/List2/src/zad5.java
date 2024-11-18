public class zad5 {
    public static int[] zero_one_sort(int[] arr) {
        int zero_count = 0;

        for (int j : arr) {
            if (j == 0) {
                zero_count++;
            }
        }
        for (int i = 0; i < zero_count; i++) {
            arr[i] = 0;
        }
        for (int i = zero_count; i < arr.length; i++) {
            arr[i] = 1;
        }

        return arr;
    }
}
