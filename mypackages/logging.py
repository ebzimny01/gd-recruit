import logging
import datetime

logging.basicConfig(filename="recruitDB.log", level=logging.DEBUG)
logger = logging.getLogger("logger")


def logQueryError(query):
    logging.error(f"{datetime.datetime.now()}: query: last error: {query.lastError()}")
    logging.error(f"{datetime.datetime.now()}: query: last query: {query.lastQuery()}")