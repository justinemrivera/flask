class Dog:


me = {
    "name": "Justine",
    "last": "Rivera",
    "email": "test@mail.com",
    "age": 30,
    "hobbies": [],
    "address": {
            "street": "main",
            "number": "42"
    }
}


def print_data():
    print(me["name"])
    print(me["name"] + " " + me["last"])

    print_data()
