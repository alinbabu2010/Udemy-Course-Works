/*global $,document */
$(document).ready(function () {
    'use strict';
    $("button#btnout").click(function () {
        $("#box1").fadeOut();
        $("#box2").fadeOut("slow");
        $("#box3").fadeOut(3000);
        $("#box4").fadeOut(1000);
    });
    $("button#btnout").click(function () {
        $("#box3").fadeIn();
        $("#box1").fadeIn("slow");
        $("#box4").fadeIn(3000);
        $("#box2").fadeIn(1000);
    });
    $("button#btnto").click(function () {
        $("#box9").fadeTo("slow", 0.25);
        $("#box10").fadeTo("slow", 0.5);
        $("#box11").fadeTo("slow", 0.75);
        $("#box12").fadeTo("slow", 0.15);
    });
    $("button#btntog").click(function () {
        $("#box13").fadeToggle();
        $("#box14").fadeToggle("slow");
        $("#box15").fadeToggle(3000);
        $("#box16").fadeToggle(1000);
    });
});