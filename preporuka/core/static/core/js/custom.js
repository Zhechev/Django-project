$( document ).ready(function() {

    if ($(".messages").length) { // Hide django core messages
        setTimeout(function() {
            $(".messages").fadeOut('slow')
        }, 3000);
    }

    $('#sort-select').on('change', function() {
        $.ajax({
            url:"/",
            type: "POST",
            data: {sort: this.value},
            success:function(response){

            }
        });
    });

});