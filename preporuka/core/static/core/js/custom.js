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
            success:function(){
                console.log('success');
            }
        });
    });

});