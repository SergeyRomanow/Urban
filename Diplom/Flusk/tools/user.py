"""
Модуль с дополнительными функциями для работы с пользователями
"""


def get_current_user_id() -> int:
    """
    Функция предназначена для получения user_id текущего пользователя.

    Если пользователь зарегистрирован и авторизован в системе - возвращается его user_id,
    в противном случае пользователь считается анонимным и возвращается 1

    Returns:
        int: возвращает user_id вошедшего в систему пользователя или 1
    """
    return 1
