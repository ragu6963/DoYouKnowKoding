var height = $(window).height() - 100;
var width = $(window).width() - 100;

$("#flipbook").turn({
    width: width,
    height: height,
});
$("#indexBtn").click(function () {
    $("#flipbook").turn("page", 1);
});
$("#pythonBtn").click(function () {
    $("#flipbook").turn("page", 2);
});
$("#javaBtn").click(function () {
    $("#flipbook").turn("page", 4);

});
$("#cBtn").click(function () {
    $("#flipbook").turn("page", 6);
});
$("#etcBtn").click(function () {
    $("#flipbook").turn("page", 8);

});

$("#prevBtn").click(function () {
    $("#flipbook").turn("previous");
});
$("#nextBtn").click(function () {
    $("#flipbook").turn("next");
});

$("#flipbook").bind("turning", function (event, page, view) {
    console.log(page + " 이동")
});