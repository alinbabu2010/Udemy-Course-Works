/* global document */
var dogImage = document.querySelector('img');

dogImage.onclick = function () {
    'use strict';
    var myImages = dogImage.getAttribute('src');
    if (myImages === 'images/buliding.jpg') {
        dogImage.setAttribute('src', 'images/nature.jpg');
    } else {
        dogImage.setAttribute('src', 'images/buliding.jpg');
    }
};