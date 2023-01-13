const btns = document.querySelectorAll('[data-carousel-btn]');

btns.forEach(btn =>{
    btn.addEventListener('click', () =>{
        const offset = btn.dataset.carouselBtn === "next" ? 1 : -1;
        const slides = btn.closest("[data-carousel]").querySelector("[data-slides]");

        const activeSlide = slides.querySelector("[data-active]");
        let newIndex = [...slides.children].indexOf(activeSlide) + offset;
        if (newIndex < 0){
            newIndex = slides.children.length - 1
        } else if (newIndex >= slides.children.length){
            newIndex = 0
        }

        slides.children[newIndex].dataset.active = true;
        delete activeSlide.dataset.active;
    })
})
