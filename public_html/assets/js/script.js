$(function() {
    $('#map').css('display', 'none');
    $('main ul').css('display', 'none');

    $('.search-input').focus(function (){
        $('.banner').css('display', 'none');
        $('#map').css('display', 'block');
    });
    $('.search-input').focusout(function (){
        var search = $('.search-input').val();
        $.ajax({
            url: 'http://185.146.156.222:3001/extendSearch',
            method: 'get',
            data: {query: search},
            success: function(json){
                var group = new H.map.Group();
                $('main ul li').each(function (){
                    $(this).remove();
                });
                map.removeObjects(map.getObjects());
                map.addObject(group);
                group.addEventListener('tap', function (evt) {
                    var bubble =  new H.ui.InfoBubble(evt.target.getGeometry(), {
                        content: evt.target.getData()
                    });
                    ui.addBubble(bubble);
                }, false);


                json.forEach(function(item) {
                    let htmlMap = '<div class="window"><h3>' + item.name +'</h3><p>Цена: ' + item.price + '</p><p>Адрес: ' + item.address +'</p><button class="addCart" data-id="'+item.id+'">В корзину</button></div>';
                    addMarkerToGroup(group, {lat:item.lat, lng:item.lon}, htmlMap);
                    let htmlUl = '<div><h3>' + item.name +'</h3><p>Цена: ' + item.price + '</p><p>Адрес: ' + item.address +'</p><button class="addCart" data-id="'+item.id+'">В корзину</button></div>';
                    $('main ul').append('<li>'+htmlUl+'</li>');
                });
                addCart();
                $('main ul').css('display', 'block');
                $('.addCart').click(function (){
                    let id = $(this).attr('data-id');
                    $.ajax({
                        url: '/ajax.php',
                        method: 'get',
                        data: {type: "addCart", id: id},
                        success: function (data) {
                            console.log(data);
                            $('.vp').html(data);
                        }
                    });
                });
            },
        });
    });
    $('#check').click(function (){
        $.ajax({
            url: '/ajax.php',
            method: 'get',
            data: {type: "createOrder"},
            success: function (json) {
                $('.vp').html('<h3>Заказ оформлен!</h3>')
            }
        });
    });

    function addCart(){
        $('.addCart').click(function (){
            let id = $(this).attr('data-id');
            $.ajax({
                url: '/ajax.php',
                method: 'get',
                data: {type: "addCart", id: id},
                success: function (data) {
                    console.log(data);
                    $('.vp').html(data);
                }
            });
        });
    }
});