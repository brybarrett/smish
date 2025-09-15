object SmishFiber {
  def attach(node: String): Unit = {
    println(s"Fiber attached to node: $node")
  }
  def drift(): Double = scala.util.Random.nextDouble()
}

object Main extends App {
  SmishFiber.attach("alpha")
}
