<?php
require_once $_SERVER['DOCUMENT_ROOT'].'/php_interface/header.php';
?>
<!doctype html>
<html lang="en">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=yes">
    <meta http-equiv="Content-type" content="text/html;charset=UTF-8">
    <title>IMPOSTER SHOP</title>
    <link rel="stylesheet" type="text/css" href="https://js.api.here.com/v3/3.1/mapsjs-ui.css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jquery-modal/0.9.1/jquery.modal.min.css" />
    <link rel="stylesheet" type="text/css" href="/assets/css/style.css?get=<?=time()?>" />
    <link rel="stylesheet" type="text/css" href="/assets/css/map.css?get=<?=time()?>" />
    <link rel="stylesheet" type="text/css" href="/assets/css/modal.css?get=<?=time()?>" />
</head>
<body id="markers-on-the-map">
    <header>
        <div class="container">
            <img class="logo" src="/assets/img/logo.png">
            <div class="search">
                <input class="search-input" placeholder="Поиск...">
            </div>
            <div class="nav">
                <div class="profile"><img src="/assets/img/profile.png" alt="профиль"></div>
                <a href="#ex1" rel="modal:open"><div class="basket"><img src="/assets/img/basket.png" alt="корзина"></div></a>
            </div>
        </div>
    </header>
    <main>
        <div class="banner">
            <img class="img" src="/assets/img/26250.png" alt="картинка">
        </div>
        <ul>
        </ul>
        <div id="map" class="map">
        </div>
    </main>
    <footer>
        <span class="tula-hack-tag">#TulaHack2020</span>
        <img class="telegram-icon" src="assets/img/telegram-icon.png">
    </footer>
    <div id="ex1" class="modal">
        <h3 class ="text">Корзина</h3>
        <div class="vp">
            <table>
                <?foreach ($basket->getBasket() as $item):?>
                    <tr>
                        <th><?=$item['name']?> руб</th>
                        <td><?=$item['price']?> руб</td>
                    </tr>
                <?endforeach;?>
            </table>
        </div>
        <div class="checkout"><button id ="check">Оформить заказ</button></div>
    </div>
    <script type="text/javascript" src="https://js.api.here.com/v3/3.1/mapsjs-core.js"></script>
    <script type="text/javascript" src="https://js.api.here.com/v3/3.1/mapsjs-service.js"></script>
    <script type="text/javascript" src="https://js.api.here.com/v3/3.1/mapsjs-ui.js"></script>
    <script type="text/javascript" src="https://js.api.here.com/v3/3.1/mapsjs-mapevents.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-modal/0.9.1/jquery.modal.min.js"></script>
    <script type="text/javascript" src='/assets/js/map.js?get=<?=time()?>'></script>
    <script type="text/javascript" src='/assets/js/script.js?get=<?=time()?>'></script>
</body>
</html>
