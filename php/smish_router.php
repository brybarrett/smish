<?php
class SmishRouter {
    private $id;
    function __construct($id) { $this->id = $id; }
    function send($msg) {
        echo "[" . $this->id . "] sending: " . $msg . PHP_EOL;
    }
}
$router = new SmishRouter("alpha");
$router->send("hello future mesh");
?>
