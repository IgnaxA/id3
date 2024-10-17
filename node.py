from typing import List, Self

class Node:
    def __init__(self) -> None:
        self.name: str = None
        self.attr: str = None
        self.target_value: int = None
        self.informativeness: float = None
        self.columns: List[str] = None
        self.parent: Self = None
        self.children: List[Self] = []

    def set_name(self, name: str) -> Self:
        self.name = name

        return self

    def set_attr(self, attr: str) -> Self:
        self.attr = attr

        return self

    def set_informativeness(self, informativeness: float) -> Self:
        self.informativeness = informativeness

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