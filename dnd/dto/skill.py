#!
# -*- coding: utf-8 -*-
"""
Created on 2021-03-13
@author: Edmund Bennett
@email: edmund.bennett@ghd.com
"""

from dnd.api.content import Content


class Skill:
    def __init__(
        self,
        index,
        name,
        url,
        description=None,
        ability_score=None,
    ):
        self.index = index
        self.name = name
        self.url = url
        self.description = description
        self.unparsed_ability_score = ability_score
        self.ability_score = None

    @staticmethod
    def parse_summary(input_dict):
        return Skill(
            index=input_dict["index"],
            name=input_dict["name"],
            url=input_dict["url"],
        )

    @staticmethod
    def parse_detail(input_dict):
        return Skill(
            index=input_dict["index"],
            name=input_dict["name"],
            url=input_dict["url"],
            description=input_dict["desc"],
            ability_score=input_dict["ability_score"],
        )

    def get_details(self, content_api: Content):
        if self.index:
            return Skill.parse_detail(content_api.get_detail(self.url))

    def get_ability_score(self, content_api: Content):
        from dnd.dto.ability_score import AbilityScore
        if self.unparsed_ability_score is not None:
            self.ability_score = AbilityScore.parse_summary(self.unparsed_ability_score).get_details(content_api)


    def __str__(self):
        return f"{self.name}"


if __name__ == "__main__":
    pass
