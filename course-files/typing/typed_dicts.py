from typing import NotRequired, TypedDict


class User(TypedDict):
    id: int
    name: str
    email: str
    phone: NotRequired[str]


user: User = {
    "id": 123,
    "name": "Alice",
    "email": "alice@example.com",
}

print(f"User data: {user.get('email')}")
