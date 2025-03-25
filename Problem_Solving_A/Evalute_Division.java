import java.util.*;

public class Solution {  // ✅ Rename the class to "Solution" as expected by the driver

    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        Map<String, Map<String, Double>> graph = new HashMap<>();

        // Build the graph
        for (int i = 0; i < equations.size(); i++) {
            String A = equations.get(i).get(0);
            String B = equations.get(i).get(1);
            double value = values[i];

            graph.putIfAbsent(A, new HashMap<>());
            graph.putIfAbsent(B, new HashMap<>());

            graph.get(A).put(B, value);
            graph.get(B).put(A, 1.0 / value);
        }

        double[] results = new double[queries.size()];

        for (int i = 0; i < queries.size(); i++) {
            String C = queries.get(i).get(0);
            String D = queries.get(i).get(1);

            if (!graph.containsKey(C) || !graph.containsKey(D)) {
                results[i] = -1.0;
            } else if (C.equals(D)) {
                results[i] = 1.0;
            } else {
                Set<String> visited = new HashSet<>();
                results[i] = dfs(graph, C, D, visited, 1.0);
            }
        }

        return results;
    }

    private double dfs(Map<String, Map<String, Double>> graph, String current, String target, Set<String> visited, double value) {
        if (current.equals(target)) {
            return value;
        }

        visited.add(current);

        for (Map.Entry<String, Double> neighbor : graph.get(current).entrySet()) {
            String next = neighbor.getKey();
            double weight = neighbor.getValue();

            if (!visited.contains(next)) {
                double result = dfs(graph, next, target, visited, value * weight);
                if (result != -1.0) {
                    return result;
                }
            }
        }

        return -1.0;
    }

    // ✅ Main function to test
    public static void main(String[] args) {
        Solution solution = new Solution();

        // Test case 1
        List<List<String>> equations1 = Arrays.asList(
                Arrays.asList("a", "b"),
                Arrays.asList("b", "c")
        );
        double[] values1 = {2.0, 3.0};
        List<List<String>> queries1 = Arrays.asList(
                Arrays.asList("a", "c"),
                Arrays.asList("b", "a"),
                Arrays.asList("a", "e"),
                Arrays.asList("a", "a"),
                Arrays.asList("x", "x")
        );

        System.out.println(Arrays.toString(solution.calcEquation(equations1, values1, queries1)));
        // ➝ [6.0, 0.5, -1.0, 1.0, -1.0]

        // Test case 2
        List<List<String>> equations2 = Arrays.asList(
                Arrays.asList("a", "b"),
                Arrays.asList("b", "c"),
                Arrays.asList("bc", "cd")
        );
        double[] values2 = {1.5, 2.5, 5.0};
        List<List<String>> queries2 = Arrays.asList(
                Arrays.asList("a", "c"),
                Arrays.asList("c", "b"),
                Arrays.asList("bc", "cd"),
                Arrays.asList("cd", "bc")
        );

        System.out.println(Arrays.toString(solution.calcEquation(equations2, values2, queries2)));
        // ➝ [3.75, 0.4, 5.0, 0.2]

        // Test case 3
        List<List<String>> equations3 = Arrays.asList(
                Arrays.asList("a", "b")
        );
        double[] values3 = {0.5};
        List<List<String>> queries3 = Arrays.asList(
                Arrays.asList("a", "b"),
                Arrays.asList("b", "a"),
                Arrays.asList("a", "c"),
                Arrays.asList("x", "y")
        );

        System.out.println(Arrays.toString(solution.calcEquation(equations3, values3, queries3)));
        // ➝ [0.5, 2.0, -1.0, -1.0]
    }
}