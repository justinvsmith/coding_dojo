function createPage(){
    var world = [
        [2,2,2,2,2,2,2,2,2,2],
        [2,1,1,2,1,1,1,1,1,2],
        [2,1,1,2,1,2,2,2,1,2],
        [2,1,1,2,1,2,1,2,1,2],
        [2,1,1,2,1,2,1,2,1,2],
        [2,1,1,2,2,2,1,2,1,2],
        [2,1,1,1,1,1,1,2,1,2],
        [2,1,1,1,1,1,1,1,1,2],
        [2,2,2,2,2,2,2,2,2,2]
    ];
    
    var output = '';

    for(var i=0; i<world.length; i++){
        output += "<div class='row'>";
        for(var j=0; j<world[i].length; j++){
            if(world[i][j] === 2){
            output += "<div class='brick'>" + "</div>";
            } else if(world[i][j] === 1){
                output += "<div class='coin'>" + "</div>";
            } else if(world[i][j] === 0){
                output += "<div class='empty'>" + "</div>";
            }
        }
        output += "</div>";
    }
    console.log(output);
    $(".wrapper").append(output);

};

$("document").keypress(function(){
    console.log(e);
});

$("document").ready(function(){
    createPage();

});