import glob
import json
from news_api import Article


class NewsArchive(object):

  def get_titles_by_source(self, source=None):
    source_and_titles = {}

    for key, articles in self.find_articles_by_source(source).items():
      source_and_titles[key] = [article.title for article in articles]

    return source_and_titles

  def pretty_print_titles_by_source(self, source=None):
    for source, articles in self.get_titles_by_source(source).items():
      print "%s:\n" % source.upper()
      for title in articles:
        print "%s \n" % title
      print "\n"

  def find_articles_by_source(self, source=None):
    if source:
      with open('./news-data/%s.json' % source, "r") as jsonFile:
        source = jsonFile.split("/")[-1].replace(".json", "")
        return [Article(article, source) for article in json.load(jsonFile)]
    else:
      all_articles = {}

      for filename in glob.glob('./news-data/*.json'):
        with open(filename, "r") as jsonFile:
          source = filename.split("/")[-1].replace(".json", "")
          all_articles[source] = [Article(article, source) for article in json.load(jsonFile)]

      return all_articles

  def find_articles_by_mention(self, entity=()):
    match_articles = []

    for filename in glob.glob('./news-data/*.json'):
      with open(filename, "r") as jsonFile:
        source = filename.split("/")[-1].replace(".json", "")

        for article_json in json.load(jsonFile)
          article = Article(article_json, source)
          if article.mentions(entity)
            match_articles.append(article)

    return match_articles
