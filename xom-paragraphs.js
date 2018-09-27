
$(document).ready(function()
{

    $('.rs').click(function() {
        topic = '#topic-' + $(this).data('ana')
        title = $(topic + ' .topic-title').html()
        type = $(topic + ' .topic-type').html()
        desc = $(topic + ' .topic-description').html()
        link = $(topic + ' .topic-link').attr('href')
        $('#topic-box .modal-title').html('Tema: '+ title + " (" + type + ")")
        $('#topic-box .modal-body').html(desc)
        $('#topic-box .multepal-link').attr('href', link) 
        $('#topic-box').trigger('focus')
    });

    $('.lb').click(function() {
        note = '#annotation-' + $(this).data('nid')
        title = $(note + ' .annotation-title').html()
        body = $(note + ' .annotation-content').html()
        link = $(note + ' .annotation-link').attr('href')
        $('#topic-box .modal-title').html('Annotación: ' + title)
        $('#topic-box .modal-body').html(body)
        $('#topic-box .multepal-link').attr('href', link) 
        $('#topic-box').trigger('focus')
    });

});