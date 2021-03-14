#!
# -*- coding: utf-8 -*-
"""
Created on 2021-03-13
@author: Edmund Bennett
@email: edmund.bennett@ghd.com
"""

from dnd.api.content import Content


class Equipment:
    def __init__(
        self,
        index,
        name,
        url,
        cost=None,
        weight=None,
        contents=None,
        unparsed_gear_category=None,
        unparsed_equipment_category=None,
    ):
        self.index = index
        self.name = name
        self.url = url
        self.cost = cost
        self.weight = weight
        self.contents = contents
        self.unparsed_gear_category = unparsed_gear_category
        self.unparsed_equipment_category = unparsed_equipment_category

    @staticmethod
    def parse_summary(input_dict):
        return Equipment(
            index=input_dict["index"],
            name=input_dict["name"],
            url=input_dict["url"],
        )

    @staticmethod
    def parse_detail(input_dict):
        return Equipment(
            index=input_dict["index"],
            name=input_dict["name"],
            url=input_dict["url"],
            cost=input_dict["cost"],
            weight=input_dict["weight"] if "weight" in input_dict.keys() else None,
            contents=input_dict["contents"] if "contents" in input_dict.keys() else None,
            unparsed_gear_category=input_dict["gear_category"],
            unparsed_equipment_category=input_dict["equipment_category"],
        )

    def get_details(self, content_api: Content):
        if self.index:
            return Equipment.parse_detail(content_api.get_detail(self.url))


    def __str__(self):
        return f"{self.name}"


if __name__ == "__main__":
    pass
