#!
# -*- coding: utf-8 -*-
"""
Created on 2021-03-13
@author: Edmund Bennett
@email: edmund.bennett@ghd.com
"""

from dnd.api.content import Content


class AbilityScore:
    def __init__(
        self,
        index,
        name,
        url,
        full_name=None,
        description=None,
        unparsed_skills=None,
    ):
        self.index = index
        self.name = name
        self.url = url
        self.full_name = full_name
        self.description = description
        self.unparsed_skills = unparsed_skills
        self.skills = []

    @staticmethod
    def parse_summary(input_dict):
        return AbilityScore(
            index=input_dict["index"],
            name=input_dict["name"],
            url=input_dict["url"],
        )

    @staticmethod
    def parse_detail(input_dict):
        return AbilityScore(
            index=input_dict["index"],
            name=input_dict["name"],
            url=input_dict["url"],
            full_name=input_dict["full_name"],
            description=input_dict["desc"],
            unparsed_skills=input_dict["skills"],
        )

    def get_details(self, content_api: Content):
        if self.index:
            return AbilityScore.parse_detail(content_api.get_detail(self.url))

    def get_skills(self, content_api: Content):
        from dnd.dto.skill import Skill
        if self.unparsed_skills is not None:
            for skill in self.unparsed_skills:
                self.skills.append(Skill.parse_summary(skill).get_details(content_api))


    def __str__(self):
        return f"{self.full_name}"


if __name__ == "__main__":
    pass
