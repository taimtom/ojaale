    var locations = [
    ['<div class="infobox"><div class="agent"><div class="image"><img class="img-thumbnail img-responsive" src="upload/testi_01.png" alt=""></div><div class="agent_desc"><h3 class="title"><a href="#">Carolina Keegan</a></h3><small>$10.00/hr</small><a class="readmore" href="#">View Profile</a></div></div></div>', 
    52.370216,
    4.895168,
    1],
    ['<div class="infobox"><div class="agent"><div class="image"><img class="img-thumbnail img-responsive" src="upload/testi_02.png" alt=""></div><div class="agent_desc"><h3 class="title"><a href="#">Carolina Keegan</a></h3><small>$10.00/hr</small><a class="readmore" href="#">View Profile</a></div></div></div>', 
    39.950467,
    32.826011,
    2],
    ['<div class="infobox"><div class="agent"><div class="image"><img class="img-thumbnail img-responsive" src="upload/testi_03.png" alt=""></div><div class="agent_desc"><h3 class="title"><a href="#">Carolina Keegan</a></h3><small>$10.00/hr</small><a class="readmore" href="#">View Profile</a></div></div></div>', 
    48.856614,
    2.352222,
    3],
    ['<div class="infobox"><div class="agent"><div class="image"><img class="img-thumbnail img-responsive" src="upload/testi_04.png" alt=""></div><div class="agent_desc"><h3 class="title"><a href="#">Carolina Keegan</a></h3><small>$10.00/hr</small><a class="readmore" href="#">View Profile</a></div></div></div>', 
    48.019573,
    66.923684,
    4],
    ['<div class="infobox"><div class="agent"><div class="image"><img class="img-thumbnail img-responsive" src="upload/testi_05.png" alt=""></div><div class="agent_desc"><h3 class="title"><a href="#">Carolina Keegan</a></h3><small>$10.00/hr</small><a class="readmore" href="#">View Profile</a></div></div></div>', 
    35.861660,
    104.195397,
    5],
    ['<div class="infobox"><div class="agent"><div class="image"><img class="img-thumbnail img-responsive" src="upload/testi_06.png" alt=""></div><div class="agent_desc"><h3 class="title"><a href="#">Carolina Keegan</a></h3><small>$10.00/hr</small><a class="readmore" href="#">View Profile</a></div></div></div>', 
    61.524010,
    105.318756,
    6],
    ['<div class="infobox"><div class="agent"><div class="image"><img class="img-thumbnail img-responsive" src="upload/testi_07.png" alt=""></div><div class="agent_desc"><h3 class="title"><a href="#">Carolina Keegan</a></h3><small>$10.00/hr</small><a class="readmore" href="#">View Profile</a></div></div></div>', 
    40.712784,
    -74.005941,
    7]
    ];

    /* ==============================================
    MAP -->
    =============================================== */
    
    var map=new google.maps.Map(document.getElementById('map'), {
        zoom: 3, scrollwheel: false, navigationControl: true, mapTypeControl: false, scaleControl: false, draggable: true, styles: [ {
            "featureType": "administrative", "elementType": "labels.text.fill", "stylers": [{"featureType":"poi.business","elementType":"geometry.fill","stylers":[{"visibility":"on"}]}]
        }
        ], center: new google.maps.LatLng(52.370216, 4.895168), mapTypeId: google.maps.MapTypeId.ROADMAP
    }
    
    );
    var infowindow=new google.maps.InfoWindow();
    var marker,
    i;
    for (i=0;
    i < locations.length;
    i++) {
        marker=new google.maps.Marker( {
            position: new google.maps.LatLng(locations[i][1], locations[i][2]), map: map, icon: 'images/apple-touch-icon.png'
        }
        );
        google.maps.event.addListener(marker, 'click', (function(marker, i) {
            return function() {
                infowindow.setContent(locations[i][0]);
                infowindow.open(map, marker);
            }
        }
        )(marker, i));
    }
