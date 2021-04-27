$(document).ready(function () {

    $("#get-forcast").submit(function (e) {
        e.preventDefault();

        //change button text on click
        $('#btn-submit').attr('value', 'Getting...');

        //disable button
        const button = document.getElementById('btn-submit')
        button.disabled = true;

        //removes spaces and lines from string
        var lat = $('#lat').val();
        var long = $('#long').val();
        // var textarr = text.trim().split(/\s+/);

        
        //send unsorted array data to views
        $.ajax({
            type : 'POST',
            url : "weather",
            data : {
                'lat' : lat,
                'long' : long,
            },
            dataType : 'json',
            headers : {'X-CSRFToken': csrftoken},

            //success response of sorted list if validation is passed
            success : function (response) {
                console.log("After sorting", response)
                var str = '<div>'
                

                str += '</div>'
                document.getElementById("weather-details").innerHTML = str;
                $('#btn-submit').attr("value","Submit");
                button.disabled = false;
            },

            //error response if validation failed
            error : function () {
                alert('Data sent is not a list of strings')
                $('#btn-submit').attr("value","Submit");
                button.disabled = false;
            }
        })
        document.getElementById('get-forcast').reset();
    })
})