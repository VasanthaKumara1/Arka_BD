def get_adults(users):
    """
    Return a list of names for users older than 18.

    Args:
        users (list[dict]): List of user dictionaries. Each dictionary is expected
            to have at least the keys 'name' and 'age'.

    Returns:
        list[str]: Names of users whose age is strictly greater than 18.
    """
    adults = []
    for u in users:
        name = u.get('name')
        age = u.get('age')
        # Validate types and age
        if isinstance(name, str) and isinstance(age, (int, float)) and age > 18:
            adults.append(name)
    return adults


if __name__ == '__main__':
    sample_users = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 18},
        {'name': 'Charlie', 'age': 19},
        {'name': 'Dana', 'age': 'twenty'},
        {'name': None, 'age': 25},
    ]

    print(get_adults(sample_users))  # Expected: ['Alice', 'Charlie']