function mobileMenu (object) {

    var elements={"page_header_nav":{title: "page_header_nav"}};
    var mobiledisplay = window.getComputedStyle(document.getElementById("page_header_nav")).display;

    //Show nav element
    for(var nav in elements) {

        if(object!==nav) {
            document.getElementById(nav).style.display='none';
        }
        if(object==nav && mobiledisplay=='block') {
            document.getElementById(nav).style.display='none';
        }
        else {
            document.getElementById(nav).style.display='block';
        }
    }
}

function HideNav () {
    var screen = window.innerWidth;
    var nav = document.getElementById("page_header_nav");

    if (screen < 1200) {
        nav.style.display='none';
    }
}