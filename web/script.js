let navToggle = document.getElementById('nav-toggle');
let nav = document.getElementById('nav-list');

let line1 = document.getElementById('line-1');
let line2 = document.getElementById('line-2');

let extended = false;

let lineScale = 5;
let offset = 16-(2*lineScale);

function animateAttribute(element, attribute, start, end, duration, easingFunction) {
  const startTime = performance.now();

  function step(currentTime) {
    const elapsed = currentTime - startTime;
    const progress = Math.min(elapsed / duration, 1);

    const easedProgress = easingFunction(progress);

    const value = start + (end - start) * easedProgress;

    element.setAttribute(attribute, value);

    if (progress < 1) {
      requestAnimationFrame(step);
    }
  }

  requestAnimationFrame(step);
}

function easeInOut(t) {
  return t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;
}

line1.setAttribute('x1', 1*lineScale+offset);
line1.setAttribute('y1', 4*lineScale+offset);
line1.setAttribute('x2', 3*lineScale+offset);
line1.setAttribute('y2', 2*lineScale+offset);

line2.setAttribute('x1', 3*lineScale+offset);
line2.setAttribute('y1', 2*lineScale+offset);
line2.setAttribute('x2', 1*lineScale+offset);
line2.setAttribute('y2', 0+offset);


function animateLines() {
  if (extended) {
    animateAttribute(line1, 'x1', parseFloat(line1.getAttribute('x1')), 1*lineScale+offset, 300, easeInOut);
    animateAttribute(line1, 'y1', parseFloat(line1.getAttribute('y1')), 4*lineScale+offset, 300, easeInOut);
    animateAttribute(line1, 'x2', parseFloat(line1.getAttribute('x2')), 3*lineScale+offset, 300, easeInOut);
    animateAttribute(line1, 'y2', parseFloat(line1.getAttribute('y2')), 2*lineScale+offset, 300, easeInOut);

    animateAttribute(line2, 'x1', parseFloat(line2.getAttribute('x1')), 3*lineScale+offset, 300, easeInOut);
    animateAttribute(line2, 'y1', parseFloat(line2.getAttribute('y1')), 2*lineScale+offset, 300, easeInOut);
    animateAttribute(line2, 'x2', parseFloat(line2.getAttribute('x2')), 1*lineScale+offset, 300, easeInOut);
    animateAttribute(line2, 'y2', parseFloat(line2.getAttribute('y2')), 0+offset, 300, easeInOut);
  } else {
    animateAttribute(line1, 'x1', parseFloat(line1.getAttribute('x1')), 3*lineScale+offset, 300, easeInOut);
    animateAttribute(line1, 'y1', parseFloat(line1.getAttribute('y1')), 4*lineScale+offset, 300, easeInOut);
    animateAttribute(line1, 'x2', parseFloat(line1.getAttribute('x2')), 1*lineScale+offset, 300, easeInOut);
    animateAttribute(line1, 'y2', parseFloat(line1.getAttribute('y2')), 2*lineScale+offset, 300, easeInOut);

    animateAttribute(line2, 'x1', parseFloat(line2.getAttribute('x1')), 1*lineScale+offset, 300, easeInOut);
    animateAttribute(line2, 'y1', parseFloat(line2.getAttribute('y1')), 2*lineScale+offset, 300, easeInOut);
    animateAttribute(line2, 'x2', parseFloat(line2.getAttribute('x2')), 3*lineScale+offset, 300, easeInOut);
    animateAttribute(line2, 'y2', parseFloat(line2.getAttribute('y2')), 0+offset, 300, easeInOut);
  }
  extended = !extended;
}

navToggle.addEventListener('click', function() {
  nav.classList.toggle('extended');
  navToggle.classList.toggle('active');
  arrow.classList.toggle('active');

  animateLines();

  console.log("click")
});