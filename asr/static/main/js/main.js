
// Slick Carousel
$(document).ready(function () {
    $(".button-up").click(function() {
        $("html, body").animate({ scrollTop: 0 }, "slow");
        return false;
    });
    /**
     * Easy selector helper function
     */
    const select = (el, all = false) => {
        el = el.trim()
        if (all) {
            return [...document.querySelectorAll(el)]
        } else {
            return document.querySelector(el)
        }
    }

    /**
   * Easy event listener function
   */
    const on = (type, el, listener, all = false) => {
        let selectEl = select(el, all)
        if (selectEl) {
            if (all) {
                selectEl.forEach(e => e.addEventListener(type, listener))
            } else {
                selectEl.addEventListener(type, listener)
            }
        }
    }

    /**
       * Back to top button
    */
    let backtotop = select('.back-to-top')
    if (backtotop) {
        const toggleBacktotop = () => {
            if (window.scrollY > 100) {
                backtotop.classList.add('active')
            } else {
                backtotop.classList.remove('active')
            }
        }
        window.addEventListener('load', toggleBacktotop)
        onscroll(document, toggleBacktotop)
    }


    $('.projects-list-wrapper').slick({
        slidesToShow: 4,
        slidesToScroll: 1,
        prevArrow: $('.project-prev'),
        nextArrow: $('.project-next'),

        responsive: [
            {
                breakpoint: 1200,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1,
                }
            },
            {
                breakpoint: 997,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 600,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }]
    });

    $('.rate-wrap').slick({
        slidesToShow: 2,
        slidesToScroll: 1,
        autoplay: true,
        arrows: false,
        dots: false,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                }
            },
            {
                breakpoint: 600,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                }
            }]

    });
    $('.partners').slick({
        slidesToShow: 5,
        slidesToScroxll: 1,
        dots: true,
        prevArrow: $('.partner-prev'),
        nextArrow: $('.partner-next'),
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 4,
                    slidesToScroll: 1,
                }
            },
            {
                breakpoint: 767,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 600,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1,
                }
            }]
    });

    $('.videos-slider-2').slick({
        autoplay: true,
        slidesToScroll: 1,
        slidesToShow: 1,
        prevArrow: $('.sp-prev'),
        nextArrow: $('.sp-next'),
        dots: false,
        asNavFor: '.slider-nav-thumbnails',
        responsive: [
            {
                breakpoint: 600,
                settings: {
                    adaptiveHeight: true,
                }
            }
        ],

      });
      
      $('.slider-nav-thumbnails').slick({
        autoplay: true,
        slidesToShow: 6,
        slidesToScroll: 1,
        asNavFor: '.videos-slider-2',
        dots: false,
        focusOnSelect: true,
        variableWidth: true,
        autoplaySpeed: 6000,
        responsive: [
            {
                breakpoint: 997,
                settings: {
                    slidesToShow: 5,
                    slidesToScroll: 1,
                   
                }
            },
            {
                breakpoint: 600,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1,
                    adaptiveHeight: true,
                    centerMode: true
                }
            }
        ],
      });

    $('.news-img-container').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        prevArrow: $('.news-prev-arrow'),
        nextArrow: $('.news-next-arrow'),
        dots: true,
    });
    $('.rate-wrapper').slickLightbox({
        src: 'src',
        itemSelector: '.rate-img-fit img',
    });

    $('.videos-slider-2').slickLightbox({
        src: 'src',
        itemSelector: '.bs-overlay img',
    });

    /**
    * Open Side-Panel
    */

    $("#panel-btn").on("click", function () {
        $('.side-panel-mask').toggleClass("side-panel-active");
        $('.side-panel-content').toggleClass("side-panel-active");
    })

    $('.side-panel-mask').on("click", function () {
        $(this).removeClass("side-panel-active");
        $('.side-panel-content').removeClass("side-panel-active");
    })

    $('#panel-close').on("click", function () {
        $('.side-panel-mask').removeClass("side-panel-active");
        $('.side-panel-content').removeClass("side-panel-active");
    })
    /**
   * Animation on scroll
   */
    window.addEventListener('load', () => {
        AOS.init({
            duration: 1000,
            easing: 'ease-in-out',
            once: true,
            mirror: false
        })
    });
    /**
 * Porfolio isotope and filter
 */
   
      
      // Remove active class from all thumbnail slides
      $('.slider-nav-thumbnails .slick-slide').removeClass('slick-active');
      
      // Set active class to first thumbnail slides
      $('.slider-nav-thumbnails .slick-slide').eq(0).addClass('slick-active');
      
      // On before slide change match active thumbnail to current slide
      $('.videos-slider-2').on('beforeChange', function (event, slick, currentSlide, nextSlide) {
        var mySlideNumber = nextSlide;
        $('.slider-nav-thumbnails .slick-slide').removeClass('slick-active');
        $('.slider-nav-thumbnails .slick-slide').eq(mySlideNumber).addClass('slick-active');
      });
    
    $('#portfolio-wrap').lingGalleryFilter({
        tagContainer: $('#filter-controls')
    });

    // $('.grid').isotope({
    //     // options
    //     itemSelector: '.grid-item',
    //     layoutMode: 'fitRows'
    //   });
    new PureCounter();
});
