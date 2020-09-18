/*global $,document*/

$(document).ready(function () {
    'use strict';
    $('#Textarea').on('input', function () {
        $('#div').text($('#Textarea').val());
    });
});