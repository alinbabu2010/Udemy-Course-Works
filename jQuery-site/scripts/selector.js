/* Script for different selector examples */

/*global $,document*/
$(document).ready(function () {
    'use strict';
    $("button").click(function () {
        $('h2').hide();
        $('#heading').hide();
        $('.para').hide();
        $('*').hide();
        $('p:first').hide();
        $(this).hide();
    });
});