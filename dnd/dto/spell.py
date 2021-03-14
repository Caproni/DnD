#!
# -*- coding: utf-8 -*-
"""
Created on 2021-03-13
@author: Edmund Bennett
@email: edmund.bennett@ghd.com
"""

from dnd.api.content import Content


class Spell:
    def __init__(
        self,
        index,
        name,
        url,
        attack_type=None,
        dc=None,
        casting_time=None,
        classes=None,
        components=None,
        concentration=None,
        damage=None,
        description=None,
        duration=None,
        higher_level=None,
        level=None,
        material=None,
        range=None,
        ritual=None,
        school=None,
        subclasses=None,
    ):
        self.index = index
        self.name = name
        self.url = url
        self.attack_type = attack_type
        self.dc = dc
        self.casting_time = casting_time
        self.classes = classes
        self.components = components
        self.concentration = concentration
        self.damage = damage
        self.description = description
        self.duration = duration
        self.higher_level = higher_level
        self.level = level
        self.material = material
        self.range = range
        self.ritual = ritual
        self.school = school
        self.subclasses = subclasses

    @staticmethod
    def parse_summary(input_dict):
        return Spell(
            index=input_dict["index"],
            name=input_dict["name"],
            url=input_dict["url"],
        )

    @staticmethod
    def parse_detail(input_dict):
        return Spell(
            index=input_dict["index"],
            name=input_dict["name"],
            url=input_dict["url"],
            attack_type=input_dict["attack_type"] if "attack_type" in input_dict.keys() else None,
            dc=input_dict["dc"] if "dc" in input_dict.keys() else None,
            casting_time=input_dict["casting_time"],
            classes=input_dict["classes"],
            components=input_dict["components"],
            concentration=input_dict["concentration"],
            damage=input_dict["damage"] if "damage" in input_dict.keys() else None,
            description=input_dict["desc"],
            duration=input_dict["duration"],
            higher_level=input_dict["higher_level"] if "higher_level" in input_dict.keys() else None,
            level=input_dict["level"],
            material=input_dict["material"] if "material" in input_dict.keys() else None,
            range=input_dict["range"],
            ritual=input_dict["ritual"],
            school=input_dict["school"],
            subclasses=input_dict["subclasses"],
        )

    def get_details(self, content_api: Content):
        if self.index:
            return Spell.parse_detail(content_api.get_detail(self.url))

    def __str__(self):
        return f"{self.name}"


if __name__ == "__main__":
    pass
