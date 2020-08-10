class Item:
    def __init__(self, name, stats, desc, item1 , item2,  pic):
        self.name = name
        self.desc = desc
        self.stats = stats
        self.item1 = item1
        self.item2 = item2
        self.pic = pic

        def getName(self):
            return self.name

        def getStats(self):
            return self.stats

        def getDesc(self):
            return self.desc

        def getItem1(self):
            return self.item1

        def getItem2(self):
            return self.item2

        def getPic(self):
            return self.pic


BF = Item("BF Sword", "+15 Attack Damage", " ",
          "N/A", "N/A",
          "test")

Tear = Item("Tear of the Goddess", "+15 Starting Mana", " ",
            "N/A", "N/A",
            "test")

Rod = Item("Needlessly large rod", "+ 15 Ability Power", " ",
           "N/A", "N/A",
           "test")

Belt = Item("Giants Belt", "+150 Health", " ",
            "N/A", "N/A",
            "test")

Shojin = Item("Spear of Shojin", "+15 Attack Damage, + 15 Starting Mana",
              "After casting Special Ability for the first time, basic attacks "
              "restore an additional 18% of maximum mana."
              , BF, Tear,
              "test")





