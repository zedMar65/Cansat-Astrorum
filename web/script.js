const bgs = document.querySelectorAll('.bg');

function parallax() {
    const scrollPosition = window.scrollY;

    bgs.forEach(bg => {
        const rect = bg.parentElement.getBoundingClientRect();
        const top = rect.top + scrollPosition;
        const offset = (scrollPosition - top) * 0.5;
        bg.style.transform = 'translateY(' + offset + 'px)';
        
    });

    // console.log(scrollPosition);
}


window.addEventListener('scroll', function() {
    parallax();
});

parallax();



const galleryNav = document.querySelector('.gallery-nav');
const gallery = document.querySelector('.gallery');
const photoParent = document.querySelector('.images');

let navButtons = [];

const photoNames = [
    "logo.jpg",
    "logo.png",
    "parachute.jpg",
    "placeholder.jpg"
];

photoNames.forEach(photo => {
    const button = document.createElement('button');
    galleryNav.appendChild(button);
    navButtons.push(button);

    const img = document.createElement('img');
    img.src = `assets/${photo}`;
    img.classList.add('gallery-photo');
    photoParent.appendChild(img);

    button.addEventListener('click', function() {
        currentPhoto = photoNames.indexOf(photo);
        photoParent.style.transform = `translateX(-${currentPhoto * 100}%)`;
        navButtons.forEach(button => button.classList.remove('active'));
        button.classList.add('active');
    });
});

navButtons[0].classList.add('active');