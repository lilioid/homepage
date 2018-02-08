$(document).ready(function () {
    // Open widget from taskbar
    $(".widget-opener").on("click", function (e) {
        var link = $(e.currentTarget).attr("data-link");
        var widget = $(".widget[data-link=" + link + "]").get(0);
        $(widget).toggleClass("active");
        console.log("Toggling " + link);
    });

    // Close widget from "x"
    $(".close-widget-icon").on("click", function (e) {
        var widget = $(e.currentTarget).closest('div.widget');
        $(widget).toggleClass("active");
        console.log("Closing " + $(widget).attr("data-link"));
    });

    // Make windows draggable
    $(".ui-draggable").draggable({
        containment: "document",
        handle: ".ui-draggable-handler"
    });

    // Make windows switch focus (class=selected)
    $(".widget").on("mousedown", function (e) {
        $(".selected").removeClass("selected");
        $(e.currentTarget).addClass("selected");
    });
})