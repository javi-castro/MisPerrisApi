$('#nombre').keypress(function(){//llamamos el id nombre y decimos que cada vez que una tecla sea ingresada por teclado obtenga el valor ingresado y reemplace la primera letra por una mayuscula y muestra el resultado por pantalla
			$(this).val($(this).val().replace(/(^|\s)\S/g, l => l.toUpperCase()));
			});