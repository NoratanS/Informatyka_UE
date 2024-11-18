public class zad7 {
    public static int missing_number(int[] arr){
        for (int i = 0; i < arr.length; i++) {
            if (i + 1 != arr[i])
                return i+1;
        }
        return -1;
    }
}
