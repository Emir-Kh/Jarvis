import logging
import os

# ساخت پوشه logs اگر وجود نداشت
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/jarvis.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger("JARVIS")


def info(message):
    logger.info(message)


def warning(message):
    logger.warning(message)


def error(message):
    logger.error(message)