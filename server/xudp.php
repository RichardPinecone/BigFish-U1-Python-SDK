<?php
$server = new swoole_server("101.200.151.218", 9500, SWOOLE_PROCESS, SWOOLE_SOCK_UDP);
$server->on('Packet', function ($server, $data, $clientInfo) {
    echo "recved {$data}\n";
    $server->sendto($clientInfo['address'], $clientInfo['port'], "Server ".$data);
    var_dump($clientInfo);
});

$server->start();
?>
