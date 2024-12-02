def clean_text(txt):
        """returns a cleaned  up version of the text"""
        for symbol in """.,?"'!;:""":
            txt = txt.replace(symbol, '')
        txt = txt.lower()
        txt = txt.split(" ")
        return txt

class TextModel:
    """a data type that represents a text model"""
    def __init__(self, model_name):
        """a constructor for the text model"""
        self.model_name = model_name
        self.words = {}
        self.word_lengths = {}
    
    def __repr__(self):
        """the string representation for the model"""
        string = 'text model name: ' + self.model_name
        string += '\nnumber of words: ' + str(len(self.words))
        string += '\nnumber of word lengths: ' + str(len(self.word_lengths))
        return string

    def add_string(self, s):
        """Analyzes the string txt and adds its pieces to all of the dictionaries in this text model."""

        word_list = clean_text(s)

        for w in word_list:
            if w in self.words:
                self.words[w] += 1
            else:
                self.words[w] = 1

            if len(w) in self.word_lengths:
                self.word_lengths[len(w)] += 1
            else:
                self.word_lengths[len(w)] = 1

    def add_file(self, filename):
        """Adds all text in a file to the model. Does not return any values"""
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        text = f.read()
        text = clean_text(text)
        self.add_string(text)
        f.close()

    def save_model(self):
        """Saves the text model's dictionaries as strings in text files"""
        words_dictname = self.model_name + '_' + 'words.txt'
        f = open(words_dictname, 'w')      # Open file for writing.
        f.write(str(self.words))              # Writes the dictionary to the file.
        f.close()     

        word_lengths_dictname = self.model_name + '_' + 'word_lengths.txt'
        f = open(word_lengths_dictname, 'w')      # Open file for writing.
        f.write(str(self.word_lengths))              # Writes the dictionary to the file.
        f.close()
    
    def read_model(self):
        """reads the text model's text files and converts them into dictionaries"""
        words_dictname = self.model_name + '_' + 'words.txt'
        f = open(words_dictname, 'r')    # Open for reading.
        d_str = f.read()           # Read in a string that represents a dict.
        f.close()

        self.words = dict(eval(d_str))

        word_lengths_dictname = self.model_name + '_' + 'word_lengths.txt'
        f = open(word_lengths_dictname, 'r')    # Open for reading.
        d_str = f.read()           # Read in a string that represents a dict.
        f.close()

        self.word_lengths = dict(eval(d_str))