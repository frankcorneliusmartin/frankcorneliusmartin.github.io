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

function sleepFor(sleepDuration){
    var now = new Date().getTime();
    while(new Date().getTime() < now + sleepDuration){
        /* Do nothing */
    }
}
function buildPages(n, n_columns){

    page_height = document.querySelector('main').clientHeight - 50;
    if($('#hidden-wrapper').contents().length > 0){

        // when we need to add a new page, use a jq object for a template
        // or use a long HTML string, whatever your preference
        template = $("#template").clone();
        template.addClass("next"+n).addClass("next").css("display", "block").css('height', page_height);
        template.attr('id', 'anchor'+n);

        // up and down navigation
        template.find(".down a").attr('href', '#anchor'+(n+1));
        template.find(".up a").attr('href', '#anchor'+(n-1));

        // remove first and last navigation
        console.log('page n: ' + n)
        if(n==1) {
            template.find(".page-divider.up").remove()
        }

        $("#content").append(template);
        $('#hidden-wrapper').columnize({
            buildOnce: true,
            columns: n_columns,
            target: ".next:last .dynamic-content",
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

    // build multi-column pages
    setTimeout(buildPages, 300, 1, n_columns);

    function scroll_to_anchor(){
        // var tag = $("#"+anchor_id);
        tag = $('#anchor2');
        console.log(tag.offset().top);
        $('main').animate({scrollTop: tag.offset().top}, 'slow');
        console.log('animation done')
    }
    // scroll_to_anchor()
    // setTimeout(scroll_to_anchor, 3000)



});
