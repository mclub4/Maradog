import pickle

class DB_Read:
    def __init__(self, filename, scoredb):
        self.filename = filename
        self.scoredb = scoredb
        try:
            self.file = open(filename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = [0]
            return
        try:
            self.scoredb = pickle.load(self.file)
        except:
            pass
        else:
            pass
        self.file.close()

    def checkScoreDB(self):
        if len(self.scoredb) == 0:
            self.scoredb = [0]
        return self.scoredb

    def writeScoreDB(self, scoredb):
        self.scoredb = scoredb
        self.file = open(self.filename, 'wb')
        pickle.dump(self.scoredb, self.file)
        self.file.close()