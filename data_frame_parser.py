from collections.abc import Callable
from copy import deepcopy
from typing import Any, List, Mapping
from pandas import DataFrame, read_csv

from attr_transform import AttrTransform


class DataFrameParser:
    def __init__(self, path_to_dataset: str,
                 attrs_to_rename: Mapping[str, str],
                 attrs_transform: List[AttrTransform],
                 attrs: List[str],
                 target: str) -> None:

        self.attrs_to_rename: Mapping[str, str] = attrs_to_rename
        self.attrs_transform: List[AttrTransform] = attrs_transform
        self.attrs: List[attrs] = attrs
        self.target: str = target
        self.path_to_dataset: str = path_to_dataset

        self.df: DataFrame = None
        self.attrs_df: DataFrame = None
        self.full_attrs_df: DataFrame = None

    def parse(self):
        self.df = read_csv(self.path_to_dataset)
        self.__rename_attrs()
        self.__transform_attrs()
        self.__set_attrs()

    def __rename_attrs(self) -> None:
        self.df.rename(columns=self.attrs_to_rename, inplace=True)

    def __transform_attrs(self) -> None:
        for attr_transform in self.attrs_transform:
            self.df[attr_transform.name] = self.df[attr_transform.name].apply(attr_transform.func)

    def __set_attrs(self) -> None:
        self.attrs_df = self.df[self.attrs]

        full_attrs: List[str] = deepcopy(self.attrs)
        full_attrs.append(self.target)

        self.full_attrs_df = self.df[full_attrs]

    def get_data_frame(self) -> DataFrame:
        return self.df

    def get_attrs_data_frame(self) -> DataFrame:
        return self.attrs_df

    def get_full_attrs_data_frame(self) -> DataFrame:
        return self.full_attrs_df
