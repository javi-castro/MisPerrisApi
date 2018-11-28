			//1) Definir Las Variables
			var opcion_1= new Array ("seleccione", "Iquique", "Alto Hospicio", "Pozo Almonte");
			var opcion_2= new Array ("seleccione", "Antofagasta", "Mejillones", "Calama");
			var opcion_3= new Array ("seleccione", "Chañaral", "Caldera", "Copiapó");
			var opcion_4= new Array ("seleccione", "La Serena", "Coquimbo", "Vicuña");
			var opcion_5= new Array ("seleccione", "Valparaíso", "Casablanca", "Concón");
			var opcion_6= new Array ("seleccione", "Rancagua", "Codegua", "Coinco");
			var opcion_7= new Array ("seleccione", "Talca", "Curepto", "Maule");
			var opcion_8= new Array ("seleccione", "Concepción", "Coronel", "Florida");
			var opcion_9= new Array ("seleccione", "Temuco", "Carahue", "Freire");
			var opcion_10= new Array ("seleccione", "Valdivia", "Corral", "Los Lagos");
			var opcion_11= new Array ("seleccione", "Puerto Montt", "Calbuco", "Cochamós");
			var opcion_12= new Array ("seleccione", "Coihaique", "Lago Verde");
			var opcion_13= new Array ("seleccione", "Punta Arenas", "Laguna Blanca", "Torres del Paine");
			var opcion_14= new Array ("seleccione", "Estación Central", "Independencia", "Providencia");
			var opcion_15= new Array ("seleccione", "Arica", "Putre", "General Lagos");
			
			// 2) crear una funcion que permita ejecutar el cambio dinamico
			function cambiar(){
				var regiones;
				//Se toma el vamor de la "regiones seleccionada"
				regiones = document.formulario1.regiones[document.formulario1.regiones.selectedIndex].value;
				//se chequea si la "regiones" esta definida
				if(regiones!=0){
					//selecionamos las regiones Correctas
					mis_opts=eval("opcion_" + regiones);
					//se calcula el numero de regiones
					num_opts=mis_opts.length;
					//marco el numero de opcion en el select
					document.formulario1.opcion.length = num_opts;
					//para cada opcion del array, la pongo en el select
					for(i=0; i<num_opts; i++){
						document.formulario1.opcion.options[i].value=mis_opts[i];
						document.formulario1.opcion.options[i].text=mis_opts[i];
					}
					}else{
						//si no habia ninguna opcion seleccionada, elimino las regiones del select
						document.formulario1.opcion.length = 1;
						//ponemos un guion en la unica opcion que he dejado
						document.formulario1.opcion.options[0].value="-";
						document.formulario1.opcion.options[0].text="-";
					}
					//hacer un reset de las opciones
					document.formulario1.opcion.options[0].selected = true;
					
				};
		