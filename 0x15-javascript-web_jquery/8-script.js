$.ajax({

    // The URL for the request
    url: "https://swapi-api.hbtn.io/api/films/?format=json",

    // Whether this is a POST or GET request
    type: "GET",

    // The type of data we expect back
    dataType : "json",
}).done(function(response) {
    for (let i = 0; i < response.results.length; i++) {
        $("UL#list_movies").append("<li>" + response.results[i].title + "</li>");
    }
});
