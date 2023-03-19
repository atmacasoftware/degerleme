$(document).ready(function () {

    $("#id_il").change(function () {
        const url = $("#addForm").attr("data-counties-url");  // get the url of the `load_cities` view
        const cityId = $(this).val();  // get the selected country ID from the HTML input
        $('#id_mahalle').children('option').remove();
        const empty_mahalle_option = document.createElement('option')
        empty_mahalle_option.textContent = '---------'
        document.getElementById("id_mahalle").appendChild(empty_mahalle_option)

        $.ajax({                       // initialize an AJAX request
            url: url,                    // set the url of the request (= /persons/ajax/load-cities/ )
            data: {
                'city_id': cityId       // add the country id to the GET parameters
            },
            success: function (data) {   // `data` is the return of the `load_cities` view function
                $("#id_ilce").html(data);
            }
        });

    });


    $("#id_ilce").change(function () {
        const url = $("#addForm").attr("data-neighbourhoods-url");  // get the url of the `load_cities` view
        const countyId = $(this).val();  // get the selected country ID from the HTML input


        $.ajax({                       // initialize an AJAX request
            url: url,                    // set the url of the request (= /persons/ajax/load-cities/ )
            data: {
                'county_id': countyId       // add the country id to the GET parameters
            },
            success: function (data) {   // `data` is the return of the `load_cities` view function
                $("#id_mahalle").html(data);
            }
        });

    });

})