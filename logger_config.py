import logging

def setup_logger(name='my_logger', log_file='app.log', level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:  # Đảm bảo không tạo nhiều handler khi import nhiều lần
        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('[%(levelname)s] %(asctime)s - %(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
