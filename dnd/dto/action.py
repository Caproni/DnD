#!
# -*- coding: utf-8 -*-
"""
Created on 2021-03-13
@author: Edmund Bennett
@email: edmund.bennett@ghd.com
"""


class Action:
    def __init__(
        self,
        name,
        description,
        damage,
        options=None,
        dc=None,
    ):
        self.name = name
        self.options = options
        self.dc = dc
        self.description = description
        self.damage = damage

    @staticmethod
    def parse(input_dict):
        return Action(
            name=input_dict["name"],
            options=input_dict["options"] if "options" in input_dict.keys() else None,
            dc=input_dict["dc"] if "dc" in input_dict.keys() else None,
            description=input_dict["desc"],
            damage=input_dict["damage"],
        )


    def __str__(self):
        return f"{self.name}"


if __name__ == "__main__":
    pass
