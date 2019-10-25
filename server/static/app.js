function getURL(url, success) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            success(xmlHttp.responseText);
        }
    }
    xmlHttp.open("GET", url, true);
    xmlHttp.send();
}

// setInterval(getTemp, 2000);

function getLight() {
    getURL('/api/light', function (result) {
        var response = JSON.parse(result);
        var insert = document.getElementsByClassName("value-lum");
        Array.prototype.forEach.call(insert, function (item) {
            item.innerHTML = "lumière : " + response.light;
        });
        if (response.light < 200) {
            // Light mode
            var dark = document.getElementsByClassName("change-lum");
            Array.prototype.forEach.call(dark, function (item) {
                item.style.backgroundImage = "url('https://images.wallpaperscraft.com/image/deer_minimalism_vector_background_nature_93845_1920x1080.jpg')";
            var changelumcolor = document.getElementsByClassName("change-lum-color");
            Array.prototype.forEach.call(changelumcolor, function (item) {
                item.style.color = "#0C5866";
            var navbar = document.getElementsByClassName("navbar");
            Array.prototype.forEach.call(navbar, function (item) {
                item.style.backgroundColor = "#0C5866";
            });
            });
            });
        } else {
            //Dark mode
            var dark = document.getElementsByClassName("change-lum");
            Array.prototype.forEach.call(dark, function (item) {
                item.style.backgroundImage = "url('https://images.wallpaperscraft.com/image/surface_dark_background_texture_50754_1920x1080.jpg')";
            var changelumcolor = document.getElementsByClassName("change-lum-color");
            Array.prototype.forEach.call(changelumcolor, function (item) {
                item.style.color = "#ffffff";
            var navbar = document.getElementsByClassName("navbar");
            Array.prototype.forEach.call(navbar, function (item) {
                item.style.backgroundColor = "#373A3F";
            });
            });
            });
        }
    });
}


getLight()
setInterval(getLight, 1000);

// NAVBAR EN JS


$(window).scroll(function () {
    if ($(this).scrollTop() > 1) {
        $('header').addClass("sticky");
    }
    else {
        $('header').removeClass("sticky");
    }
});