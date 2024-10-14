from data_frame_parser import DataFrameParser
from node import Node

class IdTree:
    def __init__(self, data_frame_parser: DataFrameParser) -> None:
        self.root: Node = Node()
        self.data_frame_parser: DataFrameParser = data_frame_parser

    def build(self) -> None:
        pass