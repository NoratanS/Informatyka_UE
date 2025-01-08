import java.util.ArrayList;
import java.util.Random;

public class RandomGraph {
    ArrayList<Node> nodes = new ArrayList<>();
    ArrayList<Node> route = new ArrayList<>();
    static double cumDist = 0;

    public RandomGraph(int k, double xBound, double yBound) {
        Random rand = new Random();
        for (int i = 0; i < k; i++) {
            nodes.add(new Node(rand.nextDouble(0,   xBound), rand.nextDouble(0,   yBound)));
        }
    }

    public void SetRandomRoute() {
        Random rand = new Random();
        int selectedIdx = rand.nextInt(nodes.size());
        Node selectedNode = nodes.get(selectedIdx);
        route.add(selectedNode);
        nodes.remove(selectedIdx);

        while (!nodes.isEmpty()) {
            double minDist = route.getLast().CalculateDistance(nodes.getFirst());
            int minDistIdx = 0;
            for (int i = 1; i < nodes.size(); i++) {
                double currentDist = route.getLast().CalculateDistance(nodes.get(i));
                if (currentDist < minDist) {
                    minDist = currentDist;
                    minDistIdx = i;
                }
            }
            cumDist += minDist;
            route.add(nodes.get(minDistIdx));
            nodes.remove(minDistIdx);
        }
    }

    public void PrintNodes() {
        System.out.println("Nodes:");
        for (int i = 0; i < nodes.size(); i++) {
            System.out.println(nodes.get(i).toString());
        }
    }

    public void PrintRoute() {
        System.out.println("Route:");
        for (int i = 0; i < route.size(); i++) {
            System.out.println(route.get(i).toString());
        }
    }

    public void PrintRouteLength() {
        System.out.println("Route Length:");
        System.out.println(cumDist);
    }
}
