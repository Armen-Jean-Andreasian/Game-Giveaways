import pickle

def test_results(path):
    with open(path, 'rb') as file:
        return pickle.load(file)


if __name__ == '__main__':
    print(test_results(path="../database/cache/cache.json"))
