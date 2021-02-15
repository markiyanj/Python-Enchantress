from dataclasses import dataclass


@dataclass
class User:
    _id: int
    name: str
    email: str
