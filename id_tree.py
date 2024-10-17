import copy

import numpy as np
from numpy.ma.extras import unique
from pandas import DataFrame
from typing import List
from node import Node
from numpy import log2

class IdTree:
    def __init__(self, data_frame: DataFrame, target: str) -> None:
        self.nodes: List[Node] = []
        self.data_frame: DataFrame = data_frame
        self.columns: List[str] = data_frame.columns.tolist()
        self.target: str = target
        self.entries_num: int = data_frame.shape[0]

    def build(self) -> None:
        possible_features: List[str] = copy.deepcopy(self.columns)
        possible_features.remove(self.target)
        feature_name, feature_informativeness, nodes = self.__calculate_question_informativeness(possible_features)

        if nodes is None and feature_name is None and feature_informativeness is None:
            return

        for node_info in nodes:
            node: Node = Node()
            node.set_attr(feature_name)
            node.set_answer_informativeness(feature_informativeness)
            node.set_question_informativeness(node_info[1])
            node.set_name(node_info[0])
            node.target_value = node_info[2]

            if node_info[2] is not None:
                node.set_target_value(node_info[2])
                self.nodes.append(node)
                continue

            features: List[str] = copy.deepcopy(possible_features)
            features.remove(feature_name)

            self.nodes.append(node)
            node.append_child(self.__build_recursively(node, features))


    def __build_recursively(self, parent_node: Node, features: List[str]) -> Node | List[Node]:
        feature_name, feature_informativeness, nodes = self.__calculate_question_informativeness(features, parent_node.attr, parent_node.name)

        node_list: List[Node] = []

        if nodes is None and feature_name is None and feature_informativeness is None:
            return node_list

        for node_info in nodes:
            node: Node = Node()
            node.set_attr(feature_name)
            node.set_answer_informativeness(feature_informativeness)
            node.set_question_informativeness(node_info[1])
            node.set_name(node_info[0])
            if node_info[1] == 0:
                node.set_target_value(node_info[2])
                node_list.append(node)
                continue


            features_copied: List[str] = copy.deepcopy(features)
            features_copied.remove(feature_name)

            node.append_child(self.__build_recursively(node, features_copied))

            node_list.append(node)

        return node_list

    def __calculate_question_informativeness(self, features: List[str], prev_feat_name: str = None, prev_feat_value: int = None) -> (str, float, List):
        best_informativeness: float = None
        best_attribute_name: str = None
        best_attributes_informativeness: List[(str, float)] = None
        for feature in features:
            unique_values = self.data_frame[feature].unique().tolist()
            informativeness_sum: float = 0
            attributes_info: List[(str, float, str | None)] = []
            for value in unique_values:
                count, answer_informativeness, target = self.__calculate_answer_informativeness(feature, value, prev_feat_name, prev_feat_value)
                attributes_info.append((value, answer_informativeness, target))
                informativeness_sum += (count / self.entries_num) * answer_informativeness

            if best_attributes_informativeness is None or informativeness_sum < best_informativeness:
                best_attributes_informativeness = attributes_info
                best_attribute_name = feature
                best_informativeness = informativeness_sum

        return best_attribute_name, best_informativeness, best_attributes_informativeness

    def __calculate_answer_informativeness(self, target_feat: str, target_value: int, prev_feat_name: str, prev_feat_value: int) -> (int, float, str):
        target_values: List[int]
        if prev_feat_name is None and prev_feat_value is None:
            target_values = self.data_frame.loc[self.data_frame[target_feat] == target_value, self.target].tolist()
        else:
            target_values = self.data_frame.loc[(self.data_frame[target_feat] == target_value) & (self.data_frame[prev_feat_name] == prev_feat_value), self.target].tolist()

        target_values_count: int = len(target_values)

        answer_informativeness: float = 0
        for value in np.unique(target_values).tolist():
            coefficient: float = target_values.count(value)/target_values_count
            answer_informativeness +=  coefficient * log2(coefficient)

        target: int = None
        if answer_informativeness == 0 and len(target_values) != 0:
            target = unique(target_values).tolist()[0]
        return target_values_count, -answer_informativeness, target
