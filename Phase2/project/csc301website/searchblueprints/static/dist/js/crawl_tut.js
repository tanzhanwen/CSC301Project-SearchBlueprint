var pageNumber = 0;
		
		function navPage(increment)
		{
		    var d  = 0;
		     if(increment && pageNumber<10)
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
		