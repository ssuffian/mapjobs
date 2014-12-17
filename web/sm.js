var base_query = {
    select: "col2\x3e\x3e0",
    from: "1HQDwmk_GQPLZDkOXUSIIVKnCizMVR79W5ZLT8JRS"
        // '1wOs5MF-tOJqxGqcUPX1c68fs9WZJlCjSmb7biaHZ'
};


var map;

$(document).on('ready', function() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: new google.maps.LatLng(35.00246654734641, -95.17131599999999),
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        zoom: 4,
        mapTypeControlOptions: {
            style: google.maps.MapTypeControlStyle.DROPDOWN_MENU
        },
        panControl: false,
        scaleControl: false,
        zoomControl: false,
        streetViewControl: false
    });

    var ftLayer = new google.maps.FusionTablesLayer({
        map: map,
        query: $.extend({}, base_query)
    });

    $("#sign-select1").change(function() {

        var e = document.getElementById("sign-select1");
        var strUser = e.options[e.selectedIndex].text;
        var address = strUser;
        console.log(address);

        if (address == "Select a State") {

            map.setCenter(new google.maps.LatLng(35.00246654734641, -95.17131599999999));
            map.setZoom(4);

        } else {

            var geocoder = new google.maps.Geocoder();

            geocoder.geocode({
                "address": address
            }, function(results, status) {

                map.setCenter(results[0].geometry.location);
            })

            map.setZoom(6);

        }
        var options = {
            query: $.extend({}, base_query)
        };

        if ($('#sign-select').val() == "" && $('#sign-select2').val() =="") {
            options.query.where = $('#sign-select1').val()
        } else if($('#sign-select').val() != "" && $('#sign-select2').val()==""){

            options.query.where = $('#sign-select1').val()+ " AND " + $('#sign-select').val();

        }
        else if($('#sign-select').val() == "" && $('#sign-select2').val()!=""){

            options.query.where = $('#sign-select1').val()+ " AND " + $('#sign-select2').val();

        }

        else
        {

          options.query.where = $('#sign-select').val() + " AND " + $('#sign-select1').val()+ " AND " + $('#sign-select2').val();
        }
        ftLayer.setOptions(options);
    });



     $("#sign-select2").change(function() {


     var options = {
            query: $.extend({}, base_query)
        };


    if ($('#sign-select').val() == "" && $('#sign-select1').val() =="") {
            options.query.where = $('#sign-select2').val()
        } 
    else if($('#sign-select').val() != "" && $('#sign-select1').val()==""){

            options.query.where = $('#sign-select2').val()+ " AND " + $('#sign-select').val();

        }
        else if($('#sign-select').val() == "" && $('#sign-select1').val()!=""){

            options.query.where = $('#sign-select2').val()+ " AND " + $('#sign-select1').val();

        }

        else
        {

          options.query.where = $('#sign-select').val() + " AND " + $('#sign-select1').val()+ " AND " + $('#sign-select2').val();
        }


    ftLayer.setOptions(options);



     });

    var signChange = function() {
        var e = document.getElementById("sign-select");
        var strUser = e.options[e.selectedIndex].text;
        var address = strUser;
        console.log(address);

        if (address == "All Jobs") {

            map.setCenter(new google.maps.LatLng(35.00246654734641, -95.17131599999999));
            map.setZoom(4);

        }

        var options = {
            query: $.extend({}, base_query)
        };
        if ($('#sign-select1').val() == "" && $('#sign-select2').val()=="") {

            options.query.where = $('#sign-select').val()
        }

        else if ($('#sign-select1').val()=="" && $('#sign-select2').val()!="") {

             options.query.where = $('#sign-select').val() + " AND " + $('#sign-select2').val();

        }


        else if ($('#sign-select1').val()!="" && $('#sign-select2').val()=="") {

             options.query.where = $('#sign-select').val() + " AND " + $('#sign-select1').val();

        }



        else{

            options.query.where = $('#sign-select').val() + " AND " + $('#sign-select1').val()+ " AND " + $('#sign-select2').val();
        }

        ftLayer.setOptions(options);  //this is complete 

    };

    $('#sign-select')
        .on('change', signChange)
        .trigger('change');


});