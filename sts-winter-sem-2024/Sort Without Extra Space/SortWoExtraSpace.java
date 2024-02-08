import java.util.LinkedList;
import java.util.Queue;

public class SortWoExtraSpace {
    private static void SortQueue(Queue queue) {
        int n = queue.size();
        for (int i = 0; i < n; i++) {
            int minIndex = -1;
            int minValue = Integer.MAX_VALUE;
            for (int j = 0; j < n; j++) {
                int currValue = queue.poll();
                if (currValue < minValue && j < (n - i)) {
                    minValue = currValue;
                    minIndex = j;
                }
                queue.add(currValue);
            }
            for (int j = 0; j < n; j++) {

            }
        }
    }
}
