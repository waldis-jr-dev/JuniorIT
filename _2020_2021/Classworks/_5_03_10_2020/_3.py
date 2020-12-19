def unpack(name, age):
    print(f"{name} : {age}")


data = {
    'age': 23,
    'name': 'Vlad',
}

unpack(**data)
