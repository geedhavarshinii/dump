public class FloydsLoop {
    static class Node {
        int data;
        Node next;

        Node(int d) {
            data = d;
            next = null;
        }
    }

    Node head;

    void push(int new_data) {
        Node new_node = new Node(new_data);
        new_node.next = head;
        head = new_node;
    }

    void detectLoop() {
        Node slow = head, fast = head;
        while (slow != null && fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                System.out.println("Loop detected");
                return;
            }
        }
        System.out.println("No loop found");
    }

    public static void main(String[] args) {
        FloydsLoop list = new FloydsLoop();
        list.push(20);
        list.push(41);
        list.push(5);
        list.push(10);
        list.head.next.next.next.next = list.head;
        list.detectLoop();
    }
}