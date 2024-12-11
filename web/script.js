function parallax() {
    const bgs = document.querySelectorAll('.bg');
    const scrollPosition = window.scrollY;

    bgs.forEach(function(bg) {
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