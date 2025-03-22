class FieldIndexError(IndexError):
    """Выбрасывается, если выбрано значение вне поля."""
    def __init__(self, message='Out of field bound'):
        super().__init__(message)


class CellOccupiedError(Exception):
    def __init__(self, message='Cell is busy!'):
        super().__init__(message)
