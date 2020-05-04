
$("document").ready(function(){
    $(".show").click(function(){
        $(".show+p span").show();
    });
    $(".fader").click(function(){
        $(".fader+p").fadeOut();
    });
    $(".attr").click(function(){
        $("img").attr({
            width: "400px;",
            height: "300px;",
            alt: "biscuits"
        })
    })

})