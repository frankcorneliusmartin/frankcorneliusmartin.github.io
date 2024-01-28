// Load the minimap
function build_minimap() {
    pagemap(document.querySelector('#map'), {
        viewport: document.querySelector('main'),
        styles: {
            'header,footer,section,article': 'rgba(255,255,255,0.08)',
            'h1,a': 'rgba(255,255,255,0.10)',
            'h2': 'rgba(152, 195, 121,.2)',
            'h3,h4': 'rgba(198, 120, 221,.2)',
            'p': 'rgba(255,255,255,0.08)',
            'div.highlight': 'rgba(255,255,255,0.08)',
            'img': 'rgba(255,255,255,0.2)',
            // 'table': 'rgba(198, 120, 221 ,0.1)',
        },
        back: 'rgba(0,0,0,0.02)',
        view: 'rgba(255,255,255,0.05)',
        drag: 'rgba(255,255,255,0.10)',
        interval: null
    });
}


document.addEventListener("DOMContentLoaded", function(event) {

    // build minimap
    build_minimap();

    let headers = document.querySelectorAll(".toggle .header");
    headers.forEach(header => {
        // Set initial state to closed
        let siblings = Array.from(header.parentNode.children);
        siblings.filter(el => el !== header).forEach(el => el.style.display = 'none');

        header.addEventListener('click', function() {

            if (header.classList.contains("open")) {

                siblings.filter(el => !el.classList.contains('header')).forEach(el => el.style.display = 'none');
            } else {

                siblings.forEach(el => el.style.display = 'block');
            }

            header.classList.toggle("open");
        });
    });
});