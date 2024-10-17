import copy

import numpy as np
from pandas import DataFrame
from typing import List
from node import Node
from numpy import log2

# class IdTree:
#     def __init__(self, data_frame: DataFrame, target: str) -> None:
#         self.nodes: List[Node] = []
#         self.data_frame: DataFrame = data_frame
#         self.columns: List[str] = data_frame.columns.tolist()
#         self.target: str = target
#         self.entries_num: int = data_frame.shape[0]
#
#     def build(self) -> None:
#         current_node: Node = (Node()
#                                 .set_columns(columns=self.columns))
#
#         attribute, informativeness = self.__select_attribute(current_node)
#
#         (current_node.set_attr(attr = attribute)
#                      .set_informativeness(informativeness = informativeness))
#
#         child_node_columns = copy.deepcopy(current_node.get_columns())
#         child_node_columns.remove(attribute)
#
#         unique_values = self.data_frame[attribute].unique()
#
#         for value in sorted(unique_values, reverse=False):
#             new_node = copy.deepcopy(current_node)
#             new_node.set_name(value)
#             new_node.append_child(self.__build_recursively(new_node, copy.deepcopy(child_node_columns)))
#             self.nodes.append(new_node)
#
#     def __build_recursively(self, parent_node: Node, columns: List[str]) -> Node | List[Node]:
#         current_node: Node = (Node()
#                               .set_columns(columns=columns)
#                               .set_parent(parent=parent_node))
#
#         attribute, informativeness = self.__select_attribute(current_node)
#
#         (current_node.set_attr(attr=attribute)
#                      .set_informativeness(informativeness=informativeness))
#
#         child_node_columns = copy.deepcopy(current_node.get_columns())
#         child_node_columns.remove(attribute)
#
#         unique_values = self.data_frame[attribute].unique()
#
#         current_nodes: List[Node] = []
#         for value in sorted(unique_values, reverse=False):
#             new_node = copy.deepcopy(current_node)
#             new_node.set_name(value)
#             current_nodes.append(new_node)
#             if len(child_node_columns) != 0:
#                 new_node.append_child(self.__build_recursively(new_node, copy.deepcopy(child_node_columns)))
#
#         return current_nodes
#
#     def __select_attribute(self, node: Node) -> (str, float):
#         best_informativeness: float = None
#         best_attribute: str = None
#         for column in node.get_columns():
#             informativeness = self.__calculate_informativeness(column=column)
#
#             if best_informativeness is None or informativeness < best_informativeness:
#                 best_informativeness = informativeness
#                 best_attribute = column
#
#         return best_attribute, best_informativeness
#
#     def __calculate_informativeness(self, column: str) -> float:
#         unique_values = self.data_frame[column].unique()
#
#         informativeness_sum = 0.0
#         for value in unique_values:
#             entropy = self.__calculate_entropy(column=column, value=value)
#             informativeness_sum += entropy
#
#         informativeness = (1 / self.entries_num) * informativeness_sum
#
#         return informativeness
#
#
#     def __calculate_entropy(self, column: str, value: float) -> float:
#         values = self.data_frame.loc[self.data_frame[column] == value, self.target].tolist()
#         value_count = len(values)
#         coefficient = len(np.unique(values)) / value_count
#         entropy = coefficient * log2(coefficient)
#
#         return -entropy


class IdTree:
    def __init__(self, data_frame: DataFrame, target: str) -> None:
        self.nodes: List[Node] = []
        self.data_frame: DataFrame = data_frame
        self.columns: List[str] = data_frame.columns.tolist()
        self.target: str = target
        self.entries_num: int = data_frame.shape[0]

    def __select_feature_for_root_node(self, columns: List[str]) -> List[(str, float)]:
        best_informativeness: float = None
        best_attribute_name: str = None
        attrs_info: List[(str, float)] = []

        for column in columns:


        return attrs_info

    def build(self) -> None:
        node: Node = Node()
        node.set_columns(self.columns)

        self.__build_recursively(node)


    def __build_recursively(self, parent_node: Node) -> None:
        pass

    def __calculate_question_informativeness(self, features: List[str], prev_feat_name: str = None, prev_feat_value: int = None) -> (str, float, List[(str, float)]):
        best_informativeness: float = None
        best_attribute_name: str = None
        best_attributes_informativeness: List[(str, float)] = None
        for feature in features:
            unique_values = self.data_frame[feature].unique().tolist()
            informativeness_sum: float = 0.0
            attributes_informativeness: List[(str, float)] = []
            for value in unique_values:
                count, answer_informativeness = self.__calculate_answer_informativeness(feature, value, prev_feat_name, prev_feat_value)





    def __calculate_answer_informativeness(self, target_feat: str, target_value: int, prev_feat_name: str, prev_feat_value: int) -> (int, float, str):
        answer_informativeness: float = 0.0
        target_values: List[int] = []
        if prev_feat_name is None and prev_feat_value is None:
            target_values = self.data_frame.loc[self.data_frame[target_feat] == target_value, self.target].tolist()
        else:
            target_values = self.data_frame.loc[self.data_frame[target_feat] == target_value and self.data_frame[prev_feat_name] == prev_feat_value, self.target].tolist()

        target_values_count: int = len(target_values)
        coefficient: float = len(np.unique(target_values)) / target_values_count

        answer_informativeness = (log2(coefficient))
        return target_values_count, answer_informativeness
