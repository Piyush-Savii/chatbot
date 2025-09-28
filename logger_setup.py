# logger_setup.py
import os
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv("ENV", "LOCAL").lower()
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
BOT_NAME = os.getenv("BOT_NAME", os.getenv("CHATBOT_NAME", "chatbot")).lower()

# Get (or create) a named logger
logger = logging.getLogger(BOT_NAME)
logger.setLevel(getattr(logging, LOG_LEVEL, logging.INFO))
logger.propagate = False  # don't double-log via root

# If uvicorn reloads, avoid adding handlers again
if not logger.handlers:
    # Common formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    # Always log to console (stdout) — required for Cloud Run
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, LOG_LEVEL, logging.INFO))
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # In local/dev, also log to a rotating file
    if ENV in ("LOCAL", "DEV"):
        # logs directory relative to this file (stable regardless of CWD)
        base_dir = os.path.dirname(__file__)
        log_dir = os.path.join(base_dir, "logs")
        os.makedirs(log_dir, exist_ok=True)
        log_file = os.path.join(log_dir, "slackbot.log")

        file_handler = RotatingFileHandler(
            log_file, maxBytes=5_000_000, backupCount=3, encoding="utf-8"
        )
        file_handler.setLevel(getattr(logging, LOG_LEVEL, logging.INFO))
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    # Now that handlers exist, this will actually emit
    logger.info("Logging initialized | env=%s | level=%s | bot=%s", ENV, LOG_LEVEL, BOT_NAME)
