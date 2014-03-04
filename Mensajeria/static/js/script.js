$(document).ready(function(){

   setInterval(function(){
   		$.ajax({
		   	url: '/table',
		   	success:function(data){
		   		$('#datagrid1').html(data)
		   	}
		 });
   },30000);

});
