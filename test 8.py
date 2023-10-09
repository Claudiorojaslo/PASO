def select_model():
    models = ["800AJ", "1250AJP"]  # Replace with your available models
    print("Seleccione Modelo:")
    for index, model in enumerate(models):
        print(f"{index + 1}. {model}")
    choice = int(input("Ingrese el numero que corresponde al modelo: "))
    return models[choice - 1]


def select_failure():
    failures = ["Motor", "Hidraulica", "Electrica"]
    print("\nSelecciones tipo de falla:")
    for index, failure in enumerate(failures):
        print(f"Falla {index + 1}. {failure.capitalize()}")
    choice = int(input("Ingrese el numero que corresponde al tipo de falla: "))

    return failures[choice - 1]


# Step 1: Get the model of the machine from the user
model = select_model()

# Step 2: Get the type of failure from the user
failure = select_failure()

# Step 3: Show options based on the model selected
if model == "800AJ":
    if failure == "Motor":
        options = ["Falla 535:7", "Falla 100:1", "Falla 91:2", "Motor no da partida y no hay codigos de falla", "Baja presion de aceite, codigo 436", 
                   "Motor se apaga cuando se exige", "Fuga de aceite por multiple de escape"]
    elif failure == "Hidraulica":
        options = ["Descompensacion UMS", "Cilindro elevacion torre no puede bajar", "Sin funciones hidraulicas, sin codigos de fallas",
                   "Equipo sin traccion"]
    elif failure == "Electrica":
        options = ["Sensor UMS Perdido", "UMS no calibrado"]
    else:
        print("Invalid failure type!")
        exit()
elif model == "1250AJP":
    if failure == "Motor":
        options =  ["Falla 535:7", "Falla 100:1", "Falla 91:2",  "Motor no da partida y no hay codigos de falla", "Baja presion de aceite, codigo 436", 
                   "Motor se apaga cuando se exige", "Fuga de aceite por multiple de escape"]
    elif failure == "Hidraulica":
        options = ["Equipo sin funciones hidraulicas, Motor Ok", "Presion de reserva sobre 500PSI", "Falla BCS - recuperacion hidraulica",
                   "Equipo sin traccion", "Equipo sin direccion", "No nivela Plataforma - fuera de tiempo", "Movimiento espasmodico de funciones"]
    elif failure == "Electrica":
        options = ["BCS - Electrico", "Falla CAN 1, Modulos JLG", "Falla CAN 2, Motor y otros", "Equipo tracciona lente en modo de transporte", "PIN load No Calibrado", 
                  "PVG bajo voltaje", "Nivelacion de plataforma fuera de tiempo", "Desacuerdo entre sensores y switches"]
    else:
        print("Invalid failure type!")
        exit()
        # Step 4: Display the troubleshooting steps or contact information
if options:
    for i, option in enumerate(options, 1):
        print(f"Opción {i}: {option}")

    # Provide steps for the selected option
    selected_option = int(input("Seleccione una opcion correspodiente al numero enterado: "))
    if selected_option in range(1, len(options) + 1):
        print(f"Selecionaste: {options[selected_option - 1]}")

        # Add logic to display the troubleshooting steps for the selected option
        if model == "800AJ":
            if failure == "Motor":
                if selected_option == 1:
                    print("1. Revisar codigo de acuerdo a tabla EMR2 codes EMR4 Codes")
                    print("2. Codigo 535:7, Revise conexion electrica y que posicion de actuador sea la correcta")
                    print("3. Revisar resistencia entre pines. Pin 1-2 = 2.0 - 2.5 Ohms, Pins 3-4 = 25-25.5 Ohms, Pin 3-5 = 25-25.5 Ohms")
                    print("4. Si valores no coinciden, cambie actuador")
                    # Add more steps as needed
                elif selected_option == 2:
                    print("1. Revisar codigo de acuerdo a tabla EMR2 codes EMR4 Codes")
                    print("2. Codigo 100:1, revisar sensor de presion de aceite, limpieza y estado de conector de sensor")
                    print("3. Ingresa a menu diagnostico --> Engine, valor de presion de aceite en ralenti debe ser entre 45 y 52 PSI")
                    print("4. Si lectura de presion en analizador esta entre 12 a 25 PSI, entonces limpiar alojamiento y valvula de alivio del circuito de aceite, llave allen cerca de filtro de aceite")
                    print("5. Si presion de aceite en analizador es igual a 0 PSI, hay problemas con cableado o sensor")
                    print("6. Mida continuidad entre modulo de motor y sensor de cableado o intente con otro sensor")
                    # Add more steps as needed
                elif selected_option == 3:
                    print("1. Revisar codigo de acuerdo a tabla EMR2 codes EMR4 Codes")
                    print("2. Codigo 91:2, limpiar conexiones y eliminar exceso de grasa dielectrica en conexiones de motor y JLG")
                    # Add more steps as needed

                elif selected_option == 4:
                    print("1. Conectar analizador, ver seccion diagnostico --> System, Ground battery voltage y Platform battery voltage")
                    print("2. Dar arranque al motor y revisar caida de tension, no deberia ser menor a 8 voltios y la diferencia entre Ground and Plataforma voltage no mayor a 0.5 voltios")
                    print("3. Si voltaje fue inferior 8 voltios, esto puede apagar modulo de motor y no arranca motor, falla presente 666 y 663, revisar capacidad de bateria con probador de baterias de arranque")
                    print("4. Voltaje sobre 8 Voltios y no hay arranque, revise filtro de aire y linea de combustible incluyendo filtro, en caso de ser necesario utilice bomba manual para cebar linea de combustible.")
                    print("5. Si al momento del arranque, analizador se apaga y vuelve al menu help, existe un problema en positivo o negativo, limpiar y mejorar instalaciones, revisar PIN 1 y 14 de modulo de motor y conector de circuito de motor y JLG")
                    print("6. Si no soluciona paso 5 con limpieza y mejora de conexion, instalar rele para reforzar linea de positivo de modulo EMR2, contacte a su soporte JLG.")
                    print("6. Contactar a Deutz para instalacion de parche llamado ""Hot Start"" esto hara que modulo de motor entrege mayor energia en caidas de tension pronunciadas.")

                elif selected_option == 5:
                    print("3. Ingresa a menu diagnostico --> Engine, valor de presion de aceite en ralenti debe ser entre 45 y 52 PSI")
                    print("4. Si lectura de presion en analizador esta entre 12 a 25 PSI, entonces limpiar alojamiento y valvula de alivio del circuito de aceite, llave allen cerca de filtro de aceite")
                    print("5. Si presion de aceite en analizador es igual a 0 PSI, hay problemas con cableado o sensor")
                    print("6. Mida continuidad entre modulo de motor y sensor de cableado o intente con otro sensor")

                elif selected_option == 6:
                    print("1. Revisar en que funciones motor se apaga comparar presiones hidraulicas. Funciones mayor exigencia brazo torre y brazo principal")
                    print("2. Si motor se apaga con una sola funcion a la vez, revisar linea de combustible - Aire")
                    print("3. Revisar que acelerador manual, no ha sido intervenido, recorrido del perno debe tener marca de pintura por Deutz, comparar con equipo operativo recorrido del perno")
                    print("4. Si motor se apaga durante la realizacion de dos funciones a la vez o en traccion en conejo con pendiente, revisar comprension de cilindros de motor")
                    print("5. Si equipo se encuentra en altura geografica sobre 3500 msnm, derratear bomba hidraulica de funciones, reducir presion de trabajo de 2600PSI a 2200PSI")

                elif selected_option == 7:
                    print("1. Esta condición se llamada ""Wet Stacking"", sucede cuando motor trabaja en baja carga para motores D2011, se indica procedimiento de asentamiento de motor añadiendo carga al motor")
                    print("2. Limpiar fuga de aceite por multiple de escape")
                    print("3. Identificar valvula hidraulica de liberacion de freno")
                    print("4. Desacoplar bobina electrica de freno, de esta manera el equipo no detectara falla por circuito abierto")
                    print("5. Pasar a control plataforma, dar arranque y conectar analizador JLG en plataforma, ingresar a Diagnostics --> Engine --> Actual Speed RPM")
                    print("6. Seleccion modo de traslado, conejo con pendiente")
                    print("7. Con joystick derecho, hacer funcion de traccion hacia adelante levemente y dejar motor entre 2500 y 2600 RPM")
                    print("8. Lo anterior hacerlo en lapsos de 2 minutos en un total de 30 minutos de prueba")
                    print("9. Si observamos que la fuga continua, hacer los pasos 7 y 8 por otros 30 minutos")
                    print("10. Si luego de los pasos anteriores sigue fugando, se debe contactar a Deutz para rectificar motor")

                else:
                    print("Invalid option!")
            if failure == "Hidraulica":
                if selected_option == 1:
                    print("1. Visualizacion de alarma de UMS activado de control tierra y plataforma a medida que brazo torre sube luego torre no deja bajar")
                    print("2. Verifique proyeccion de brazo vertical, codo que une a brazo torre con brazo principal donde se encuentra cilindro de nivel")
                    print("3. Si proyeccion hacia el suelo de brazo vertical es de 90º, entonces posible falla de sensor UMS, vaya a menu fallas electicas")
                    print("4. Si la proyeccion no es 90º entonces se debe realizar procedimiento de compensacion de cilindros")
                    print("5. Si brazo torre, no permite bajar, con analizador, Access level 2 --> Service Mode --> Tower Lift down --> ingrese codigo 81075, deberia bajar brazo")
                    print("6. Si no tiene analizador, jale de perilla roja y haga la funcion de brazo torre, esta funcion no debe hacerla permanentemente. Se debe realizar hasta que alarma visual UMS desapareza de panel")
                    print("7. Si luego de varios procedimientos de sincronizacion, equipo pierde y se activa alarma UMS con frecuencia, vaya a falla ""Cilindro torre no baja"" y siga los pasos")
                    print("8. Completado el punto 7 y no se encuentran fallas, entonces haga mantenimiento a bloque de renivelacion o cambielo, ver plano hidraulico 3D para su ubicacion")
                    # Add more steps as needed
                elif selected_option == 2:
                    print("1. Si Cilindro no baja, verifique con analizador en seccion UMS --> Status:")
                    print("2. Si Status = Normal, entonces existe un problema en valvulas de alivio de conjunto torre-level o valvula manual de secuencia no activada")
                    print("3. Verifique que valvula manual se activada completamente cuando telescopico de torre esta replegado, en caso que no actue, eleve el brazo principal esto dara un peso adicional sobre brazo telescopico de torre y ayuda a que valvula cierre, si funciona, revise posicion y recorrido de valvula")
                    print("4. Si UMS Sensor = 80º y 89º el sensor esta perdido y debe hacer modo de servicio, clave 81075. Si modo de servicio no funciona entonces, posible falla en lectura de sensor de proximidad de telescopico de torre o problema hidraulico en valvula manual de descenso de brazo torre con esto repita lo mencionado en punto 2")
                    print("5. Para que funcione el modo de servicio, en diagnostico Tower lift sensor = Closed, Tower telescope = Open, Tower Position = Up/Retracted")
                    print("5. Si Status = Backward Concern o Forward Concern, realizar procedimiento de sincronizacion, luego verificar que lampara de UMS no apareza en control tierra")
                    print("6. De acuerdo al punto 2, para verificar estado de valvulas realizar los siguientes procedimientos")
                    print("7. Con plano hidraulico, identificar, uprigth level cylinder en circuito serie de elevacion de torre, ver punto 6 y 7")
                    print("8. Verificar valvula de retencion de lado vastago, todos los brazos complemente abajo. Haga la funcion de bajada de brazo principal y deje haciendo la funcion por 30 segundos, verifique alguna alarma en UMS y verifique perpendicularidad de brazo uprigth, si no se cumplen cambie valvula de retencion")
                    print("9. Verificar valvula de retencion de lado botella, todos los brazos complemente abajo. eleve brazo torre 1.5 metros, jale de perilla roja de re-nivelacion por 30 segundos, verifique alguna alarma en UMS y verifique perpendicularidad de brazo uprigth, si no se cumplen cambie valvula de retencion")
                    print("10. Con plano hidraulico, identificar, Lift tower en circuito serie de elevacion de torre, ver punto  del 9 al 10")
                    print("11. Verificar valvula de retencion de lado botella. Brazo torre completamente elevado y retraido con brazo principal completamente elevado y extendido, con bajada de emergencia baje completamente brazo torre,verifique alguna alarma en UMS y verifique perpendicularidad de brazo uprigth, si no se cumplen cambie valvula de retencion")
                    print("12. Verificar valvula de retencion brazo torre, ubicado en bloque principal. Con equipo completamente replegado, conecte reloj hidraulico en puerto MX7, haga funcion de elevacion de torre por 5 segundos y luego libere, verificar que reloj mide sobre 1000 PSI por un minuto, si no es asi cambie valvula")

                    # Add more steps as needed
                elif selected_option == 3:
                    print("1. Verificar si la funcion no se realiza desde control tierra y control plataforma")
                    print("2. Si motor eleva las RPM y no hay funciones, probabilidad de ser falla en Presion o Flujo hidraulico")
                    print("3. Si motor NO eleva las RPM, codigo operacional o de falla presente que bloquea activacion de Valvula Dump y aceleracion de motor")
                    print("4. Si motor eleva las RPM, no hay codigos y solo se realiza funciones desde un comando es decir o solo de control tierra o solo de control plataforma, hay incongruencias con valores de personalidades o machine setup")
                    print("5. Para valores de Machine Setup, revise manual de servicio que aplica a numero de serie o contacte a su soporte JLG")
                    print("6. Revise valores de Personalidades de las funciones que no se realizan, revise manual de servicio que aplica a numero de serie o contacte a su soporte JLG")
                    print("7. Si valores de personalidad estan bien, entonces con reloj hidraulico mida presiones de bomba, tanto de trabajo como stand-by y presiones de los diferentes movimientos, si no tiene presion hidraulica, alta probabilidad de falla en valvula dump o valvula de alivios")
                    print("8. Si tiene presion hidraulica, entonces revise sellos y alojamiento de valvulas direccionesle, revise plano hidraulico para intercambiar valvulas direccionales en caso de que aplique ")
                    print("9. Si componentes hidraulicos y mecanicos de valvulas estan Ok, revise valores de resistencia electrica de selenoide, revisar valores en manual de servicio o contacte a su soporte JLG")
                    print("10. En ultima instancia cambie bombra hidraulica de funciones")

                elif selected_option == 4:
                    print("1. Verificar si la funcion no se realiza desde control tierra y control plataforma")
                    print("2. Si motor eleva las RPM y no hay funciones, probabilidad de ser falla en Presion o Flujo hidraulico")
                    print("3. Si motor NO eleva las RPM, codigo operacional o de falla presente que bloquea activacion de Valvula Dump y aceleracion de motor")
                    print("4. Si motor eleva las RPM, no hay codigos y solo se realiza funciones de un solo comando es decir, solo de control tierra o solo de control plataforma, hay incongruencias con valores de personalidades o machine setup")
                    print("5. Para valores de Machine Setup, revise manual de servicio que aplica a numero de serie o contacte a su soporte JLG")
                    print("6. Revise valores de Personalidades de las funciones que no se realizan, revise manual de servicio que aplica a numero de serie o contacte a su soporte JLG")
                    print("7. Si valores de personalidad estan bien, entonces con reloj hidraulico mida presiones de bomba, tanto de trabajo como stand-by y presiones de los diferentes movimientos, si no tiene presion hidraulica, alta probabilidad de falla en valvula dump o valvula de alivios")
                    print("8. Si tiene presion hidraulica, entonces revise sellos y alojamiento de valvulas direccionesle, revise plano hidraulico para intercambiar valvulas direccionales en caso de que aplique ")
                    print("9. Si componentes hidraulicos y mecanicos de valvulas estan Ok, revise valores de resistencia electrica de selenoide, revisar valores en manual de servicio o contacte a su soporte JLG")
                    print("10. En ultima instancia cambie bombra hidraulica de funciones")
                    # Add more steps as needed
                else:
                    print("Invalid option!")
        
            if failure == "Electrica":
                if selected_option == 1:
                    print("1. Verificar que alerta UMS esta activa en Analizador o Display")
                    print("2. Conectar analizador, diagnostico --> UMS verificar valor de grados de Tilt UMS.")
                    print("3. Si el valor es de 85° o mas significa que UMS esta desconectado o sensor defectuoso")
                    # Add more steps as needed
                elif selected_option == 2:
                    print("1. Verifique que analizador, indique la falla de UMS No Calibrado")
                    print("2. Ingrese nivel 2 y proceda a calibrar UMS siguiendo lo indicado por analizador")
                    print("3. Se solicita que el Tilt sensor debe esta correctamente calibrado antes de calibrar UMS, el valor debe ser menor a 1.3 grados, negativo o positivo")
                    print("4. Luego de calibrar, en Menu UMS vaya a Status y eleve y baje el brazo torre, siempre debe marcar normal, si indica un valor de FWD o REV concern entonces puede haber problemas hidraulicos o repita la calibracion considerando el valor del tilt sensor")
                
                else:
                    print("Invalid option!")

        if model == "1250AJP":
            if failure == "Motor":
                if selected_option == 1:
                    print("1. Revisar codigo de acuerdo a tabla EMR2 codes EMR4 Codes")
                    print("2. Codigo 535:7, Revise conexion electrica y que posicion de actuador sea la correcta")
                    print("3. Revisar resistencia entre pines. Pin 1-2 = 2.0 - 2.5 Ohms, Pins 3-4 = 25-25.5 Ohms, Pin 3-5 = 25-25.5 Ohms")
                    print("4. Si valores no coinciden, cambie actuador")
                    # Add more steps as needed
                elif selected_option == 2:
                    print("1. Revisar codigo de acuerdo a tabla EMR2 codes EMR4 Codes")
                    print("2. Codigo 100:1, revisar sensor de presion de aceite, limpieza y estado de conector de sensor")
                    print("3. Ingresa a menu diagnostico --> Engine, valor de presion de aceite en ralenti debe ser entre 45 y 52 PSI")
                    print("4. Si lectura de presion en analizador esta entre 12 a 25 PSI, entonces limpiar alojamiento y valvula de alivio del circuito de aceite, llave allen cerca de filtro de aceite")
                    print("5. Si presion de aceite en analizador es igual a 0 PSI, hay problemas con cableado o sensor")
                    print("6. Mida continuidad entre modulo de motor y sensor de cableado o intente con otro sensor")
                    # Add more steps as needed
                elif selected_option == 3:
                    print("1. Revisar codigo de acuerdo a tabla EMR2 codes EMR4 Codes")
                    print("2. Codigo 91:2, limpiar conexiones y eliminar exceso de grasa dielectrica en conexiones de motor y JLG")
                    # Add more steps as needed

                elif selected_option == 4:
                    print("1. Conectar analizador, ver seccion diagnostico --> System, Ground battery voltage y Platform battery voltage")
                    print("2. Dar arranque al motor y revisar caida de tension, no deberia ser menor a 8 voltios y la diferencia entre Ground and Plataforma voltage no mayor a 0.5 voltios")
                    print("3. Si voltaje fue inferior 8 voltios, esto puede apagar modulo de motor y no arranca motor, falla presente 666 y 663, revisar capacidad de bateria con probador de baterias de arranque")
                    print("4. Voltaje sobre 8 Voltios y no hay arranque, revise filtro de aire y linea de combustible incluyendo filtro, en caso de ser necesario utilice bomba manual para cebar linea de combustible.")
                    print("5. Si al momento del arranque, analizador se apaga y vuelve al menu help, existe un problema en positivo o negativo, limpiar y mejorar instalaciones, revisar PIN 1 y 14 de modulo de motor y conector de circuito de motor y JLG")
                    print("6. Si no soluciona paso 5 con limpieza y mejora de conexion, instalar rele para reforzar linea de positivo de modulo EMR2, contacte a su soporte JLG.")
                    print("6. Contactar a Deutz para instalacion de parche llamado ""Hot Start"" esto hara que modulo de motor entrege mayor energia en caidas de tension pronunciadas.")

                elif selected_option == 5:
                    print("3. Ingresa a menu diagnostico --> Engine, valor de presion de aceite en ralenti debe ser entre 45 y 52 PSI")
                    print("4. Si lectura de presion en analizador esta entre 12 a 25 PSI, entonces limpiar alojamiento y valvula de alivio del circuito de aceite, llave allen cerca de filtro de aceite")
                    print("5. Si presion de aceite en analizador es igual a 0 PSI, hay problemas con cableado o sensor")
                    print("6. Mida continuidad entre modulo de motor y sensor de cableado o intente con otro sensor")

                elif selected_option == 6:
                    print("1. Revisar en que funciones motor se apaga comparar presiones hidraulicas. Funciones mayor exigencia brazo torre y brazo principal")
                    print("2. Si motor se apaga con una sola funcion a la vez, revisar linea de combustible - Aire")
                    print("3. Revisar que acelerador manual, no ha sido intervenido, recorrido del perno debe tener marca de pintura por Deutz, comparar con equipo operativo recorrido del perno")
                    print("4. Si motor se apaga durante la realizacion de dos funciones a la vez o en traccion en conejo con pendiente, revisar comprension de cilindros de motor")
                    print("5. Si equipo se encuentra en altura geografica sobre 3500 msnm, derratear bomba hidraulica de funciones, reducir presion de trabajo de 2600PSI a 2200PSI")

                elif selected_option == 7:
                    print("1. Esta condición se llamada ""Wet Stacking"", sucede cuando motor trabaja en baja carga para motores D2011, se indica procedimiento de asentamiento de motor añadiendo carga al motor")
                    print("2. Limpiar fuga de aceite por multiple de escape")
                    print("3. Identificar valvula hidraulica de liberacion de freno")
                    print("4. Desacoplar bobina electrica de freno, de esta manera el equipo no detectara falla por circuito abierto")
                    print("5. Pasar a control plataforma, dar arranque y conectar analizador JLG en plataforma, ingresar a Diagnostics --> Engine --> Actual Speed RPM")
                    print("6. Seleccion modo de traslado, conejo con pendiente")
                    print("7. Con joystick derecho, hacer funcion de traccion hacia adelante levemente y dejar motor entre 2500 y 2600 RPM")
                    print("8. Lo anterior hacerlo en lapsos de 2 minutos en un total de 30 minutos de prueba")
                    print("9. Si observamos que la fuga continua, hacer los pasos 7 y 8 por otros 30 minutos")
                    print("10. Si luego de los pasos anteriores sigue fugando, se debe contactar a Deutz para rectificar motor")

                else:
                    print("Invalid option!")
            if failure == "Hidraulica":
                if selected_option == 1:
                    print("1. Conecte en el puerto MP del bloque hidraulico principal")
                    print("2. Verifique que la presion de reserva tenga un valor de entre 400 PSI a 500PSI, y la presion de alta sea de 3200PSI.")
                    print("3. Si al momento de realizar una funcion no eleva la presion entonces revisar valvula Dump de bloque principal y valvula Dump de bloque de plataforma")
                    print("4. Revisar Spool de ambas valvulas y resistencia electrica de solenoide, valor de referencia 7.2 Ohms")
                    print("5. Si los valvulas Dump estan bien, entonces es posible que exista una fuga interna por Swivel, bloquear puerto B, que es el puerto de salida del bloque hacia el swivel. Si ahora tiene presion entonces debe cambiar sellos de Swivel")
                    print("6. Si no tiene presion aun bloqueado el puerto B, puede que bomba de funciones esta dañada, desconecte mangueras de la bomba y verifique que no exista partes estrucurales")
                    # Add more steps as needed
                elif selected_option == 2:
                    print("1. Si motor parte acelerado, puede deberse a que la presion de reserva es sobre los 500 PSI.")
                    print("2. Conecte medidor de presion hidraulico en puerto MP de bloque principal y puerto MP de bloque de plataforma")
                    print("3. Si la presion es alta en ambos lados, revisar valvula Dump de plataforma, si la presion es alta en bloque principal, verifique que valvula antiretorno de bomba auxiliar esta funcionando correctamente")
                    print("4. Si lo anterior esta OK entonces existe una obstruccion en la linea de retorno. Levantar linea T2 que viene de Swivel, si presion se normaliza, entonces hay problemas de sello de Swivel")
                    print("5. Si sigue teniendo exceso de presion, entonces puede ser que bloque hidraulico este fracturado, ideal separar bloque principal (aluminio), del cuerpo de valvulas PVG, ya que comparten la linea de retorno. Es permite cambiar no todo el conjunto en caso de fractura")
                    # Add more steps as needed
                elif selected_option == 3:
                    print("1. Entender que falla BCS hidraulica hace referencia a componentes electricos o hidraulicos de los movimientos criticos para la seguridad en el envelope de trabajo, por lo tanto entender circuito hidraulico de Tower, Tele Tower y Main Lift")
                    print("2. Revisar en Menu de fallas que no exista algun falla de Open Circuit de Valve enable pilot y valves enable, las de pilotaje se encuentran a la derecha superior mirando de frente al bloque y las valvula Enable se encuentran en la parte superior del bloque hidraulica, se observan bloques independientes")
                    print("3. Revisar que sensores y switches esten en los valores correctos con maquina Stowed, calibre las PVG, verifique el cambio de luces, calibracion con motor apagado, si la calibracion falla puede ser debido a problemas de alimentacion o conexion de CAN BUS de PVGs, intercambie la conexion y vea si la falla de calibracion cambia valvula, si cambie el problema es el servo de la PVG, si no cambia el nombre es el cableado")
                    print("4. Con lo anterior OK, tenga las claves de modo de servicio proximos a usted, intente generar la falla. Si la falla ocurre durante movimiento Tower-Teletower verificar si algun sensor o switch pierde conexion, si la falla ocurre en un punto en especifico, puede haber daños en bomba de funciones, debido a que el flujo hidraulico no es suficiente, generado falla Envelope Encroached")
                    # Add more steps as needed
                elif selected_option == 4:
                    print("1. Conectar analizador, Diagnostico --> Drive, verificar que modulo identifique, hacia adelante 100% y reversa 100% y verifique que Brake status cambie de Locked a Released")
                    print("2. Verificar conexiones correcta de bobinas de Drive en bomba drive lado derecho y bomba Drive lado izquierdo, valores de resistencia, bomba rexthrot 5.8 ohms, bomba Danfoss 3.8 ohms")
                    print("3. Conecte reloj hidralico en puerto MP de bloque de traccion, con motor en ralenti y en alta deberia dar un valor entre 400PSI y 500PSI, que es necesario para liberar frenos hidraulicos")
                    print("4. Si presion es inferior a 300 PSI revisar bobina de freno y valvula de alivio ubicado en bloque de traccion")
                    print("5. Si la presion esta Ok, remueva Spool de valvula de freno, revise sellos, limpie valvula y alojamiento. Vea si recupera Drive")
                    print("6. Si todo lo anterior esta OK, alta probabilidad de daños en sellos dde swivel")

                elif selected_option == 5:
                    print("1. Conectar analizador, Diagnostico --> Steer, verificar que modulo identifique, hacia derecha 100% e izquierda 100% y verifique que Brake status cambie de Locked a Released")
                    print("2. Conecte reloj hidralico en puerto MP de bloque de traccion, con motor en ralenti y en alta deberia dar un valor entre 400PSI y 500PSI, que es necesario para liberar frenos hidraulicos")
                    print("3. Si presion es inferior a 300 PSI revisar bobina de freno y valvula de alivio ubicado en bloque de traccion")
                    print("4. Si la presion esta Ok, remueva Spool de valvula de freno, revise sellos, limpie valvula y alojamiento")
                    print("5. Remueva valvula de direccion, la cual piloteada internamente, revise sellos y alojamiento")
                    print("6. Si esta todo OK, alta probabilidad que exista daño en sellos de Swivel")

                elif selected_option == 6:
                    print("1. Revisar que No nivele desde control tierra y desde control plataforma, si solo arroja la falla desde un comando. revisar valores de personalidades y calibraciones de CrackPoint, modificar valores y volver a calibrar")
                    print("2. verificar si arroja la falla de perdida de nivel, cuando el brazo principal sube o cuando brazo principal baja, esto ayudara a identificar los parametros que puedan requerir modificacion, tanto de personalidad como de crackpoint")
                    print("3. Conectar analizador, Diagnostico --> Boom Functions, verificar que modulo identifica correctamente nivel de platafoma UP and Down")
                    print("4. Conectar reloj hidraulico en puertos de M1 y M2, presion en M1 debe ser 3000psi, presion en M2 debe ser 2500psi, si valores estan invertidos, entonces las mangueras hidraulicas estan mal conectadas, en caso de que los valores no sean exactos, calibrar valvulas de alivio, revisar plano hidraulico")
                    print("5. Si valores de presion estan OK, revisar resistencia electrica de bobina de nivelacion debe ser de 10 ohms")
                    print("6. Si valor de resistencia esta OK, intercambiar Spool con giro de plataforma, son igual, verificar movimiento")
                    print("7. Revisar sellos de cilindro, cambiar en caso de que aplique")

                elif selected_option == 7:
                    print("1. Los movimientos espasmodisco existen debido a una discordancia entre valores de crackpoint y valores de personalidad, por lo general ocurren cuando hay mas de un movimiento involucrado")
                    print("2. Hacer movimientos desde control tierra y control plataforma, este ultimo con potenciometro en valocidad Creep, 50% y full, si da en algunos casos, alta probabilidad que sean parametros incorrectos, revisar con manual de servicio")
                    print("3. Si valores estan OK, entonces se debe confirmar que las presiones sean de acuerdo al manual de servicio, si sigue dando la condicion entonces eleve las presiones del movimientos con problemas en unos 200PSI.")
                    print("4. Revisar valores de resistencia electrica de las bobinas de los movimientos que presetan la condicion")
                    print("5. Hacer mantenimiento a Spools de movimientos que presentan condicion, cambiar en caso de falla")
                    print("6. Si todo lo anterior esta OK, revisar flujo hidraulico de bomba de funciones")
        
                else:
                    print("Invalid option!")

            if failure == "Electrica":
                if selected_option == 1:
                    print("1. BCS - Electrico es una falla que siempre se presenta con otras fallas mostradas por analizador, identificar las fallas por ejemplo. Si hay falla en sensores de Tower lift, Tele-tower y Main lift o en Switches de transporte")
                    print("2. Si equipo esta completamente replegado, Conectar analizador --> Diagnostico y dejar registro de los siguientes Menu. Transport Data, Boom Sensors, Boom Switches, BCS, confirmar que valor esta fuera de rango de acuerdo a los parametros pre determinados que debe tener el equipo replegado")
                    print("3. BCS electrico tambien puede generarse por problemas en linea CAN BUS o alimentacion de modulos, revisar falla de CAN Bus 1")
                    print("4. Si equipo replegado no presenta falla, elevar y sacar telescopico de brazos de equipo hasta que genere la falla, buscar otras fallas presentes como Lost Communications, out of range o Disagrement")
                    print("5. Si aparece Lost Communications de algun sensor, significa que cable se estira y desconecta complemente el sensor, si apare Out of range high o low, significa que se pierde conexion de Positivo o tierra respectivamente, si aparece Disagreement significa que switch componente mecanico o electrico se encuentra defectuoso, siempre comprobar estado de sensores y switches")
                    print("6. Si la falla ocurre cuando la plataforma esta en proceso de elevacion, significa que cableado puede estar en mal estado debido al esfuerzo mecanico, existe una alta probabilidad que conexion Y que se encuentra en codo de union de Tower-Main este defectuosa o conexion en articulacion de JIB. Conectar analizador Diagnostico --> System, verficar que voltaje de Modulo de plataforma se mantenga estable")
                    print("7. Si la falla continua y no se aprecia errores de Sensores/switches, proceder a realizar procedimiento de Unlock Boom, si aparece el mensaje Check Faults, significa que tiene presente una falla fisica, es decir cableado o sensores, tambien puede aparecer Calibration required, y requiere volver a calibrar equipo. Si equipo permite continua con procedimiento, completar paso a paso indicado por analizador")
                    print("8. Si falla continua, puede explicarse por problemas hidraulicos en cilindro de Tower, Tele Tower o Main Lift. Revisar en historial de fallas si hay presenta codigos de Encroached puede ser problemas con sellos de cilindros o valvulas de retencion, hacer prueba de drift de cilindros")
                    # Add more steps as needed
                elif selected_option == 2:
                    print("1. Las fallas CAN Bus pueden presentarse en el equipo por problemas de alimentacion o cableado del CAN bus")
                    print("2. Conectar analizador, diagnosticos --> System, revisar voltaje de modulo de tierra y modulo de plataforma, si modulo de plataforma muestra 25V, signfica que no esta llegando alimentacion a modulo y sistema dara falla de CAN BUS de plataforma o falla de LSS CAN BUS")
                    print("3. Para identificar que modulo no tiene comunicacion CAN Bus, conectar analizador, Diagnostic --> Versions, revisar que modulo aparece con simbolo de interrogacion, eso identifica el modulo perdido")
                    print("4. Revisar parametros de CAN BUS, diagnostic --> CAN Statistics, valores correctos RX: 650 Approx, TX: 288 Approx, BUS OFF, PASSIVE y MSG Error = 0, Si algun valor es diferente, revisar conexiones de CAN BUS como conectores T o derivadores, remover exceso de dielectrico o suciedad")
                    print("6. Si solo tienes falla de CAN Bus de modulo de chasis, alta probabilidad que este fallando alimentacion que viene de bateria, a traves de un Rele que se ubica detras de bomba auxiliar")
                    print("7. Si con analizador, no es posible identificar origen de CAN BUS, usando un tester y con maquina apagada, Medir en conector T ubicado en control tierra. Verificar conector que va hacia modulo de tierra con protector verde. Desconectar y medir hacia circuito. Medir entre A y B deberia dar 60 ohms y medir resistencia entre CAN H y CAN L con Shield debe dar resistencia en Mega Ohms o marcar OL, en caso de tener 120 ohms, cable esta cortado, en caso de tener continuidad o baja resistencia de CAN con Shield debe cambiar o reparar cableado")
                    print("8. Otra forma de revisar CAN BUS es revisar si alguna carga distorsiona valores, por lo tanto con analizador verificar si desconectado los siguientes componentes las fallas se borran, por ejemplo desconectar Valvulas PVG, PIN Load, MDI, Displays de tierra y plataforma, Sensor de peso LSS, Main angle 1 y 2, si las fallas se borran es posible que carga este dañada")
                    print("9. ")
                    print("10. Check air intake system.")
                    # Add more steps as needed
                elif selected_option == 3:
                    print("1. Check oil pressure gauge.")
                    print("2. Inspect oil filter.")
                    print("3. Test oil pressure sensor.")
                    # Add more steps as needed
                else:
                    print("Invalid option!")