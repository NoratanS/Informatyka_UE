import java.util.ArrayList;
public class Kadane {
    public static int Kadane(int[] arr) {
        int maxEnding = arr[0];
        int result = arr[0];
        for (int i = 1; i < arr.length; i++) {
            maxEnding = Math.max(maxEnding + arr[i], arr[i]);
            result = Math.max(result, maxEnding);
        }
        return result;
    }
}


