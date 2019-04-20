DATA_BASE = "mongodb://soporte:soporte.3135@192.168.33.113/?authSource=celulares&authMechanism=SCRAM-SHA-1"
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
NAME_CSV_FIJOS = "FijosSeguridad"

# My sql database
HOST = "192.168.33.80",
USER = "soporte",
PASSWORD = "Soporte.3135"
DATA_BASE_SQL = "fijos"
