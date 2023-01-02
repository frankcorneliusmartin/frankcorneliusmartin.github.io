var current_page = 1;

function sleepFor(sleepDuration){
    var now = new Date().getTime();
    while(new Date().getTime() < now + sleepDuration){
        /* Do nothing */
    }
}

/*
    - [ ] make snapped scroll optional
    - [ ] snap minimap scroll to anchor
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
            buildOnce: true,
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
    // console.log('anchor: '+current_page);
    // console.log('tag position: '+tag.position().top)
    // console.log('top offset: '+tag.offsetTop)
    // console.log('wrapper offset: '+$('.wrapper').offset().top)
    // console.log('main offset: '+$('main').offset().top)
    $('main').animate({'scrollTop': tag.position().top - $('.wrapper').offset().top}, 200);
    $('main').promise().done(function(){
        scrolling = false;
    });
    console.log('animation done')

}

function build_body() {

    // compute the view width and determine if we want to use columns
    // and pages or not.
    var view_width = $(window).width();
    console.log('window width: ' + view_width)

    var use_columns = view_width > 1200;
    use_columns = false;
    console.log('use column layout: ' + use_columns)

    // keep hidden copy for resize events
    stash_content()

    if ( use_columns ) {
        // build columns and pages
        buildPages(1,2);
        replace_scroll_event();

    } else {
        $('#hidden-wrapper').css('display', 'block');
        restore_scroll_event();
    }
}

function stash_content() {

    // store the page content in a hidden wrapper so we can use a
    // different layout on a resize event (=rebuilding pages)
    safe_ = $('#hidden-wrapper').clone();
    safe_.attr('id', 'hidden-wrapper-2')
    safe_.css('display', 'none');
    $("#content").append(safe_);

}

function clear_content(){
    $(".clone").remove();
}

function pop_content() {
    $('#hidden-wrapper').remove()
    content_clone = $('#hidden-wrapper-2').clone()
    content_clone.attr("id","hidden-wrapper");
    $("#content").append(content_clone);
}

function paged_scroll (event) {
    console.log('scroll on main event')
    if( !scrolling ) {
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
}

function replace_scroll_event() {
    // hiden the scroll bar
    $('main').css('overflow', 'hidden')

    // replace the scroll event
    $('main').bind('mousewheel DOMMouseScroll', paged_scroll )
}

function restore_scroll_event() {
    $('main').css('overflow', 'scroll')
    $('main').unbind('mousewheel DOMMouseScroll', paged_scroll);
}

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
            // 'table': 'rgba(198, 120, 221 ,0.1)',
        },
        back: 'rgba(0,0,0,0.02)',
        view: 'rgba(255,255,255,0.05)',
        drag: 'rgba(255,255,255,0.10)',
        interval: null
    });
}
$( document ).ready(function() {

    build_body();
    build_minimap();

    $(window).on('resize', function() {
        clear_content();
        pop_content();
        build_body();
        build_minimap();
    })

    // toggle content
    $(".toggle > *").hide();
    $(".toggle .header").show();
    $(".toggle .header").click(function() {
        if ($(this).hasClass("open")) {
            $(this).parent().children().not(".header").slideUp();
        } else {
            $(this).parent().children().not(".header").slideDown();
        }
        $(this).parent().children(".header").toggleClass("open");
    })
});
