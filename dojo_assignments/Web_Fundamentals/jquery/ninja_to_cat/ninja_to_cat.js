$("document").ready(function(){
    $("img").click(function(){
       console.log("data-alt-src value is", $(this).attr("data-alt-src")); 
       var newImg = $(this).attr("data-alt-src");
        $(this).attr("src", newImg);
    });
});