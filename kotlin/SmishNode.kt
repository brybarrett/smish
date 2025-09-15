class SmishNode(val id: String) {
    fun probe(signal: String): Double {
        println("[$id] probing $signal")
        return signal.length * 0.01
    }
}

fun main() {
    val node = SmishNode("alpha")
    node.probe("init")
}
