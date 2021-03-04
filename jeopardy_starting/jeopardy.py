import pandas as pd
pd.set_option('display.max_colwidth',7)

data = pd.read_csv('jeopardy.csv')
data.columns = [column.strip() for column in data.columns]


def filter_data(data, words):
  # Lowercases all words in the list of words as well as the questions. Returns true is all of the words in the list appear in the question.
  filter = lambda x: all(word.lower() in x.lower() for word in words)
  # Applies the labmda function to the Question column and returns the rows where the function returned True
  return data.loc[data["Question"].apply(filter)]

word_list = ["Life"]
#print(len(filter_data(data, word_list)))
data['Value'] = data.Value.apply(lambda x: float(x.replace('$', '').replace(',', '')) if x != 'None' else 0)
print(data.head)

print(filter_data(data, word_list).Value.mean())

def count_unique(data):
  return data.Answer.value_counts()

print(count_unique(filter_data(data, word_list)))