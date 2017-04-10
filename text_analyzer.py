class TextAnalyzer(object):

  def __init__(self, text):
    self.raw_text = text
    self.text = nlp(text)

  def sentiment(self):
    # Use model to find overall sentiment of a text.
    return True

  def entity_sentiment(self, entity=()):
    # To look at entity sentiment, we need the representation of the verb construction
    # that the entity is an argument of, as well as a model trained for
    # sentiment analysis of this type of argument, the intuition being that the model
    # learned the argument structure surrounding an entity that are associated with its sentiment.
    return True

  def get_pos_tags(self):
    return [(word.text, word.tag_) for word in self.text]
