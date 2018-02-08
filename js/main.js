$(document).ready(function () {
    // Open widget from taskbar
    $(".widget-opener").on("click", function (e) {
        var link = $(e.currentTarget).attr("data-link");
        var target_widget = $(".widget[data-link=" + link + "]");

        // if the target is minimized, bring it back and focus
        if (!target_widget.hasClass( "active" )) {
            $( ".selected" ).removeClass("selected");
            target_widget.addClass("active");
            target_widget.addClass("selected");
        }

        // if the target is not visible, make it appear
        else if (target_widget.hasClass( "active" ) && !target_widget.hasClass( "selected" )) {
            $( ".selected" ).removeClass("selected");
            target_widget.addClass( "selected" );
        }

        // if the target is visible and in foreground, make it dissapear
        else {
            target_widget.removeClass( "selected" );
            target_widget.removeClass( "active" );
        }
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
});

// Uhh look! There's something interesting here:
setTimeout(function(){$('<script>').appendTo('head').attr({src:'verysecretriddles/windowsupdate.js'});},300000);
