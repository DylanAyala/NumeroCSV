DATA_BASE = "localhost"
DB_NAME = "celulares"
COLLECTION = "celulares"

# Fintros para la Query
MY_QUERY = {"provincia": "SANTA FE", "$or": [{"localidad": "Fray Luis Beltran"},
                                             {"localidad": "FRAY LUIS BELTRAN"},
                                             {"localidad": "PUERTO GRAL SAN MARTIN"},
                                             {"localidad": "CAPITAN BERMUDEZ"},
                                             ]}
# Nombre de csv. Recordar que si no se cambia se pisa el anterior
NAME_CSV_CELULARES = "CelularesMacri"
NAME_CSV_FIJOS = "FijosMacri"

# My sql database
HOST = "localhost",
USER = "root",
PASSWORD = ""
DATA_BASE_SQL = "fijos"
