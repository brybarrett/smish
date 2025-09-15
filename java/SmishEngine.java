public class SmishEngine {
    private String nodeId;
    public SmishEngine(String nodeId) { this.nodeId = nodeId; }
    public void connect() { System.out.println("Connecting: " + nodeId); }
    public static void main(String[] args) {
        SmishEngine engine = new SmishEngine("alpha");
        engine.connect();
    }
}
