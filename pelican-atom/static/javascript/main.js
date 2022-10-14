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
    interval: 200
});

function sleepFor(sleepDuration){
    var now = new Date().getTime();
    while(new Date().getTime() < now + sleepDuration){
        /* Do nothing */
    }
}


$(function(){
    var n = 1
    function buildPages(){

        if($('#hidden-wrapper').contents().length > 0){
            console.log('tigger')
            // when we need to add a new page, use a jq object for a template
            // or use a long HTML string, whatever your preference
            template = $("#template").clone().addClass("next"+n).addClass("next").css("display", "block");
            n++;
            $("#content").append(template);
            $('#hidden-wrapper').columnize({
                buildOnce: true,
                columns: 2,
                target: ".next:last .dynamic-content",
                overflow: {
                    height: document.querySelector('main').clientHeight - 50,
                    id: "#hidden-wrapper",
                    doneFunc: function(){
                        console.log('next');
                        buildPages()
                    }
                }
            })
            console.log('done')
        }


    }
    setTimeout(buildPages, 300);
});
