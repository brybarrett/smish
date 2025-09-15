using System;
public class SmishAgent {
    public string Id { get; set; }
    public SmishAgent(string id) { Id = id; }
    public void Handshake(string peer) {
        Console.WriteLine($"[{Id}] handshaking with {peer}");
    }
    public static void Main() {
        var agent = new SmishAgent("alpha");
        agent.Handshake("beta");
    }
}
