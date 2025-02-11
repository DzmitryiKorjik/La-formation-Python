import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="C:\\Users\\dmard\\Desktop\\Study\\La formation Python\\20250207\\app.log",
                    filemode="a",
                    format='%(asctime)s : %(levelname)s : %(message)s')

logging.debug("La fonction a bien été exécutée")
logging.info("Message d'information général")
logging.warning("Attention !")
logging.error("Une erreur")
logging.critical("Erreur critical")