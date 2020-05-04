$(document).ready(function(){

    var pokeImg = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/";
    for(var i = 1; i <= 807; i++) {
        var img = $('<img />').attr({
            'id': i,
            'src': pokeImg + i + ".png",
            'width': 250
        }).appendTo('.left .row');               
    };
    
    
    $(document).on('click', 'img', function(){
        var rightImg = "<img src='" + $(this).attr('src') + "'>";
        var pokemonId = $(this).attr('id');
        var pokemonName ='';
        var pokemonHeight, pokemonWeight;
        var pokemonTypes = '';
        $.get("https://pokeapi.co/api/v2/pokemon/" + pokemonId, function(res){
            pokemonName = "<h2>" + res.name + "</h2>";
            pokemonHeight = "<h4>Height</h4>" + "<p>" + res.height + "</p>";
            pokemonWeight = "<h4>Weight</h4>" + "<p>" + res.weight + "</p>";
            pokemonType = res.types[0].type.name;
            $(".img").html(rightImg);
            $(".names").html(pokemonName);
            $("#poke-height").html(pokemonHeight);
            $("#poke-weight").html(pokemonWeight);
            pokemonTypes += "<h4>Types</h4>";
            pokemonTypes += "<ul>"; 
            for(var i = 0; i < res.types.length; i++) {
                pokemonTypes += "<li>" + res.types[i].type.name + "</li>";
            }
            pokemonTypes += "</ul>";
            $(".list-types").html(pokemonTypes);

        }, "json");

    });
});