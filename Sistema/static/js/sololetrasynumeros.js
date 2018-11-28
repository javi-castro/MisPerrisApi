function validar(e) {//llamamos el vento validar desde la clase seleccion
	tecla = (document.all) ? e.keyCode : e.which;
	if (tecla==8) return true;
			patron =/[A-Za-z\s]/;//validamos de que solo sean caracteres los datos ingresados por teclado
			te = String.fromCharCode(tecla);
	return patron.test(te);
}	

 function soloNumeros(e){
    var key = window.event ? e.which : e.keyCode;
    if (key < 48 || key > 57) {
        //Usando la definición del DOM level 2, "return" NO funciona.
        e.preventDefault();
    }
}