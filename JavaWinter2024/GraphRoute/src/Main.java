public class Main {
    public static void main(String[] args) {
        RandomGraph ex1 = new RandomGraph(10, 10, 10);
        ex1.PrintNodes();
        ex1.SetRandomRoute();
        ex1.PrintRoute();
        ex1.PrintRouteLength();
    }
}