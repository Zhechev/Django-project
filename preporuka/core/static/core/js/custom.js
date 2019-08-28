$( document ).ready(function() {

    if ($(".messages").length) { // Hide django core messages
        setTimeout(function() {
            $(".messages").fadeOut('slow')
        }, 3000);
    }

});