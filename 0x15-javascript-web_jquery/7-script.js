    let name = "";

    $.ajax({
    
        // The URL for the request
        url: "https://swapi-api.hbtn.io/api/people/5/?format=json",
    
        // Whether this is a POST or GET request
        type: "GET",
    
        // The type of data we expect back
        dataType : "json",
    }).done(function(response) {
        name = response.name;
        $("DIV#character").text(name);
    });
