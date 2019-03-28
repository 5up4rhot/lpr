$(document).ready(function(){
    // active links in nav menu
    if (location.pathname !== "/") {
        var path = location.pathname.split("/")[1] + "/"
    }
    $(".menu-active-list a[href*='" + path + "']").addClass("menu-active");

    // hamburger icon animation
    var $hamburger = $(".hamburger");
    $hamburger.on("click", function(e) {
    $hamburger.toggleClass("is-active");
  });;
});
