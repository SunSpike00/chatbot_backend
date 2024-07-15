from data.rank_data import Rank

class RankController:
    def __init__(self):
        self.rank = Rank()

    def getRankList(self):
        return self.rank.getRankList()

    def getUserTopPresent(self, username):
        return self.rank.topPresent(username)