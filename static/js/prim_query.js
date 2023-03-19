$(document).ready(function () {
    document.querySelector('.show-prim').style.display = 'none'
    document.getElementById("prim_query").addEventListener('click', function (e) {
        e.preventDefault();
        let yil = document.getElementById("id_yil").value
        let ay = document.getElementById("id_ay").value
        $.ajax({
            type: 'GET',
            url: `/prim-sorgu/${yil}/${ay}`,
            success: function (response) {
                console.log(response.data)
                document.querySelector('.show-prim').style.display = 'block'
                document.getElementById("showPrim").value = response.data
                console.log(response.query)
            },
            error: function (error) {
                console.log(error)
            }
        })
    })
});