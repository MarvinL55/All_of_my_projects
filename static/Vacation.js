var images = Array.from(document.getElementById("slideshow").getElementsByTagName("img"));
var currentIndex = 0;
var slideshowContainer = document.getElementById("slideshow");
var searchInput = document.querySelector(".search-input");
var searchButton = document.querySelector(".search-button");

function changeBackground() {
    images.forEach(function (image) {
        image.style.display = "none";
    });

    currentIndex = (currentIndex + 1) % images.length;
    images[currentIndex].style.display = "block";
}

function performSearch(){
    var searchTerm = searchInput.value;

    window.location.href = "/search?term=" + searchTerm;
}

searchButton.addEventListener("click", performSearch)

setInterval(changeBackground, 3000);
