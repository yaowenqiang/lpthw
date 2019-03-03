<?php
    $client = new Redis();
    $client->connect('localhost', 6379);
    print_r(Redis::PIPELINE);
    $client->multi(Redis::PIPELINE)
            ->set('aaa','bbb')
            ->set('ccc','ddd')
            ->exec();
?>
