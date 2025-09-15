class SmishGateway
  def initialize(id); @id = id; end
  def route(message); puts "[#{@id}] routing: #{message}"; end
end

if __FILE__ == $0
  gateway = SmishGateway.new("alpha")
  gateway.route("hello future mesh")
end
