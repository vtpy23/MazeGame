import numpy as np
import mazeGeneration as mg
import json as js
import time
import authentication 
from authentication import USERNAME
class saveLoad:
    count = None
    maxFile = 10
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
    def saveGame(self, board_matrix, start_point, end_point, player_step, timer_count):
        self.takeNumericalOrder()
        self.local_time = time.localtime()
        self.matrix = board_matrix  # Corrected variable name
        self.start_point = start_point
        self.end_point = end_point
        time_saving = {'Date': str(self.local_time.tm_mday) + '/' + str(self.local_time.tm_mon) + '/' + str(self.local_time.tm_year), 
                       'Time' : str(self.local_time.tm_hour) + ':' + str(self.local_time.tm_min) + ':' + str(self.local_time.tm_sec)}

        newGame = {"gameNumber": saveLoad.count, 'board': self.matrix, 'player_pos': self.start_point, 'ambitation_pos': self.end_point, 'player_step': player_step, 'time': time_saving, 'username': authentication.USERNAME, 'counting_sec': timer_count}
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
        gameInfo.extend([gameLoader['player_pos'], gameLoader['ambitation_pos'], gameLoader['player_step'], gameLoader['counting_sec']])
        return matrix, gameInfo
    
    def takeNameFile(self):
        self.takeNumericalOrder()
        dataFile =[]
        if len(self.dataGame) == 1: 
            return []
        for i in range(len(self.dataGame)):
            try:
                dataFile.append(self.dataGame[i]['username'])
            except:
                print()
        return dataFile

class LeaderBoard:
    def __init__(self) -> None:
        self.count_win = 0
        self.timer = 0
        self.step = 0
        self.name = authentication.USERNAME
    def sortLeaderBoard(self, data):
        #list player
        for i in range(len(data)):
            Flag = i
            top = data[i]
            for j in range(i+1, len(data)):
                if(data[j]['count_win'] > top['count_win']):
                    Flag = j
                    top = data[j]
                elif(data[j]['count_win'] == top['count_win']):
                    if(data[j]['average_timer'] < top['average_timer']):
                        Flag = j
                        top = data[j]
            data[i], data[Flag] = data[Flag], data[i]
        return data
    
    def saveWin(self, step, timer):
        Flag = False
        self.timer = timer
        self.step = step
        game = {'name': self.name, 'average_timer': self.timer, 'average_step': self.step, 'count_win': 1, 'timer': [self.timer], 'step': [self.step]}
        try:
            with open("leaderBoard.json", encoding="utf-8") as fr:
                self.leaderBoard = js.load(fr)
        except:
            self.leaderBoard = []
        for i in range(len(self.leaderBoard)):
            if(self.leaderBoard[i]['name'] == self.name):
                Flag = True
                self.leaderBoard[i]['timer'].append(self.timer)
                self.leaderBoard[i]['step'].append(self.step)
                self.leaderBoard[i]['average_timer'] = sum(self.leaderBoard[i]['timer'])/len(self.leaderBoard[i]['timer'])
                self.leaderBoard[i]['average_step'] = sum(self.leaderBoard[i]['step'])/len(self.leaderBoard[i]['step'])
                self.leaderBoard[i]['count_win'] += 1

        if(Flag == False):
            self.leaderBoard.append(game)
        
        self.leaderBoard = self.sortLeaderBoard(self.leaderBoard)
        with open("leaderBoard.json", "w") as fw:
            js.dump(self.leaderBoard, fw, indent=4)

    def get_data(self, file_path):
        with open(file_path, encoding="utf-8") as fi:
            return js.load(fi)
    
    def sort_average_time(self):
        data = self.get_data("leaderBoard.json")
        return sorted(data, key=lambda x: x['average_timer'])
        
    def sort_average_step(self):
        data = self.get_data("leaderBoard.json")
        return sorted(data, key=lambda x: x['average_step'])
        
    def get_top(self, top_list):
        data = self.get_data("leaderBoard.json")
        if len(data) < 5:
            leader_board_len = len(data)
        else: leader_board_len = 5 
        return top_list[:5]

def savebyusername():
    try:
        with open('gameSaving.json', 'r') as file:
            data = js.load(file)
        filtered_data = [entry for entry in data if entry.get('username') == USERNAME]

        with open('save_byUSERNAME.json', 'w') as file:
            js.dump(filtered_data, file, indent=4)
    except Exception as e:
        print(f'Something went wrong: {e}')

savebyusername()