#!
# -*- coding: utf-8 -*-
"""
Created on 2021-03-13
@author: Edmund Bennett
@email: edmund.bennett@ghd.com
"""

from dnd.api.content import Content


class EquipmentCategory:
    def __init__(
        self,
        index,
        name,
        url,
        unparsed_equipment=None,
    ):
        self.index = index
        self.name = name
        self.url = url
        self.unparsed_equipment = unparsed_equipment
        self.equipment = []

    @staticmethod
    def parse_summary(input_dict):
        return EquipmentCategory(
            index=input_dict["index"],
            name=input_dict["name"],
            url=input_dict["url"],
        )

    @staticmethod
    def parse_detail(input_dict):
        return EquipmentCategory(
            index=input_dict["index"],
            name=input_dict["name"],
            url=input_dict["url"],
            unparsed_equipment=input_dict["equipment"],
        )

    def get_details(self, content_api: Content):
        if self.index:
            return EquipmentCategory.parse_detail(content_api.get_detail(self.url))

    def get_equipment(self, content_api: Content):
        from dnd.dto.equipment import Equipment
        if self.unparsed_equipment is not None:
            for unparsed_equipment in self.unparsed_equipment:
                self.equipment.append(Equipment.parse_summary(unparsed_equipment).get_details(content_api))


    def __str__(self):
        return f"{self.name}"


if __name__ == "__main__":
    pass
