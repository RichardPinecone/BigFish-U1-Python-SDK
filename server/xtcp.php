<?php
$server = new swoole_server("101.200.151.218", 9500);
$server->on('connect', function ($server, $fd){
    echo "connection open: {$fd}\n";
});
$server->on('receive', function ($server, $fd, $reactor_id, $data) {
    echo "recved {$data}\n";
    $server->send($fd, "Server Echo: {$data}");
});
$server->on('close', function ($server, $fd) {
    echo "connection close: {$fd}\n";
});

$server->start();
?>
