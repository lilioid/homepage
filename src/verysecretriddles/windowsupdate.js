console.log("Windows Updates found. Updating...");
$('<link>').appendTo('head').attr({
    rel: 'stylesheet',
    type: 'text/css',
    href: 'verysecretriddles/windowsupdate.css'
});

var x = "PGRpdiBpZD0id2lkZ2V0LXdpbmRvd3N1cGRhdGVzIiBjbGFzcz0id2lkZ2V0IHdpbmRvd3M5OC13aWRnZXQiPgogICAgPGRpdiBjbGFzcz0id2lkZ2V0LXRvcGJhciB1aS1kcmFnZ2FibGUtaGFuZGxlciI+CiAgICAgICAgPHAgY2xhc3M9IndpZGdldC10aXRsZSBuby1zZWxlY3QgZGVmYXVsdC1jdXJzb3IiPldpbmRvd3MgVXBkYXRlPC9wPgogICAgPC9kaXY+CiAgICA8ZGl2IGNsYXNzPSJ3aWRnZXQtYm9keSI+CiAgICAgICAgPGRpdj4KICAgICAgICAgICAgPGgyPlJlc3RhcnQgeW91ciBjb21wdXRlciB0byBmaW5pc2ggaW5zdGFsbGluZyBpbXBvcnRhbnQgdXBkYXRlcy48L2gyPgogICAgICAgICAgICA8cD5XaW5kb3dzIGNhbid0IHVwZGF0ZSBpbXBvcnRhbnQgZmlsZXMgYW5kIHNlcnZpY2VzIHdoaWxlIHRoZSBTeXN0ZW0gaXMgdXNpbmcgdGhlbS4KICAgICAgICAgICAgICAgIE1ha2Ugc3VyZSB0byBzYWZlIHlvdXIgZmlsZXMgYmVmb3JlIHJlc3RhcnRpbmcuPC9wPgoKICAgICAgICAgICAgPGJ1dHRvbiBpZD0icmVzdGFydC1idXR0b24iPlJlc3RhcnQgbm93PC9idXR0b24+CiAgICAgICAgPC9kaXY+CiAgICA8L2Rpdj4KPC9kaXY+";
$(atob(x)).appendTo("#desktop-root");

setTimeout(function () {
    $("#widget-windowsupdates").addClass("active").addClass("selected");
    console.log("Waiting for reboot");
}, 2000);
$("#restart-button").on("click", function (e) {
    console.log("Updating now...");
    open("verysecretriddles/windowsupdate.php", "_self");
});