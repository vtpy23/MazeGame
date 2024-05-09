import numpy as np
import mazeGeneration as mg
import json as js
import time


matrix = mg.mazeGeneration().createMaze()
startpoint = (1, 1)  # Can change the start and end points as needed
endpoint = (len(matrix) - 3, len(matrix) - 3)  # Can change


class saveLoad:
    count = None
    maxFile = 20
    def __init__(self):
        self.dataGame = None
        self.name = None
        return
    def takeNumericalOrder(self):
        try:
            with open("gameSaving.json", encoding="utf-8") as fr:
                self.dataGame = js.load(fr)
        except:
            self.dataGame = [{'count' : 1}]
        order = self.dataGame[0]
        saveLoad.count = order['count']
    def saveGame(self, board_matrix, start_point, end_point):
        self.takeNumericalOrder()
        self.local_time = time.localtime()
        self.matrix = board_matrix  # Corrected variable name
        self.start_point = start_point
        self.end_point = end_point
        time_saving = {'Date': str(self.local_time.tm_mday) + '/' + str(self.local_time.tm_mon) + '/' + str(self.local_time.tm_year), 
                       'Time' : str(self.local_time.tm_hour) + ':' + str(self.local_time.tm_min) + ':' + str(self.local_time.tm_sec)}

        newGame = {"gameNumber": saveLoad.count, 'board': self.matrix, 'player_pos': self.start_point, 'ambitation_pos': self.end_point, 'time': time_saving}
        try:
            del self.dataGame[self.count]
        except:
            print("There is no file to pop")
        self.dataGame.insert(saveLoad.count, newGame)
        if(saveLoad.count < saveLoad.maxFile): saveLoad.count += 1
        else: saveLoad.count = 1
        self.dataGame[0]['count'] = saveLoad.count
        with open("gameSaving.json", "w") as fw:
            js.dump(self.dataGame, fw, indent=4)
        
    
    def loadGame(self, num):
        with open("gameSaving.json", encoding="utf-8") as fr:
            self.dataGame = js.load(fr)
        gameLoader = self.dataGame[num]
        matrix = gameLoader['board']
        gameInfo = []
        gameInfo.extend([gameLoader['player_pos'], gameLoader['ambitation_pos']])
        return matrix, gameInfo
    
    def takeNameFile(self):
        self.takeNumericalOrder()
        dataFile =[]
        if len(self.dataGame) == 1: 
            return []
        for i in range(len(self.dataGame)):
            try:
                dataFile.append(self.dataGame[i]['time']['Time'])
            except:
                print()
        return dataFile
