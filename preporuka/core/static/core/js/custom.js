$( document ).ready(function() {

    $('#home-search-button').on('click', function() {

    });

    $("form").submit(function(e) {
        flag_validation = false;

//         if (!$('#home-search-title').val()) {
//            $('#home-search-title').attr("placeholder", "Въведете име на обекта!");
//            $('#home-search-title').addClass('placeholder-red');
//            $('#home-search-title-div').effect( "shake" );
//            flag_validation = true;
//         }

         if (!$('#search-choose-category').val()) {
            $('#search-choose-category-div').effect( "shake" );
            flag_validation = true;
         }

         if (!$('#search-choose-city').val()) {
            $('#search-choose-city-div').effect( "shake" );
            flag_validation = true;
         }

        if (flag_validation) {
            e.preventDefault();
        }
    });


    $('#sort-select').on('change', function() {
        $.ajax({
            url:"/",
            type: "POST",
            data: {sort: this.value},
            success:function(response){

            }
        });
    });


    $( "#utf_add_comment" ).submit(function( event ) {
        event.preventDefault();
        url = $(this).attr('action');
        var form = $(this);
        formData = new FormData(form[0]);
        $.ajax({
            url: url,
            type: "POST",
            processData: false,
            contentType: false,
            data: formData,
            success:function(data) {
                if (!data['error']) {
                    showPopUp('message_popup', 'green', 'Успех!', 'Успешно добавихте нов коментар, който ще бъде видим след одобрение!');
                    $('.utf_leave_rating input:radio').prop('checked', false);
                    $('#textarea-review-content').val('');
                    if (data['rating']) {

                    }
                } else {
                    showPopUp('message_popup', 'red', 'Грешка!', 'Добавянето на коментар не беше успешно, свържете се с администратор!');
                }
            }
        });
    });

function hide_django_messages() {
    if ($(".messages").length) { // Hide django core messages
        setTimeout(function() {
            $(".messages").fadeOut('slow')
        }, 3000);
    }
}

//showPopUp("example", 'white', 'Успех!',  'Успешно добавихте нов коментар');

function showPopUp(id, type, title, content) {
        //var cancelar = 'Cancel';
        var buttonText = 'OK';

        var popFundo = '<div id="popFundo_' + id + '" class="popUpFundo ' + type + '"></div>'
        var janela = '<div id="' + id + '" class="popUp"><h1>' + title + "</h1><div><span>" + content + "</span></div><button class='puEnviar' data-parent=" + id + " id='" + id +"_enviar'>" + buttonText + "</button></div>";
        $("window, body").css('overflow', 'hidden');

        //$("body").append(popFundo);
        $("body").append(janela);
        //$("body").append(popFundo);

        $("#popFundo_" + id).fadeIn("fast");
        $("#" + id).addClass("p " + type + " popUpEntrada");

        $("#" + id + '_enviar').on("click", function(){
            fetchPopUp(id);
        });

    function fetchPopUp(id) {
        if(id !== undefined) {
            $("#" + id).removeClass("popUpEntrada").addClass("popUpSaida");

                $("#popFundo_" + id).fadeOut(1000, function(){
                    $("#popFundo_" + id).remove();
                    $("#" + $(this).attr("id") + ", #" + id).remove();
                    if (!($(".popUp")[0])){
                        $("window, body").css('overflow', 'auto');
                    }
                });
        } else {
            $(".popUp").removeClass("popUpEntrada").addClass("popUpSaida");
                $(".popUpFundo").fadeOut(1000, function() {
                    $(".popUpFundo").remove();
                    $(".popUp").remove();
                    $("window, body").css('overflow', 'auto');
                });
        }
    }
}

});