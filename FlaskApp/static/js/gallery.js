  jQuery(document).ready(function($) {
	     var carousel = $("#myCarousel");
       	carousel.carousel({
                interval: 8000
        });
 
        //Handles the carousel thumbnails
        $('[id^=carousel-selector-]').click(function () {
    		var id_selector = $(this).attr("id");
    		try {
    		    var id = /-(\d+)$/.exec(id_selector)[1];
    		    console.log(id_selector, id);
    		    carousel.carousel(parseInt(id));

    		} catch (e) {
    		    console.log('Regex failed!', e);
    		}
    	});
        // When the carousel slides, auto update the text
        carousel.on('slid.bs.carousel', function (e) {
                 var id = $('.item.active').data('slide-number');
                console.log(id)
                $('#carousel-text').html($('#slide-content-'+id).html());
        });
});
