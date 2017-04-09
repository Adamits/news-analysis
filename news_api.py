# -*- coding: utf-8 -*-

import json
import requests
import os
import util
from json_writer import *

class NewsApi(object):
  def __init__(self, sources=[]):
    self.news_api_key = os.environ['NEWS_API_KEY']
    self.sources = sources

  def find_single_source(self, source):
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
  def find_by_mention(self, entity=()):
    article_sources = [self.find_single_source(source) for source in self.sources]
    matches =[]

    for articles in article_sources:
      for article in articles:
        if article.mentions(entity):
          matches.append(article)

    return matches


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

news_api = NewsApi(["cnn", "the-new-york-times", "the-wall-street-journal", "breitbart-news"])
articles = news_api.find_by_mention(("Trump", "NNP"))
json_writer = JsonWriter()
for article in articles:
  article_json = article.format_json()
  json_writer.write("./data/%s" % article_json.pop("source") + ".json", article_json)