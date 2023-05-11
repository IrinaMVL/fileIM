from pydantic import BaseModel


class Car(BaseModel):
    name: str
    model: str
    engine: float
    owner_phonenumber: str


data = {
    'name': 'Toyota',
    'model': 'Rav4',
    'engine': 2.4,
    'owner_phonenumber': '+375295711010'
}
car = Car(**data)
print(car)

