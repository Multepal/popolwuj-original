
$(document).ready(function()
{
    $('.rs').click(function() {
        topic = '#topic-' + $(this).data('ana')
        content = $(topic).html()
        $('#topic-box').html(content)
        $('#topic-box').dialog({
            width: 500,
            modal: true,
            maxHeight: 600
        })
    });

    $('.pb').click(function() {
//        side = $(this).data("side")
//        sel = '[data-side="' + side + '"]'
//        $(sel).parent().offset({top:100})
    });

});