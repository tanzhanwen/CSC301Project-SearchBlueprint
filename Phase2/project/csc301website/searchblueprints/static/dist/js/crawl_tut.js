var pageNumber = 0;
		
		function navPage(increment)
		{
		    var d  = 0;
		     if(increment && pageNumber<3)
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
				$('.btn').attr("disabled","disabled");
			 

			 }
			
			}
		    }
		function cr_l1(){
			
			$('.hid').hide();
			 
			$( "#cr1_1" ).delay( 1000 ).fadeIn( 400 );
			$( "#cr1_2" ).delay( 2000 ).fadeIn( 400 );
			$( "#cr1_3" ).delay( 5000 ).fadeIn( 400 );
			$( "#cr1_4" ).delay( 5000 ).fadeIn( 400 );
			$( "#cr1_5" ).delay( 5000 ).fadeIn( 400 );
		}
		function cr1(){
			$( "#cr1_5" ).fadeOut( 400 );
			$( "#cr1_6" ).delay( 400 ).fadeIn( 400 );
			$('.btn').removeAttr('disabled');
		
		
		}
		function cr2(){
			$( "#cr1_5" ).fadeOut( 400 );
			$( "#cr1_7" ).delay( 400 ).fadeIn( 400 );
			$('.btn').removeAttr('disabled');
			
		}
		