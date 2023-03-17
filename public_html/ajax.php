<?php
require_once $_SERVER['DOCUMENT_ROOT'].'/php_interface/header.php';
global $basket;
$type = htmlspecialchars($_GET['type']);

switch ($type){
    case 'addCart':
        $res = $basket->addCart(htmlspecialchars($_GET['id']));
        $basket->setBasket();
        ?>
        <table>
            <?foreach ($basket->getBasket() as $item):?>
                <tr>
                    <th><?=$item['name']?> руб</th>
                    <td><?=$item['price']?> руб</td>
                </tr>
            <?endforeach;?>
        </table>
        <?php
        break;
    case 'createOrder':
        $res = $basket->createOrder();
        break;
    default:
        break;
}