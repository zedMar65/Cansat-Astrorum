const bgs = document.querySelectorAll('.bg');
const headerBg = document.querySelector('.header-bg');
const headerFadeDistance = 100;
const headerBlurAmount = 32;

function parallax(scrollPosition) {
    const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
    if (isMobile) {
        return;
    }
    bgs.forEach(bg => {
        const rect = bg.parentElement.getBoundingClientRect();
        const top = rect.top + scrollPosition;
        const offset = (scrollPosition - top) * 0.5;
        bg.style.transform = 'translateY(' + offset + 'px)'; 
    });
}

function headerFade(scrollPosition) {
    const opacity = Math.min(scrollPosition / headerFadeDistance, 1);
    headerBg.style.backdropFilter = `blur(${headerBlurAmount * opacity}px)`;
}

function updateScroll() {
    const scrollPosition = window.scrollY;
    headerFade(scrollPosition);
    parallax(scrollPosition);
}

window.addEventListener('scroll', updateScroll);
window.addEventListener('resize', updateScroll);

updateScroll();

const hamburger = document.querySelector('.hamburger');
const headerList = document.querySelector('.header-list');

hamburger.addEventListener('click', function() {
    headerList.classList.toggle('active');
});

const navLinks = document.querySelectorAll('.header-link');

navLinks.forEach(link => {
    link.addEventListener('click', function() {
        headerList.classList.remove('active');
    });
});

const yearSpans = document.querySelectorAll('#year');

yearSpans.forEach(span => {
    span.innerText = new Date().getFullYear();
});

const transitionTime = 0.5;

const gallery = document.querySelector('.gallery');
const leftButton = document.querySelector('.gallery-button-left');
const rightButton = document.querySelector('.gallery-button-right');

let leftPhoto = document.querySelector('.gallery-left');
let centerPhoto = document.querySelector('.gallery-center');
let rightPhoto = document.querySelector('.gallery-right');

const photoNames = [
    "konferencija.jpg",
    "kompas.jpg",
    "team_together.jpg",
];

function nextIndex(index) {
    return (index + 1) % photoNames.length;
}

function prevIndex(index) {
    return (index + photoNames.length - 1) % photoNames.length;
}

let currentPhoto = 0;
let buttonsEnabled = true;

leftPhoto.src = `assets/${photoNames[prevIndex(currentPhoto)]}`;
centerPhoto.src = `assets/${photoNames[currentPhoto]}`;
rightPhoto.src = `assets/${photoNames[nextIndex(currentPhoto)]}`;

leftPhoto.style.transition = 'left ' + transitionTime + 's';
centerPhoto.style.transition = 'left ' + transitionTime + 's';
rightPhoto.style.transition = 'left ' + transitionTime + 's';

leftButton.addEventListener('click', function() {
    if (!buttonsEnabled) return;
    buttonsEnabled = false;

    currentPhoto = prevIndex(currentPhoto);

    leftPhoto.classList.add('gallery-center');
    leftPhoto.classList.remove('gallery-left');
    centerPhoto.classList.add('gallery-right');
    centerPhoto.classList.remove('gallery-center');
    rightPhoto.style.transition = 'none';
    rightPhoto.classList.add('gallery-left');
    rightPhoto.classList.remove('gallery-right');

    const temp = leftPhoto;
    leftPhoto = rightPhoto;
    rightPhoto = centerPhoto;
    centerPhoto = temp;

    setTimeout(() => {
        leftPhoto.style.transition = 'left ' + transitionTime + 's';
        leftPhoto.src = `assets/${photoNames[prevIndex(currentPhoto)]}`;
        buttonsEnabled = true;
    }, transitionTime * 1000);
});

rightButton.addEventListener('click', function() {
    if (!buttonsEnabled) return;
    buttonsEnabled = false;

    currentPhoto = nextIndex(currentPhoto);

    rightPhoto.classList.add('gallery-center');
    rightPhoto.classList.remove('gallery-right');
    centerPhoto.classList.add('gallery-left');
    centerPhoto.classList.remove('gallery-center');
    leftPhoto.style.transition = 'none';
    leftPhoto.classList.add('gallery-right');
    leftPhoto.classList.remove('gallery-left');

    const temp = rightPhoto;
    rightPhoto = leftPhoto;
    leftPhoto = centerPhoto;
    centerPhoto = temp;

    setTimeout(() => {
        rightPhoto.style.transition = 'left ' + transitionTime + 's';
        rightPhoto.src = `assets/${photoNames[nextIndex(currentPhoto)]}`;
        buttonsEnabled = true;
    }, transitionTime * 1000);
});
