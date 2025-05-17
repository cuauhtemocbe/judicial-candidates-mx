# app/data.py

analistas_data = {
    "fabrizio": {
        "mujeres": [
            {"numero": "03", "nombre": "Lenia Batres Guadarrama", "razones": "Militante de izquierda, defensora de comunidades indígenas, opuesta a maniobras de Norma Piña."},
            {"numero": "26", "nombre": "María Estela Ríos González", "razones": "Abogada de los trabajadores y de AMLO, comprometida con causas sociales."},
            {"numero": "17", "nombre": "Ana María Ibarra Olguín", "razones": "Cercana a Zaldívar y Romero, alineada con el proyecto de Nación."},
            {"numero": "31", "nombre": "Natalia Téllez Torres Orozco", "razones": "Jurídica de Raquel Buenrostro, defensora del interés público en materia fiscal."},
            {"numero": "09", "nombre": "Fabiana Estrada", "razones": "Trayectoria en derechos humanos, comprometida con justicia social."}
        ],
        "hombres": [
            {"numero": "12", "nombre": "Gilberto Batiz García", "razones": "Respaldado por el Ejecutivo, con compromiso en justicia electoral."},
            {"numero": "19", "nombre": "Luis Enrique Rivero Carrera", "razones": "Trayectoria sólida en el ámbito judicial, defensor de la legalidad."},
            {"numero": "25", "nombre": "Manuel Vizcarra", "razones": "Experiencia judicial, comprometido con la justicia social."},
            {"numero": "16", "nombre": "Ernesto Castillo Torres", "razones": "Enfocado en derechos humanos, con visión de interés público."},
            {"numero": "22", "nombre": "Arturo Medel", "razones": "Conocido por su integridad, defensor de causas sociales y la legalidad."}
        ]
    },
    "viridiana": {
        "mujeres": [
            {"numero": "06", "nombre": "Selene Cruz Alcalá", "razones": "Defensora de los trabajadores, justicia transformadora, cercana y con perspectiva social."},
            {"numero": "31", "nombre": "Natalia Téllez Torres Orozco", "razones": "Experta en justicia fiscal, combate a la corrupción, enfoque social y derechos humanos."},
            {"numero": "01", "nombre": "Olivia Aguirre Bonilla", "razones": "Académica con enfoque en derechos humanos, justicia accesible, lenguaje claro y humano."},
            {"numero": "05", "nombre": "Marisol Castañeda Pérez", "razones": "Magistrada con visión ética y social, enfoque en equidad de género y transparencia."},
            {"numero": "13", "nombre": "Alma Delia González Centeno", "razones": "Propuesta de reforma judicial con evaluación periódica, acceso a justicia para todos."}
        ],
        "hombres": [
            {"numero": "40", "nombre": "Isaac De Paz González", "razones": "Visión transformadora y justicia social; doctorado en derechos fundamentales; independiente de partidos."},
            {"numero": "57", "nombre": "Carlos Enrique Odriozola", "razones": "Defensa histórica de derechos humanos; trayectoria ciudadana y visión crítica del sistema judicial."},
            {"numero": "38", "nombre": "Edgar Corzo Sosa", "razones": "Experiencia internacional en derechos migrantes; impulsa justicia cercana y con sentido social."},
            {"numero": "55", "nombre": "Sergio Javier Molina Martínez", "razones": "Clave en la reforma laboral; visión sensible y centrada en derechos colectivos y justicia cercana al pueblo."},
            {"numero": "42", "nombre": "Raymundo Espinoza Hernández", "razones": "Defensa del medio ambiente; busca una Corte con justicia social efectiva y democrática."},
            {"numero": "62", "nombre": "Antonio Sorela Castillo", "razones": "Enfoque en interculturalidad y derechos humanos; experiencia internacional y académica."},
            {"numero": "46", "nombre": "Angel Mario García Guerra", "razones": "Crítica directa a jurisprudencia regresiva; propone revisión integral y justicia accesible."}
        ]
    },
    "pedrero": {
        "mujeres": [
            {"numero": "03", "nombre": "Lenia Batres", "razones": "Consecuente, joven, símbolo de renovación, ha votado en favor del pueblo."},
            {"numero": "08", "nombre": "Yasmín Esquivel", "razones": "A pesar de polémicas, se prefiere evitar la fragmentación del voto que daría paso a peores perfiles."},
            {"numero": "22", "nombre": "Loreta Ortiz", "razones": "Misma razón que Yasmín: evitar que entren perfiles más cuestionables como Maricela Morales o Suema Mosri."},
            {"numero": "26", "nombre": "María Estela Ríos", "razones": "Fue consejera jurídica de AMLO, abogada de confianza, perfil vinculado a la 4T."},
            {"numero": "31", "nombre": "Natalia Télez Torres Orozco", "razones": "Perfil limpio, magistrada laboral pro-trabajadores, avalada por Raquel Buenrostro."}
        ],
        "hombres": [
            {"numero": "34", "nombre": "Hugo Aguilar Ortiz", "razones": "Representante indígena, oaxaqueño, sin escándalos, perfil limpio."},
            {"numero": "36", "nombre": "Federico Anaya Gallardo", "razones": "Defensor de derechos humanos en Chiapas, ideología clara de izquierda."},
            {"numero": "40", "nombre": "Isaac de Paz González", "razones": "Catedrático del norte del país, académico, campaña austera."},
            {"numero": "49", "nombre": "César Gutiérrez Priego", "razones": "Abogado penalista, cercano al pueblo, perfil reivindicativo por la historia de su padre, oposición a regímenes autoritarios."}
        ]
    }
}

resumen_candidatos = {
    "mujeres": [
        {"numero": "03", "nombre": "Lenia Batres Guadarrama", "analistas": ["Fabrizio", "Manuel"]},
        {"numero": "26", "nombre": "María Estela Ríos González", "analistas": ["Fabrizio", "Manuel"]},
        {"numero": "31", "nombre": "Natalia Téllez Torres Orozco", "analistas": ["Fabrizio", "Viridiana", "Manuel"]},
        {"numero": "06", "nombre": "Selene Cruz Alcalá", "analistas": ["Viridiana"]},
        {"numero": "01", "nombre": "Olivia Aguirre Bonilla", "analistas": ["Viridiana"]},
        {"numero": "05", "nombre": "Marisol Castañeda Pérez", "analistas": ["Viridiana"]},
        {"numero": "13", "nombre": "Alma Delia González Centeno", "analistas": ["Viridiana"]},
        {"numero": "08", "nombre": "Yasmín Esquivel", "analistas": ["Manuel"]},
        {"numero": "22", "nombre": "Loreta Ortiz", "analistas": ["Manuel"]},
        {"numero": "09", "nombre": "Fabiana Estrada", "analistas": ["Fabrizio"]},
        {"numero": "17", "nombre": "Ana María Ibarra Olguín", "analistas": ["Fabrizio"]}
    ],
    "hombres": [
        {"numero": "40", "nombre": "Isaac De Paz González", "analistas": ["Viridiana", "Manuel"]},
        {"numero": "12", "nombre": "Gilberto Batiz García", "analistas": ["Fabrizio"]},
        {"numero": "19", "nombre": "Luis Enrique Rivero Carrera", "analistas": ["Fabrizio"]},
        {"numero": "25", "nombre": "Manuel Vizcarra", "analistas": ["Fabrizio"]},
        {"numero": "16", "nombre": "Ernesto Castillo Torres", "analistas": ["Fabrizio"]},
        {"numero": "22", "nombre": "Arturo Medel", "analistas": ["Fabrizio"]},
        {"numero": "34", "nombre": "Hugo Aguilar Ortiz", "analistas": ["Manuel"]},
        {"numero": "36", "nombre": "Federico Anaya Gallardo", "analistas": ["Manuel"]},
        {"numero": "49", "nombre": "César Gutiérrez Priego", "analistas": ["Manuel"]},
        {"numero": "57", "nombre": "Carlos Enrique Odriozola", "analistas": ["Viridiana"]},
        {"numero": "38", "nombre": "Edgar Corzo Sosa", "analistas": ["Viridiana"]},
        {"numero": "55", "nombre": "Sergio Javier Molina Martínez", "analistas": ["Viridiana"]},
        {"numero": "42", "nombre": "Raymundo Espinoza Hernández", "analistas": ["Viridiana"]},
        {"numero": "62", "nombre": "Antonio Sorela Castillo", "analistas": ["Viridiana"]},
        {"numero": "46", "nombre": "Angel Mario García Guerra", "analistas": ["Viridiana"]}
    ]
}

