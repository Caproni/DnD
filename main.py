#!
# -*- coding: utf-8 -*-
"""
Created on 2021-03-14
@author: Edmund Bennett
@email: edmund.bennett@ghd.com
"""

from dnd.api.content import Content
from dnd.dto.skill import Skill
from dnd.dto.ability_score import AbilityScore
from dnd.dto.language import Language
from dnd.dto.alignment import Alignment
from dnd.dto.equipment_category import EquipmentCategory
from dnd.dto.monster import Monster
from dnd.dto.spell import Spell


def get_spells(content_api):
    spells = [Spell.parse_summary(e).get_details(content_api) for e in content_api.get_summary("spells")]
    return spells


def get_skills(content_api):
    skills = [Skill.parse_summary(e).get_details(content_api) for e in content_api.get_summary("skills")]
    for skill in skills:
        skill.get_ability_score(content_api)
    return skills

def get_ability_scores(content_api):
    ability_scores = [AbilityScore.parse_summary(e).get_details(content_api) for e in content_api.get_summary("ability-scores")]
    for ability_score in ability_scores:
        ability_score.get_skills(content_api)
    return ability_scores

def get_languages(content_api):
    languages = [Language.parse_summary(e).get_details(content_api) for e in content_api.get_summary("languages")]
    return languages

def get_alignments(content_api):
    alignments = [Alignment.parse_summary(e).get_details(content_api) for e in content_api.get_summary("alignments")]
    return alignments

def get_equipment_categories(content_api):
    equipment_categories = [EquipmentCategory.parse_summary(e).get_details(content_api) for e in content_api.get_summary("equipment-categories")]
    for equipment_category in equipment_categories:
        equipment_category.get_equipment(content_api)
    return equipment_categories

def get_monsters(content_api):
    monsters = [Monster.parse_summary(e).get_details(content_api) for e in content_api.get_summary("monsters")]
    # for monster in monsters:
    #     monster.get_equipment(content_api)
    return monsters


if __name__ == '__main__':
    content_api = Content(load_caches=True)
    print(f"Spells: {get_spells(content_api)}")
    print(f"Skills: {get_skills(content_api)}")
    print(f"Ability Scores: {get_ability_scores(content_api)}")
    print(f"Languages: {get_languages(content_api)}")
    print(f"Monsters: {get_monsters(content_api)}")
    content_api.dump_caches()