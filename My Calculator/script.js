/*jslint evil: true */
/*global $,document */
$(document).ready(function () {
    'use strict';
    $("input.button").on('click', function () {
        var value = $(this).val();
        $("#display").val($("#display").val() + value);
    });
    $("input[value='C']").on("click", function () {
        $("#display").val(" ");
    });
    $('#equal').on("click", function () {
        var result = eval($("#display").val());
        $("#display").val(result).show();
    });
});