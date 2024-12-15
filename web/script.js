const bgs = document.querySelectorAll('.bg');
const header = document.querySelector('header');
const headerFadeDistance = 100;
const headerBlurAmount = 64;

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
    header.style.backdropFilter = `blur(${headerBlurAmount * opacity}px)`;
}

function updateScroll() {
    const scrollPosition = window.scrollY;
    headerFade(scrollPosition);
    parallax(scrollPosition);
}

window.addEventListener('scroll', updateScroll);
window.addEventListener('resize', updateScroll);

updateScroll();

const yearSpans = document.querySelectorAll('#year');

yearSpans.forEach(span => {
    span.innerText = new Date().getFullYear();
});

const galleryNav = document.querySelector('.gallery-nav');
const gallery = document.querySelector('.gallery');
const photoParent = document.querySelector('.images');

let navButtons = [];

const photoNames = [
    "konferencija.jpg",
    "kompas.jpg",
];

photoParent.style.width = `${photoNames.length * 100}%`;

photoNames.forEach(photo => {
    const button = document.createElement('button');
    galleryNav.appendChild(button);
    navButtons.push(button);

    const img = document.createElement('img');
    img.src = `assets/${photo}`;
    img.classList.add('gallery-photo');
    img.style.width = `${100 / photoNames.length}%`;
    photoParent.appendChild(img);

    button.addEventListener('click', function() {
        currentPhoto = photoNames.indexOf(photo);
        photoParent.style.transform = `translateX(-${currentPhoto * 100 / photoNames.length}%)`;
        navButtons.forEach(button => button.classList.remove('active'));
        button.classList.add('active');
    });
});

navButtons[0].classList.add('active');