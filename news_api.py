# -*- coding: utf-8 -*-

import json
import requests
import os
import util
from json_writer import *


class NewsApi(object):
  def __init__(self):
    self.news_api_key = os.environ['NEWS_API_KEY']

  def find_articles_by_source(self, source):
    response = requests.get(
      "https://newsapi.org/v1/articles?source=%s&apiKey=%s" % (source, self.news_api_key))
    response_json = json.loads(response.text)
    articles = []
    status = response_json.get("status")

    if status == "error":
      return response_json.get("message")
    else:
      for article in response_json["articles"]:
        source = response_json["source"]
        articles.append(Article(article, source))

      return articles

  # Entity is a tuple of (text_string, pos_string) to search for
  def find_articles_by_mention(self, sources=[], entity=()):
    article_sources = [self.find_articles_by_source(source) for source in sources]
    matches = []

    for articles in article_sources:
      for article in articles:
        if article.mentions(entity):
          matches.append(article)

    return matches

  def get_sources(self, params=None):
    if params:
      response = requests.get(
        "https://newsapi.org/v1/sources?%s&apiKey=%s" % (params, self.news_api_key))
    else:
      response = requests.get(
        "https://newsapi.org/v1/sources?apiKey=%s")

    response_json = json.loads(response.text)
    status = response_json.get("status")
    if status == "ok":
      return [source["id"]for source in response_json["sources"]]
    else:
      return response_json.get("message")


class Article(object):
  def __init__(self, args={}, source=""):
    self.json = args
    self.source = source
    self.title = args.get("title")
    self.url = args.get("url")
    self.author = args.get("author")
    self.description = args.get("description")
    self.published_at = args.get("publishedAt")

  def mentions(self, entity=()):
    return entity in util.get_pos_tags(self.title)

  def format_json(self):
    format_dict = self.__dict__.copy()
    format_dict.pop("json")

    return format_dict

def add():
  news_api = NewsApi()
  for source in news_api.get_sources("language=en&country=us"):
    articles = news_api.find_articles_by_source(source)
    json_writer = JsonWriter()
    for article in articles:
      article_json = article.format_json()
      json_writer.write("./news-data/%s" % article_json.pop("source") + ".json", article_json)

add()