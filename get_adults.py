def get_adults(users):
    adults=[]
    for u in users:
        name=u.get('name')
        age=u.get('age')
        if age>18:
            adults.append(name)
    return adults
