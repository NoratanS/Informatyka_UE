public class zad4 {

    public static int[] combine_two_arrays(int[] arr1, int[] arr2) {
        int arr1_len = arr1.length;
        int arr2_len = arr2.length;
        int arr1_idx = 0;
        int arr2_idx = 0;
        int res_idx = 0;
        int[] res = new int[arr1_len + arr2_len];

        while (arr1_idx < arr1_len && arr2_idx < arr2_len) {
            if (arr1[arr1_idx] < arr2[arr2_idx]) {
                res[res_idx++] = arr1[arr1_idx++];
            }
            else {
                res[res_idx++] = arr2[arr2_idx++];
            }
        }

        while (arr1_idx < arr1_len) {
            res[res_idx++] = arr1[arr1_idx++];
        }

        while (arr2_idx < arr2_len) {
            res[res_idx++] = arr2[arr2_idx++];
        }

        return res;
    }
}
