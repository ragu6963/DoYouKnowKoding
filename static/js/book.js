var height = $(window).height() - 100;
var width = $(window).width() - 100;
var all_page = [2, 3]
var python_page = [4, 5, 6, 7]
var java_page = [8, 9, 10, 11]
var c_page = [12, 13, 14, 15]
var etc_page = [16, 17, 18, 19]
var end_page = [20]


function hidden_bookmark(hiddenBtn) {
    $("#" + hiddenBtn).css('visibility', 'hidden')
}

function visible_bookmark(visibleBtnlist) {
    visibleBtnlist.forEach(visibleBtn => {
        $("#" + visibleBtn).css('visibility', 'visible')
    });
}

function move_all_bookmark(location, value) {
    $("#allBtn").removeAttr("style")
    $("#allBtn").css(location, value + "%")
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

// turn js 설정
$("#flipbook").turn({
    width: width,
    height: height,
    duration: 1200,
});

// 종합 페이지
$("#allBtn").click(function () {
    $("#flipbook").turn("page", all_page[0]);
});

// 파이썬 페이지
$("#pythonBtn").click(function () {
    $("#flipbook").turn("page", python_page[0]);
});

// 자바 페이지
$("#javaBtn").click(function () {
    $("#flipbook").turn("page", java_page[0]);
});

// C 페이지
$("#cBtn").click(function () {
    $("#flipbook").turn("page", c_page[0]);
});

// 기타 페이지
$("#etcBtn").click(function () {
    $("#flipbook").turn("page", etc_page[0]);
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

    // 목차 & 종합 페이지
    if (all_page.includes(page)) {
        hiddenBtn = "allBtn"
        hidden_bookmark(hiddenBtn)
        visibleBtnlist = ["pythonBtn", "javaBtn", "cBtn", "etcBtn"]
        setTimeout(function () {
            visible_bookmark(visibleBtnlist)
        }, 100);
        move_python_bookmark("right", 5)
        move_java_bookmark("right", 10)
        move_c_bookmark("right", 15)
        move_etc_bookmark("right", 20)
    }
    // 파이썬 페이지
    else if (python_page.includes(page)) {
        hiddenBtn = "pythonBtn"
        hidden_bookmark(hiddenBtn)
        visibleBtnlist = ["allBtn", "javaBtn", "cBtn", "etcBtn"]
        setTimeout(function () {
            visible_bookmark(visibleBtnlist)
        }, 100);
        move_all_bookmark("left", 5)
        move_java_bookmark("right", 5)
        move_c_bookmark("right", 10)
        move_etc_bookmark("right", 15)
    }
    else if (java_page.includes(page)) {
        hiddenBtn = "javaBtn"
        hidden_bookmark(hiddenBtn)
        visibleBtnlist = ["allBtn", "pythonBtn", "cBtn", "etcBtn"]
        setTimeout(function () {
            visible_bookmark(visibleBtnlist)
        }, 100);
        move_all_bookmark("left", 5)
        move_python_bookmark("left", 10)
        move_c_bookmark("right", 5)
        move_etc_bookmark("right", 10)
    }
    else if (c_page.includes(page)) {
        hiddenBtn = "cBtn"
        hidden_bookmark(hiddenBtn)
        visibleBtnlist = ["allBtn", "pythonBtn", "javaBtn", "etcBtn"]
        setTimeout(function () {
            visible_bookmark(visibleBtnlist)
        }, 100);
        move_all_bookmark("left", 5)
        move_python_bookmark("left", 10)
        move_java_bookmark("left", 15)
        move_etc_bookmark("right", 5)
    }
    else if (etc_page.includes(page)) {
        hiddenBtn = "etcBtn"
        hidden_bookmark(hiddenBtn)
        visibleBtnlist = ["allBtn", "pythonBtn", "javaBtn", "cBtn"]
        setTimeout(function () {
            visible_bookmark(visibleBtnlist)
        }, 100);
        move_all_bookmark("left", 5)
        move_python_bookmark("left", 10)
        move_java_bookmark("left", 15)
        move_c_bookmark("left", 20)
    }
    else if (end_page.includes(page)) {
        visibleBtnlist = ["allBtn", "pythonBtn", "javaBtn", "cBtn", "etcBtn"]
        setTimeout(function () {
            visible_bookmark(visibleBtnlist)
        }, 100);
        move_all_bookmark("left", 5)
        move_python_bookmark("left", 10)
        move_java_bookmark("left", 15)
        move_c_bookmark("left", 20)
        move_etc_bookmark("left", 25)
    }
    else {
        visibleBtnlist = ["allBtn", "pythonBtn", "javaBtn", "cBtn", "etcBtn"]
        setTimeout(function () {
            visible_bookmark(visibleBtnlist)
        }, 100);
        move_all_bookmark("right", 5)
        move_python_bookmark("right", 10)
        move_java_bookmark("right", 15)
        move_c_bookmark("right", 20)
        move_etc_bookmark("right", 25)
    }
});