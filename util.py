# functions for interfacing with NLP stuff

import spacy
nlp = spacy.load('en')

def analyze_sentiment(input_str="", entity=""):
  # components from Stanford's Dependency parser to create dep. tree.
  return True

def get_pos_tags(sentence):
  return [(word.text, word.tag_)for word in nlp(sentence)]

def get_dependency_structure(sentence):
  # Get tuples from iterable
  deps = dep_parse.raw_parse(sentence)
  # Return it as a list of triples
  return list(deps.next().triples())


# print get_pos_tags(u"Donald Trump is such a dog")
# print get_dependency_structure("Hey, I am a dog named Donald Trump")
# print [dep_tuple for dep_triple in get_dependency_structure("Hey I am a dog named Donald Trump") for dep_tuple in dep_triple if isinstance(dep_tuple, tuple)]
