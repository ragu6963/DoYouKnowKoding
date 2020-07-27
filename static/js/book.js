var height = $(window).height() - 100;
var width = $(window).width() - 100;
var all_page = [1]
var python_page = [2, 3]
var java_page = [4, 5]
var c_page = [6, 7]
var etc_page = [8, 9]
var end_page = [10, 11]
function hidden_bookmark(hiddenBtn) {
    $("#" + hiddenBtn).css('visibility', 'hidden')
}
function visible_bookmark(visibleBtnlist) {
    visibleBtnlist.forEach(visibleBtn => {
        $("#" + visibleBtn).css('visibility', 'visible')
    });
}
function move_python_bookmark(location, value) {
    $("#pythonBtn").removeAttr("style")
    $("#pythonBtn").css(location, value + "%")
}
function move_java_bookmark(location, value) {
    $("#javaBtn").removeAttr("style")
    $("#javaBtn").css(location, value + "%")
}
function move_c_bookmark(location, value) {
    $("#cBtn").removeAttr("style")
    $("#cBtn").css(location, value + "%")
}
function move_etc_bookmark(location, value) {
    $("#etcBtn").removeAttr("style")
    $("#etcBtn").css(location, value + "%")
}
$("#flipbook").turn({
    width: width,
    height: height,
    gradients: true,
});
// 종합 페이지
$("#allBtn").click(function () {
    $("#flipbook").turn("page", all_page);
});
// 파이썬 페이지
$("#pythonBtn").click(function () {
    $("#flipbook").turn("page", python_page);
});
// 자바 페이지
$("#javaBtn").click(function () {
    $("#flipbook").turn("page", java_page);
});
// C 페이지
$("#cBtn").click(function () {
    $("#flipbook").turn("page", c_page);
});
// 기타 페이지
$("#etcBtn").click(function () {
    $("#flipbook").turn("page", etc_page);
});

// 이전 다음 버튼
$("#prevBtn").click(function () {
    $("#flipbook").turn("previous");
});
$("#nextBtn").click(function () {
    $("#flipbook").turn("next");
});
// 페이지 이동 이벤트
$("#flipbook").bind("turning", function (event, page, view) {
    console.log(page + " 이동")
    // 종합 페이지
    if (all_page.includes(page)) {
        hiddenBtn = "allBtn"
        hidden_bookmark(hiddenBtn)
        visibleBtnlist = ["pythonBtn", "javaBtn", "cBtn", "etcBtn"]
        setTimeout(function () {
            visible_bookmark(visibleBtnlist)
        }, 100);
        move_python_bookmark("right", 10)
        move_java_bookmark("right", 15)
        move_c_bookmark("right", 20)
        move_etc_bookmark("right", 25)
    }
    else if (python_page.includes(page)) {
        hiddenBtn = "pythonBtn"
        hidden_bookmark(hiddenBtn)
        visibleBtnlist = ["allBtn", "javaBtn", "cBtn", "etcBtn"]
        setTimeout(function () {
            visible_bookmark(visibleBtnlist)
        }, 100);
        move_java_bookmark("right", 10)
        move_c_bookmark("right", 15)
        move_etc_bookmark("right", 20)
    }
    else if (java_page.includes(page)) {
        hiddenBtn = "javaBtn"
        hidden_bookmark(hiddenBtn)
        visibleBtnlist = ["allBtn", "pythonBtn", "cBtn", "etcBtn"]
        setTimeout(function () {
            visible_bookmark(visibleBtnlist)
        }, 100);
        move_python_bookmark("left", 10)
        move_c_bookmark("right", 10)
        move_etc_bookmark("right", 15)
    }
    else if (c_page.includes(page)) {
        hiddenBtn = "cBtn"
        hidden_bookmark(hiddenBtn)
        visibleBtnlist = ["allBtn", "pythonBtn", "javaBtn", "etcBtn"]
        setTimeout(function () {
            visible_bookmark(visibleBtnlist)
        }, 100);
        move_python_bookmark("left", 10)
        move_java_bookmark("left", 15)
        move_etc_bookmark("right", 10)
    }
    else if (etc_page.includes(page)) {
        hiddenBtn = "etcBtn"
        hidden_bookmark(hiddenBtn)
        visibleBtnlist = ["allBtn", "pythonBtn", "javaBtn", "cBtn"]
        setTimeout(function () {
            visible_bookmark(visibleBtnlist)
        }, 100);
        move_python_bookmark("left", 10)
        move_java_bookmark("left", 15)
        move_c_bookmark("left", 20)
    }
    else {
        visibleBtnlist = ["allBtn", "pythonBtn", "javaBtn", "cBtn", "etcBtn"]
        visible_bookmark(visibleBtnlist)
        move_python_bookmark("left", 10)
        move_java_bookmark("left", 15)
        move_c_bookmark("left", 20)
        move_etc_bookmark("left", 25)
    }
});