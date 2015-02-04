var base_query = {
    from: 
        "1AyXWy35PEgI22f0NTxEHdraooI7SiaUwlSJU7boP"
};



$(document).on('ready', function() {
    var map = new google.maps.Map(document.getElementById('map'), {
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

    var queryChange = function() {
        var options = {
                query: $.extend({}, base_query)
            };
            
        var value1 = $("#salary-slider").slider("values", 0);
        var value2 = $("#salary-slider").slider("values", 1);
 
        salary= "Salary >= " + value1 + " AND Salary <=" + value2;
        category = $('#category-select').val();
        state = $('#state-select').val();
        education = $('#education-select').val();

        query_where = salary;
        if(category.length > 0){
            query_where = query_where + " AND " + category;
        }
        if(state.length > 0){
            query_where = query_where + " AND " + state;
        }
        if(education.length > 0){
            query_where = query_where + " AND " + education;
        }

        options.query.where = query_where;
        console.debug(query_where);
        ftLayer.setOptions(options); 

    }
   
    $('#category-select').on('change', queryChange).trigger('change');
    $('#state-select').on('change', queryChange).trigger('change');
    $('#salary-slider').slider({change: function( event, ui ) {queryChange();
    }})
    $('#education-select').on('change', queryChange).trigger('change');
})


