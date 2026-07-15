import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/eventos.log",
    level=logging.INFO,
    encoding="utf-8",
    format="%(asctime)s | %(levelname)s | %(message)s"
)


class Logger:

    @staticmethod
    def info(mensaje):
        logging.info(str(mensaje))

    @staticmethod
    def warning(mensaje):
        logging.warning(str(mensaje))

    @staticmethod
    def error(mensaje):
        logging.error(str(mensaje))

    @staticmethod
    def critical(mensaje):
        logging.critical(str(mensaje))