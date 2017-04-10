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


# print get_dependency_structure("My name is Adam and I was once a boy, but am now a man.")
