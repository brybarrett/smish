defmodule SmishNode do
  def start(id), do: IO.puts("[#{id}] node started")
  def ping(peer), do: IO.puts("Pinging peer: #{peer}")
end

SmishNode.start("alpha")
SmishNode.ping("beta")
