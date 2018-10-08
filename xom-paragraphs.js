
$(document).ready(function()
{

    $('.rs[data-ana]').click(function() {
        ana = $(this).data('ana')
        topic = '#topic-' + ana
        src_str = $(this).html()
        title = $(topic + ' .topic-title').html()
        type = $(topic + ' .topic-type').html()
        desc = $(topic + ' .topic-description').html()
        link = $(topic + ' .topic-link').attr('href')
        $('#topic-box .modal-type').html('Téma')
        $('#topic-box .modal-title').html(title + " (" + type + ")")
        $('#topic-box .modal-body').html(desc)
        $('#topic-box .modal-body').prepend('<div class="source-string alert alert-success">As given: <b>'+src_str+'</b></div>')
        $('#topic-box .multepal-link').attr('href', link) 
        $('#topic-box').trigger('focus')
        $('.rs[data-ana="' + ana + '"]').css('color', 'gray')
    });

    $('.lb').click(function() {
        nid = $(this).data('nid')
        note = '#annotation-' + nid
        line_id = $(this).data('source-line-id')
        line_id_label = parse_line_id(line_id)
        title = $(note + ' .annotation-title').html()
        body = $(note + ' .annotation-content').html()
        link = $(note + ' .annotation-link').attr('href')
        $('#topic-box .modal-type').html('Annotación')
        $('#topic-box .modal-title').html(title)
        $('#topic-box .modal-body').html(body)
        $('#topic-box .modal-body').prepend('<div class="source-line-id alert alert-success">&#8853; '+line_id_label+'</div>')
        $('#topic-box .multepal-link').attr('href', link) 
        $('#topic-box').trigger('focus')
        $('a.lb[data-nid="' + nid + '"] .annotation-icon').css('color', 'gray')
    });

    $('a.folio-index-item').click(function() {
        target = $(this).data('target')
        window.location.href = '#quc-' + target
        window.location.href = '#spa-' + target
    });

    function parse_line_id(line_id = '') {
        line_id = line_id.replace(/-/g, '')
            .replace(/xom/, '')
            .replace(/f/, 'Folio ')
            .replace(/s/, ', side ')
            .replace(/quc/, ", K'iche', line ")
            .replace(/spa/, ", Castellano, line ")
        return line_id
    }

});