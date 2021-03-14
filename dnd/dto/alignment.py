#!
# -*- coding: utf-8 -*-
"""
Created on 2021-03-13
@author: Edmund Bennett
@email: edmund.bennett@ghd.com
"""

from dnd.api.content import Content


class Alignment:
    def __init__(
        self,
        index,
        name,
        url,
        abbreviation=None,
        description=None,
        typical_speakers=None,
    ):
        self.index = index
        self.name = name
        self.url = url
        self.abbreviation = abbreviation
        self.description = description

    @staticmethod
    def parse_summary(input_dict):
        return Alignment(
            index=input_dict["index"],
            name=input_dict["name"],
            url=input_dict["url"],
        )

    @staticmethod
    def parse_detail(input_dict):
        return Alignment(
            index=input_dict["index"],
            name=input_dict["name"],
            url=input_dict["url"],
            abbreviation=input_dict["abbreviation"],
            description=input_dict["desc"],
        )

    def get_details(self, content_api: Content):
        if self.index:
            return Alignment.parse_detail(content_api.get_detail(self.url))


    def __str__(self):
        return f"{self.name}"


if __name__ == "__main__":
    pass
