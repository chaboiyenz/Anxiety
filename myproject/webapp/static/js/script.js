function myFunction() {
    window.location.href = "http://127.0.0.1:8000/assessment";
}



// navbar
let list = document.querySelectorAll(".navigation li");

function activeLink() {
    list.forEach((item) => {
        item.classList.remove("hovered");
    });
    this.classList.add("hovered");
}

list.forEach((item) => item.addEventListener("mouseover", activeLink));

// Menu Toggle
let toggle = document.querySelector(".toggle");
let navigation = document.querySelector(".navigation");
let main = document.querySelector(".main");

toggle.onclick = function () {
    navigation.classList.toggle("active");
    main.classList.toggle("active");
};

//exercise popup
function timetogglePopup() {
    document.getElementById("time-popup1").classList.toggle("active");
}
//mind popup
function mindtogglePopup() {
    document.getElementById("mind-popup1").classList.toggle("active");
}

//distract popup
function distracttogglePopup() {
    document.getElementById("distract-popup1").classList.toggle("active");
}
//ground popup
function groundtogglePopup() {
    document.getElementById("ground-popup1").classList.toggle("active");
}

function aromatogglePopup() {
    document.getElementById("aroma-popup1").classList.toggle("active");
}

function cbttogglePopup() {
    document.getElementById("cbt-popup1").classList.toggle("active");
}


function defusiontogglePopup() {
    document.getElementById("defusion-popup1").classList.toggle("active");
}

function religiontogglePopup() {
    document.getElementById("religion-popup1").classList.toggle("active");
}



