var current_page = 1;

function sleepFor(sleepDuration){
    var now = new Date().getTime();
    while(new Date().getTime() < now + sleepDuration){
        /* Do nothing */
    }
}

/*
    - [x] automatic scrolling
    - [ ] manual scrolling should snap (mobile?)
    - [ ] check how it is without pagination on mobile

*/
var n_of_pages = 0;
function buildPages(n, n_columns){

    page_height = $('main').height() - 50;
    contents = $('#hidden-wrapper').contents().length;
    console.log(contents)

    if(contents > 0){
        console.log('building page n: ' + n)

        // be careful this is updated in the recursion
        n_of_pages = n;

        // when we need to add a new page, use a jq object for a template
        // or use a long HTML string, whatever your preference
        template = $("#template").clone();
        template.addClass("clone");
        template.addClass("next"+n).addClass("next").css("display", "block").css('height', page_height);
        template.attr('id', 'anchor'+n);

        // up and down navigation
        template.find(".down a").attr('onclick', "go_to_page("+(n+1)+")");
        template.find(".up a").attr('onclick', "go_to_page("+(n-1)+")");

        // remove first and last navigation
        if(n==1) {
            template.find(".page-divider.up").remove()
        }

        $("#content").append(template);
        $('#hidden-wrapper').columnize({
            buildOnce: false,
            columns: n_columns,
            target: ".next:last .dynamic-content",
            buildOnce: true,
            overflow: {
                height: page_height,
                id: "#hidden-wrapper",
                doneFunc: function(){
                    console.log('processing next page');
                    buildPages(n+1, n_columns)
                }
            }
        })
        console.log('paginator done')
    } else {
        template.find(".page-divider.down").remove()
    }
}

var scrolling = false;

function go_to_page(page){
    current_page = page;
    scroll_to_anchor();
}

function scroll_to_anchor(){
    // var tag = $("#"+anchor_id);
    // if (scrolling){ return }
    scrolling = true;
    var tag = $('#anchor'+current_page);
    console.log('anchor: '+current_page);
    console.log('tag position: '+tag.position().top)
    console.log('top offset: '+tag.offsetTop)
    console.log('wrapper offset: '+$('.wrapper').offset().top)
    console.log('main offset: '+$('main').offset().top)
    $('main').animate({'scrollTop': tag.position().top - $('.wrapper').offset().top}, 200);
    $('main').promise().done(function(){
        scrolling = false;
    });
    console.log('animation done')

}

$( document ).ready(function() {

    // determine number of columns
    wwidth = $(window).width()
    if( wwidth > 1200 ) {
        n_columns = 2;
    } else {
        n_columns = 1;
    }
    console.log('window width: ' + wwidth)
    console.log('number of columns: ' + n_columns)

    safe_ = $('#hidden-wrapper').clone();
    safe_.attr('id', 'hidden-wrapper-2')
    safe_.css('display', 'none');
    $("#content").append(safe_);

    // build multi-column pages
    var pages = new Promise(resolve => {
        setTimeout(function () {
            buildPages(1, n_columns)
            resolve();
        }, 300);
    });

    Promise.all([pages]).then( () => {
        console.log('number of pages:' + n_of_pages)
    });

    $('main').css('overflow', 'hidden')




    // scroll_to_anchor()
    // setTimeout(scroll_to_anchor, 3000)

    pagemap(document.querySelector('#map'), {
        viewport: document.querySelector('main'),
        styles: {
            'header,footer,section,article': 'rgba(255,255,255,0.08)',
            'h1,a': 'rgba(255,255,255,0.10)',
            'h2,h3,h4': 'rgba(255,255,255,0.08)',
            'p': 'rgba(255,255,255,0.08)'
        },
        back: 'rgba(0,0,0,0.02)',
        view: 'rgba(255,255,255,0.05)',
        drag: 'rgba(255,255,255,0.10)',
        interval: null
    });

    $(window).on('resize', function() {
        $('#hidden-wrapper').remove()
        content_clone = $('#hidden-wrapper-2').clone()
        content_clone.attr("id","hidden-wrapper");
        $("#content").append(content_clone);
        $(".clone").remove();
        buildPages(1, n_columns);
        // setTimeout(buildPages, 300, 1, n_columns);
    })

    $('main').bind('mousewheel DOMMouseScroll', (event) => {
        console.log('scroll on main event')
        if (!scrolling){
            old_page = current_page;
        if (event.originalEvent.wheelDelta > 0 || event.originalEvent.detail < 0) {
            current_page -= 1;
            if (current_page < 1) { current_page = 1}
        }
        else {
            current_page += 1;
            if (current_page > n_of_pages) { current_page = n_of_pages}
        }
        console.log('current page: '+current_page);
        if (current_page != old_page){
            scroll_to_anchor('anchor'+current_page);
        }
        }

    })



});
