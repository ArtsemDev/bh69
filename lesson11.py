from abc import ABC, abstractmethod
from io import TextIOWrapper
from typing import Type, List, TypeVar

from pydantic import BaseModel, Field, PositiveInt
from pydantic.types import Decimal
from pydantic_core import ValidationError

Schema = TypeVar('Schema', bound=BaseModel)


class Parser(ABC):
    schema: Type[BaseModel]

    @classmethod
    @abstractmethod
    def parse(cls, file: TextIOWrapper, delimiter: str) -> List[Schema]:
        ...

    @classmethod
    @abstractmethod
    def dump(cls, objs: List[Schema], file: TextIOWrapper, delimiter: str) -> None:
        ...


class ProductDetail(BaseModel):
    title: str = Field(..., max_length=128)
    descr: str = Field(..., max_length=4096)
    price: Decimal = Field(..., max_digits=8, decimal_places=2)
    count: PositiveInt


class ProductParser(Parser):
    schema = ProductDetail

    @classmethod
    def dump(cls, objs: List[Schema], file: TextIOWrapper, delimiter: str) -> None:
        objs = [obj.model_dump() for obj in objs]
        fieldnames = delimiter.join(objs[0].keys())
        objs = [delimiter.join(f'{value}' for value in obj.values()) for obj in objs]
        objs.insert(0, fieldnames)
        file.write('\n'.join(objs))

    @classmethod
    def parse(cls, file: TextIOWrapper, delimiter: str) -> List[Schema]:
        fieldnames = file.readline().strip().split(delimiter)
        values = [line.strip().split(delimiter) for line in file]
        values = [dict(zip(fieldnames, value)) for value in values]
        data = []
        for value in values:
            try:
                data.append(cls.schema(**value))
            except ValidationError:
                pass
        return data


with open('product.csv', 'r', encoding='utf-8') as file, open('product_dump.csv', 'w', encoding='utf-8') as file2:  # type: TextIOWrapper
    ProductParser.dump(ProductParser.parse(file=file, delimiter='|'), file=file2, delimiter=';')
