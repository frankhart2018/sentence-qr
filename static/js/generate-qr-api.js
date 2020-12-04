$(document).ready(function() {

    $("#generate-qr").click(function() {
        var sentence = $("#sentence").val();

        if(sentence != "") {
            $.ajax({
                url: "/generate-qr",
                type: "post",
                dataType: "json",
                data: {"sentence": sentence},
                success: function(result) {
                    alert(result.status);
                    window.location.assign(result.filename);
                }
            });
        } else {
            alert("Please enter a sentece or a link to generate QR code for!");
        }
    });

});