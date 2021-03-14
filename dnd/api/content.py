#!
# -*- coding: utf-8 -*-
"""
Created on 2021-03-13
@author: Edmund Bennett
@email: edmund.bennett@ghd.com
"""

import requests
import json
from os.path import abspath, isfile
import dnd.utils.logger as log


class Content:

    _CACHE_DUMP_FORMAT = "utf-8"
    _STUB = "https://www.dnd5eapi.co"

    def __init__(self, load_caches=True):

        self.summary_cache = {}
        self.detail_cache = {}
        if load_caches:
            self.load_caches()

    def get_summary(self, type):
        log.logger.info(f"Getting summary specified by type: {type}")
        key = f"summary {type}"
        if key in self.summary_cache.keys():
            log.logger.debug(f"Data available in cache")
            return self.summary_cache[key]
        else:
            log.logger.debug(f"Data not available in cache")
            try:
                formed_uri = Content._STUB + f"/api/{type}"
                response = requests.get(formed_uri)
                data = json.loads(response.text)["results"]
                self.summary_cache[key] = data
                return data
            except Exception as e:
                log.logger.critical(f"API call failed with error: {e}")
                return None

    def get_detail(self, url):
        log.logger.info(f"Getting detail specified by url: {url}")
        key = f"detail {url}"
        if key in self.detail_cache.keys():
            log.logger.debug(f"Data available in cache")
            return self.detail_cache[key]
        else:
            log.logger.debug(f"Data not available in cache")
            try:
                formed_uri = Content._STUB + f"{url}"
                response = requests.get(formed_uri)
                data = json.loads(response.text)
                self.detail_cache[key] = data
                return data
            except Exception as e:
                log.logger.critical(f"API call failed with error: {e}")
                return None

    def get_detail_by_type_and_index(self, type, index):
        log.logger.info(f"Getting detail specified by type: {type} and index: {index}")
        url = f"/api/{type}/{index}"
        key = f"detail {url}"
        if key in self.detail_cache.keys():
            log.logger.debug(f"Data available in cache")
            return self.detail_cache[key]
        else:
            log.logger.debug(f"Data not available in cache")
            try:
                formed_uri = Content._STUB + f"{url}"
                response = requests.get(formed_uri)
                data = json.loads(response.text)
                self.detail_cache[key] = data
                return data
            except Exception as e:
                log.logger.critical(f"API call failed with error: {e}")
                return None

    def dump_caches(self):
        self.dump_summary_cache()
        self.dump_detail_cache()

    def dump_summary_cache(self):
        with open(abspath("cache/summary.cache"), "wb") as summary_cache_file:
            summary_cache_file.write(json.dumps(self.summary_cache).encode(Content._CACHE_DUMP_FORMAT))

    def dump_detail_cache(self):
        with open(abspath("cache/detail.cache"), "wb") as detail_cache_file:
            detail_cache_file.write(json.dumps(self.detail_cache).encode(Content._CACHE_DUMP_FORMAT))

    def load_caches(self):
        self.load_summary_cache()
        self.load_detail_cache()

    def load_summary_cache(self):
        cache_file = abspath("cache/summary.cache")
        log.logger.info(f"Loading summary cache file at: {cache_file}")
        if isfile(cache_file):
            with open(cache_file, "rb") as summary_cache_file:
                cache_contents = summary_cache_file.read().decode(Content._CACHE_DUMP_FORMAT)
                if cache_contents:
                    self.summary_cache = json.loads(cache_contents)

    def load_detail_cache(self):
        cache_file = abspath("cache/detail.cache")
        log.logger.info(f"Loading detail cache file at: {cache_file}")
        if isfile(cache_file):
            with open(cache_file, "rb") as detail_cache_file:
                cache_contents = detail_cache_file.read().decode(Content._CACHE_DUMP_FORMAT)
                if cache_contents:
                    self.detail_cache = json.loads(cache_contents)


if __name__ == "__main__":
    pass
