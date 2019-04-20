DATA_BASE = "localHost"
DB_NAME = "celulares"
COLLECTION = "celulares"

# Fintros para la Query
MY_QUERY = {"provincia": "SANTA FE", "$or": [{"localidad": "Fray Luis Beltran"},
                                             {"localidad": "FRAY LUIS BELTRAN"},
                                             {"localidad": "PUERTO GRAL SAN MARTIN"},
                                             {"localidad": "CAPITAN BERMUDEZ"},
                                             ]}
# Provincia para Cuendo se carga un csv con las localidades
LOCALIDAD = "SANTA FE"

# Nombre de csv. Recordar que si no se cambia se pisa el anterior
NAME_CSV_CELULARES = "CelularesMacri"
NAME_CSV_FIJOS = "FijosMacri"

# My sql database
HOST = "localhost",
USER = "admin",
PASSWORD = ""
DATA_BASE_SQL = "fijos"

# ACTIVOS
CELULARES = "ACTIVO"
FIJOS = "ACTIVO"
