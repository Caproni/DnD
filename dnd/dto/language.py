#!
# -*- coding: utf-8 -*-
"""
Created on 2021-03-13
@author: Edmund Bennett
@email: edmund.bennett@ghd.com
"""

from dnd.api.content import Content


class Language:
    def __init__(
        self,
        index,
        name,
        url,
        type=None,
        script=None,
        typical_speakers=None,
    ):
        self.index = index
        self.name = name
        self.url = url
        self.type = type
        self.script = script
        self.typical_speakers = typical_speakers

    @staticmethod
    def parse_summary(input_dict):
        return Language(
            index=input_dict["index"],
            name=input_dict["name"],
            url=input_dict["url"],
        )

    @staticmethod
    def parse_detail(input_dict):
        return Language(
            index=input_dict["index"],
            name=input_dict["name"],
            url=input_dict["url"],
            type=input_dict["type"],
            script=input_dict["script"],
            typical_speakers=input_dict["typical_speakers"],
        )

    def get_details(self, content_api: Content):
        if self.index:
            return Language.parse_detail(content_api.get_detail(self.url))


    def __str__(self):
        return f"{self.name}"


if __name__ == "__main__":
    pass
