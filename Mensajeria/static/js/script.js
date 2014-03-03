$(document).ready(function(){

   $('#aceptar').on('clic',refrescar);

});


function refrescar()
{
	setInterval(function(){
   		$.ajax({
		   	url: '/table',
		   	success:function(data){
		   		$('#datagrid1').html(data)
		   	}
		 });
   },3e3);
}