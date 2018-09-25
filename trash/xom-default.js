
function main () {

    $("#cmd-breaks").click(function(){                    
        label = $(this).html()
        if (label == 'Show breaks') {
            // Show breaks
            $('.break').show()     
            $('.del').show()
            $('p').css('margin-top', '0')                   
            $(this).html('Hide breaks');
        } else {
            // Hide breaks
            $('.break').hide()
            $('.del').hide()
            $('p').css('margin-top', '.5rem')
            $(this).html('Show breaks');
        }                
    })
    
}
