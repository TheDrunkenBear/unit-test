def get_user() -> dict[str, any]:
    """Возвращает словарь с информацией о пользователе"""
    return {"name": "Алёша Попович", "age": 30}


if __name__ == "__main__":
    print(get_user())
