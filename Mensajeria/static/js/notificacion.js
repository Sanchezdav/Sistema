$(document).ready(function () {

    $("#aceptar").click(function () {
        SimpleNotification.notify({
            icon: 'http://saludsrh.edomex.gob.mx/bt/bolsa_de_trabajo/images/PiensaGrande.png',
            title: 'Nuevo Servicio',
            description: 'Tienes un nuevo servicio por favor verifica'
        }).onClickOpen("http://10.33.168.1:8000").show();
    });
	
	SimpleNotification = window.SimpleNotification || {};
SimpleNotification = (function () {
    var notification;
    var permitted = window.webkitNotifications.checkPermission() == 0 ? true : false;

    var defaults = {
        icon: 'http://saludsrh.edomex.gob.mx/bt/bolsa_de_trabajo/images/PiensaGrande.png',
        title: 'Nuevo Servicio',
        description: 'Tienes un nuevo servicio por favor verifica'
    }

    var showNotification = function (options) {
        if (!permitted) {
            window.webkitNotifications.requestPermission();
            return;
        }
        var settings = jQuery.extend({}, defaults, options);
        notification = window.webkitNotifications.createNotification(
            settings.icon,
            settings.title,
            settings.description
        );
        return this;
    }

    var clickEvent = function (url) {
        notification.onclick = function () {
            window.open(url);
            notification.close();
        }
        return this;
    }

    var showEvent = function () {
        notification.show();
    }

    return {
        notify: showNotification,
        onClickOpen: clickEvent,
        show: showEvent
    }

})();

});