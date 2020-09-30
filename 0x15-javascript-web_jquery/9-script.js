$.ajax({

    // The URL for the request
    url: "https://fourtonfish.com/hellosalut/?lang=fr",

    // Whether this is a POST or GET request
    type: "GET",

    // The type of data we expect back
    dataType : "json",
}).done(function(response) {
    $("DIV#hello").text(response.hello);
});
