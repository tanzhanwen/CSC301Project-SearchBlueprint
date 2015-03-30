function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});
var datas= "";
var pageNumber = 0;
		
		function navPage(increment)
		{
		    var d  = 0;
		     if(increment && pageNumber<13)
		    {
		        pageNumber = pageNumber +1; 
				d = 1;
		    }
		    
		    else if (!increment && pageNumber > 0)
		    {
		        pageNumber = pageNumber-1;
				d = 1;
				
		    }
			if (d){
		     $('.container').hide();
				$('#container' + pageNumber).show();
			 if(pageNumber ==1){
			 cr_l1();
				//$('.btn').attr("disabled","disabled");
			 

			 }
			 if(pageNumber ==2){
			 cr_l2();
			 
			 }
			 if(pageNumber ==3){
			 cr_l3();
			 
			 }
            		if(pageNumber == 7){
                		cr_l7();
            		}
            		if(pageNumber == 8){
                		cr_l8();
            		}
            		if(pageNumber == 9){
                	cr_l9();
            		}
            		if(pageNumber == 10){
                	cr_l10();
            		}
            		if(pageNumber == 11){
                	cr_l11();
            		}
					if(pageNumber == 12){
                	cr_l12();
            		}
					if(pageNumber == 13){
                	cr_l13();
            		}
			}
		    }
			
		function fadeAnswer(txt,txt2){
			var all_fade = txt.split(",");
		
			for (var i = 0; i < all_fade.length; i++) {
				$( all_fade[i]).fadeOut( 400 );
   
			}
			
			$( txt2).delay( 400 ).fadeIn( 400 );
			//$('.btn').removeAttr('disabled');
		
		}
		function cr_l1(){
			
			$('.hid').hide();
			 
			$( "#cr1_1" ).delay( 1000 ).fadeIn( 400 );
			$( "#cr1_2" ).delay( 2000 ).fadeIn( 400 );
			$( "#cr1_3" ).delay( 3000 ).fadeIn( 400 );
			$( "#cr1_4" ).delay( 3500 ).fadeIn( 400 );
			$( "#cr1_5" ).delay( 4000 ).fadeIn( 400 );
		}
		
		function cr_l2(){
			
			$('.hid2').hide();
			 
			$( "#cr2_1" ).show();
			$( "#cr2_2" ).delay( 1000 ).fadeIn( 300 );
			$( "#cr2_3" ).delay( 2000 ).fadeIn( 300 );
			$( "#cr2_4" ).delay( 3000 ).fadeIn( 300 );
			

		}
		function cr_l3(){
			
			$('.hid3').hide();
			 
			$( "#cr3_1" ).delay( 1000 ).fadeIn( 300 );
			$( "#cr3_2" ).delay( 2000 ).fadeIn( 300 );
			$( "#cr3_3" ).delay( 3000 ).fadeIn( 300 );

		}
		function cr_l7(){
			
			$('.hid7').hide();
			 
			$( "#cr7_1" ).delay( 1000 ).fadeIn( 300 );
			$( "#cr7_2" ).delay( 2000 ).fadeIn( 300 );
			$( "#cr7_3" ).delay( 3000 ).fadeIn( 300 );
            		$( "#cr7_4" ).delay( 4000 ).fadeIn( 300 );

		}
		function cr_l8(){
			
			$('.hid8').hide();
			 
			$( "#cr8_1" ).delay( 1000 ).fadeIn( 300 );
			$( "#cr8_2" ).delay( 2000 ).fadeIn( 300 );
			$( "#cr8_3" ).delay( 3000 ).fadeIn( 300 );

		}
		function cr_l9(){
			
			$('.hid9').hide();
			 
			$( "#cr9_1" ).delay( 1000 ).fadeIn( 300 );
			$( "#cr9_2" ).delay( 2000 ).fadeIn( 300 );
			$( "#cr9_3" ).delay( 3000 ).fadeIn( 300 );
            		$( "#cr9_4" ).delay( 4000 ).fadeIn( 300 );
            		$( "#cr9_5" ).delay( 5000 ).fadeIn( 300 );

		}
		function cr_l10(){
			
			$('.hid10').hide();
			 
			$( "#cr10_1" ).delay( 1000 ).fadeIn( 300 );
			$( "#cr10_2" ).delay( 2000 ).fadeIn( 300 );
			$( "#cr10_3" ).delay( 3000 ).fadeIn( 300 );
            		$( "#cr10_4" ).delay( 4000 ).fadeIn( 300 );
            		$( "#cr10_5" ).delay( 5000 ).fadeIn( 300 );

		}
		function cr_l11(){
			
			$('.hid11').hide();
			 
			$( "#cr11_1" ).delay( 1000 ).fadeIn( 300 );
			$( "#cr11_2" ).delay( 2000 ).fadeIn( 300 );
			$( "#cr11_3" ).delay( 3000 ).fadeIn( 300 );
            		$( "#cr11_4" ).delay( 4000 ).fadeIn( 300 );

		}
		function cr_l12(){
			
			$('.hid12').hide();
			 
			$( "#cr12_1" ).delay( 0 ).fadeIn( 300 );
			$( "#cr12_2" ).delay( 2000 ).fadeIn( 300 );
			$( "#cr12_3" ).delay( 3000 ).fadeIn( 300 );
            $( "#cr12_4" ).delay( 4000 ).slideDown( 300 );
			$( "#cr12_5" ).delay( 5000 ).slideDown( 300 );
            $( "#cr12_6" ).delay( 6000 ).slideDown( 300 );
			$( "#cr12_7" ).delay( 7000 ).slideDown( 300 );


		}
		function cr_l13(){
			
			$('.hid13').hide();
			 
			$( "#cr13_1" ).delay( 1000 ).fadeIn( 300 );
			$( "#cr13_2" ).delay( 2000 ).fadeIn( 300 );
			
            		

		}
		function doStuff(){
			$( "#cr13_5" ).fadeIn( 300 );
			$.ajax({
					 type: "POST",
					url: "/runScript/"+$( "#tt").val(),
					success: function(response){
					   output = response;
					   
					   outputs = output.split("http://");
					   
					   for (i = 0;i<outputs.length;i++){
							var table = document.getElementById("table");
							var row = table.insertRow(-1);
							var cell1 = row.insertCell(0);
							cell1.innerHTML = outputs[i];
						}
						
			   }
			  
			   
			}).done(function(data){
			 $( "#cr13_4" ).fadeIn( 300 );
			 $( "#cr13_3" ).fadeIn( 300 );
			 $( "#cr13_5" ).fadeOut( 300 );
			});
			 
		
		
		}
		
