from datetime import datetime
from time import sleep 
def timer(function):
  def new_function(*args, **kwargs):
    start_time = datetime.now()
    res = function(*args, **kwargs)
    elapsed = (datetime.now() - start_time).total_seconds()
    print(f'Function took {elapsed} seconds to complete.')
    return res
  return new_function
    
@timer
def index_words(text):
    result = []
    if text:
        sleep(0.1)
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            sleep(0.1)
            result.append(index + 1)
    return result

@timer
def index_words_iter(text):
    if text:
        sleep(0.1)
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            sleep(0.1)
            yield index + 1

if __name__ == '__main__':
    words = ["breathe", "sunflower", "rainbow", "three to the right", "four to the left"]
    capitals = (word.upper() for word in words)
    print(next(capitals))
    print(next(capitals))