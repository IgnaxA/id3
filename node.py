from typing import List, Self
from uuid import uuid4

class Node:
    def __init__(self) -> None:
        self.uuid = str(uuid4())
        self.name: int = None
        self.attr: str = None
        self.target_value: int = None
        self.question_informativeness: float = None
        self.answer_informativeness: float = None
        self.columns: List[str] = None
        self.parent: Self = None
        self.children: List[Self] = []

    def set_name(self, name: int) -> Self:
        self.name = name

        return self

    def set_attr(self, attr: str) -> Self:
        self.attr = attr

        return self

    def set_question_informativeness(self, informativeness: float) -> Self:
        self.question_informativeness = informativeness

        return self

    def set_answer_informativeness(self, informativeness: float) -> Self:
        self.answer_informativeness = informativeness

        return self

    def set_columns(self, columns: List[str]) -> Self:
        self.columns = columns

        return self

    def set_parent(self, parent: Self) -> Self:
        self.parent = parent

        return self

    def set_target_value(self, target_value: int) -> Self:
        self.target_value = target_value

        return self

    def append_child(self, child: Self | List[Self]) -> None:
        if isinstance(child, Node):
            self.children.append(child)
        else:
            self.children = self.children + child

    def get_columns(self) -> List[str]:
        return self.columns

    def get_target_value(self) -> int:
        return self.target_value

    def get_uuid(self) -> str:
        return self.uuid

    def get_name(self) -> str:
        name = ''
        if self.attr is not None:
            name += f'{self.attr}\n'
        if self.name is not None:
            name += f'{self.name}\n'
        if self.question_informativeness is not None:
            name += f'{self.question_informativeness}\n'
        if self.target_value is not None:
            name += f'{self.target_value}'
        return name