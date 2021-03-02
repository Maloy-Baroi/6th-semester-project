window.onload = function () {
    let labels = document.getElementsByTagName('label');
    for (let i = 0; i < labels.length; i++) {
        disableSelection(labels[i]);
    }
};

function disableSelection(element) {
    if (typeof element.onselectstart != 'undefined') {
        element.onselectstart = function () {
            return false;
        };
    } else if (typeof element.style.MozUserSelect != 'undefined') {
        element.style.MozUserSelect = 'none';
    } else {
        element.onmousedown = function () {
            return false;
        };
    }
}