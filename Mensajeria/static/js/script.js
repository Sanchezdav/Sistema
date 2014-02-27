$(document).ready(function(){

   $('#aceptar').on('click', refresh);

});

function refresh() {
    $.ajax({
        url: '{% url servicios %}',
        success: function(data) {
            $('#datagrid1').html(data);
        }
    });
    setInterval("refresh()", 3000);
}

$(function(){
    refresh();
});
}

