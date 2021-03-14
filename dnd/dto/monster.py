#!
# -*- coding: utf-8 -*-
"""
Created on 2021-03-13
@author: Edmund Bennett
@email: edmund.bennett@ghd.com
"""

from dnd.api.content import Content
from dnd.dto.action import Action


class Monster:
    @staticmethod
    def parse_summary(input_dict):
        return Monster(
            index=input_dict["index"],
            name=input_dict["name"],
            url=input_dict["url"],
        )

    def __init__(
        self,
        index,
        name,
        url,
        size=None,
        type=None,
        subtype=None,
        alignment=None,
        armor_class=None,
        challenge_rating=None,
        charisma=None,
        constitution=None,
        dexterity=None,
        intelligence=None,
        wisdom=None,
        strength=None,
        speed=None,
        actions=None,
        special_abilities=None,
        legendary_actions=None,
        senses=None,
        proficiencies=None,
        condition_immunities=None,
        damage_immunities=None,
        damage_resistances=None,
        damage_vulnerabilities=None,
        hit_dice=None,
        hit_points=None,
        languages=None,
        xp=None,
    ):
        self.index = index
        self.name = name
        self.url = url
        self.size = size
        self.type = type
        self.subtype = subtype
        self.alignment = alignment
        self.armor_class = armor_class
        self.challenge_rating = challenge_rating
        self.charisma = charisma
        self.constitution = constitution
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.strength = strength
        self.speed = speed
        self.actions = actions
        self.special_abilities = special_abilities
        self.legendary_actions = legendary_actions
        self.senses = senses
        self.proficiencies = proficiencies
        self.condition_immunities = condition_immunities
        self.damage_immunities = damage_immunities
        self.damage_resistances = damage_resistances
        self.damage_vulnerabilities = damage_vulnerabilities
        self.hit_dice = hit_dice
        self.hit_points = hit_points
        self.languages = languages
        self.xp = xp

    @staticmethod
    def parse_detail(input_dict):
        return Monster(
            index=input_dict["index"],
            name=input_dict["name"],
            url=input_dict["url"],
            size=input_dict["size"],
            type=input_dict["type"],
            subtype=input_dict["subtype"],
            alignment=input_dict["alignment"],
            armor_class=input_dict["armor_class"],
            challenge_rating=input_dict["challenge_rating"],
            charisma=input_dict["charisma"],
            constitution=input_dict["constitution"],
            dexterity=input_dict["dexterity"],
            intelligence=input_dict["intelligence"],
            wisdom=input_dict["wisdom"],
            strength=input_dict["strength"],
            speed=input_dict["speed"],
            actions=[Action.parse(e) for e in input_dict["actions"]] if "actions" in input_dict.keys() else None,
            special_abilities=input_dict["special_abilities"] if "special_abilities" in input_dict.keys() else None,
            legendary_actions=input_dict["legendary_actions"] if "legendary_actions" in input_dict.keys() else None,
            senses=input_dict["senses"],
            proficiencies=input_dict["proficiencies"],
            condition_immunities=input_dict["condition_immunities"],
            damage_immunities=input_dict["damage_immunities"],
            damage_resistances=input_dict["damage_resistances"],
            damage_vulnerabilities=input_dict["damage_vulnerabilities"],
            hit_dice=input_dict["hit_dice"],
            hit_points=input_dict["hit_points"],
            languages=input_dict["languages"],
            xp=input_dict["xp"],
        )

    def get_details(self, content_api: Content):
        if self.index:
            return Monster.parse_detail(content_api.get_detail(self.url))


    def __str__(self):
        return f"{self.name}"


if __name__ == "__main__":
    pass
