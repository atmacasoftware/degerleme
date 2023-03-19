$(document).ready(function () {
    $.ajax({
        type: 'GET',
        url: '/adres/city-county-json/',
        success: function (response) {
            const data = response.data
            data.map(item => {
                const option = document.createElement('option')
                option.textContent = item.name
                option.setAttribute('value', item.id)
                document.getElementById("id_il").appendChild(option)
            })
        },
        error: function (error) {
            console.log(error)
        }
    })

    document.getElementById("id_il").addEventListener('change', e => {
        const selectedCity = e.target.value

        $('#id_ilce').children('option').remove();
        const emptyoption = document.createElement('option')
        emptyoption.textContent = '---------'
        document.getElementById("id_ilce").appendChild(emptyoption)

        $('#id_mahalle').children('option').remove();
        const empty_mahalle_option = document.createElement('option')
        empty_mahalle_option.textContent = '---------'
        document.getElementById("id_mahalle").appendChild(empty_mahalle_option)

        $.ajax({
            type: 'GET',
            url: `/adres/city-county-json/${selectedCity}/`,
            success: function (response) {
                const cityData = response.data
                cityData.map(item => {
                    const option = document.createElement('option')
                    option.textContent = item.name
                    option.setAttribute('value', item.id)
                    document.getElementById("id_ilce").appendChild(option)
                })
            },
            error: function (error) {
                console.log(error)
            }
        })
    })

    document.getElementById("id_ilce").addEventListener('change', e => {
        const selectCounty = e.target.value
        $('#id_mahalle').children('option').remove();
        const emptyoption = document.createElement('option')
        emptyoption.textContent = '---------'
        document.getElementById("id_mahalle").appendChild(emptyoption)
        $.ajax({
            type: 'GET',
            url: `/adres/county-neighbourhood-json/${selectCounty}/`,
            success: function (response) {
                const cityData = response.data
                cityData.map(item => {
                    const option = document.createElement('option')
                    option.textContent = item.name
                    option.setAttribute('value', item.id)
                    document.getElementById("id_mahalle").appendChild(option)
                })
            },
            error: function (error) {
                console.log(error)
            }
        })

    })
})