/*jslint evil: true */
/*global $,document */
$(document).ready(function () {
    'use strict';
    $("input.button").on('click', function () {
        var value = $(this).val();
        if (value == $("#divide").val()) {
            value = '/';
        } else if (value == $("#minus").val()) {
            value = '-';
        } else if (value == $("#product").val()) {
            value = '*';
        }
        $("#display").val(calc.display.value + value);
    });
    $("input[value='C']").on("click", function () {
        $("#display").val(" ");
    });
    $('#equal').on("click", function () {
        var result = eval(calc.display.value);
        $("#display").val(result);
    });
});