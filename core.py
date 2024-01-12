class Core:
    def write_data(self, data: dict) -> None:
        with open("words.txt", "a") as file:
            en =  data['en']
            uz =  data['uz']

            file.write(f"{en}|{uz}\n")

    def get_all_words(self):
        with open("words.txt", "r") as file:
            words = list()
            data = file.readlines()
            for word in data:
                word = word[:-1].split("|")
                en, uz = word
                words.append({'en':en, 'uz':uz})
        return words
            # data = file.read().split('\n')[:-1]
            # data = list(map(lambda word: word.split('|'), data))
            # print(data)
    def get_word(self, word):
        data = self.get_all_words()
        for words in data:
            en = words.get('en')
            uz = words.get('uz')
            if word == en or word == uz:
                return en, uz
        return 0

core = Core()
core.get_word("da")