from pydantic import BaseModel


class Car(BaseModel):
    name: str
    model: str
    engine: float


data = {
    'name': 'Toyota',
    'model': 'Rav4',
    'engine': 2.4
}
car = Car(**data)

