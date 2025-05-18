def get_user() -> dict[str, any]:
    """Возвращает словарь с информацией о пользователе"""
    return {"name": "Алёша Попович", "age": 30, "gender": "m", "salary": 54000}


if __name__ == "__main__":
    print(get_user())
