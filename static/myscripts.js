jQuery(document).ready(function ($) {
    var bgColorArray = ["#00A5E3", "#FC6238", "#C05780", "#00CDAC", "#FFD872"],
        selectBG = bgColorArray[Math.floor(Math.random() * bgColorArray.length)];

    $("body").css("background-color", selectBG);
    $(".title").css("color", selectBG);
    $(".btn").css("color", selectBG);
});

function myFunction() {
    alert("Hello everyone! An important reminder: Drink Responsibly.");
}