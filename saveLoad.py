import json as js
import time
import authentication 
from authentication import USERNAME
class saveLoad:
    count = None
    maxFile = 200
    def __init__(self):
        self.dataGame = None
        return
    
    def takeNumericalOrder(self):
        try:
            with open("gameSaving.json", encoding="utf-8") as fr:
                self.dataGame = js.load(fr)
        except:
            self.dataGame = [{'count' : 1}]
        order = self.dataGame[0]
        saveLoad.count = order['count']
    def saveGame(self, mode_play, board_matrix, start_point, end_point, player_step, timer_count):
        self.takeNumericalOrder()
        self.local_time = time.localtime()
        self.mode_play = mode_play
        self.matrix = board_matrix  # Corrected variable name
        self.start_point = start_point
        self.end_point = end_point
        time_saving = {'Date': str(self.local_time.tm_mday) + '/' + str(self.local_time.tm_mon) + '/' + str(self.local_time.tm_year), 
                       'Time' : str(self.local_time.tm_hour) + ':' + str(self.local_time.tm_min) + ':' + str(self.local_time.tm_sec)}

        newGame = {"gameNumber": saveLoad.count, 'board': self.matrix, 'player_pos': self.start_point, 'ambitation_pos': self.end_point, 'player_step': player_step, 'time': time_saving, 'username': authentication.USERNAME, 'counting_sec': timer_count, 'ran_cus': self.mode_play}
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
        with open("gameSaveUser.json", encoding="utf-8") as fr:
            dataGame = js.load(fr)
            matrix = dataGame[num]["board"]
            size = len(dataGame[num]["board"])
            player_pos = dataGame[num]["player_pos"]
            player_aimbitation = dataGame[num]["ambitation_pos"]
            ran_cus = dataGame[num]["ran_cus"]
            time_start = dataGame[num]["counting_sec"]
        return ran_cus, matrix, size, tuple(player_pos), tuple(player_aimbitation), time_start
    
    def savebyusername(self):
        with open('gameSaving.json', 'r') as file:
            data = js.load(file)
            filtered_data = [entry for entry in data if entry.get('username') == USERNAME]
            with open('gameSaveUser.json', 'w') as file:
                js.dump(filtered_data[-10:], file, indent=4)
            return filtered_data[-10:]

    def takeNameFile(self):
        dataGame = self.savebyusername()
        dataFile = []
        for i in range(len(dataGame)):
            sizemap = str(len(dataGame[i]['board']))
            ran_cus = "Random" if dataGame[i]['player_pos'] == [0, 0] else "Custom"
            name = sizemap + "   " + ran_cus + "   " + dataGame[i]['time']['Time'] + "   " + dataGame[i]['time']['Date']
            dataFile.append(name)
        return dataFile

class LeaderBoard:
    def __init__(self) -> None:
        self.count_win = 0
        self.timer = 0
        self.step = 0
        self.size = None
        self.name = USERNAME
    
    def saveWin(self, step, timer, mazeSize):
        with open("leaderBoard.json", 'r') as file:
            data = js.load(file)

        game = {
            'username' : USERNAME,
            'hard_mode': mazeSize, 
            'timer': timer, 
            'step': step
            }

        data.append(game)

        with open("leaderBoard.json", 'w') as file:
            js.dump(data, file, indent=4)

    def ldbbysizemap(self, sizemap):
        with open('leaderBoard.json', 'r') as file:
            data_by_user = js.load(file)
            data_by_size = [entry for entry in data_by_user if entry.get('hard_mode') == sizemap]
            return data_by_size
        
    def data_processing(self,sizemap):
        data = self.ldbbysizemap(sizemap)
        result = {}
        for item in data:
            username = item['username']
            if username in result:
                result[username]['number'] += 1
                result[username]['total_time'] += item['timer']
                result[username]['total_step'] += item['step']
            else:
                result[username] = {
                    'number': 1,
                    'total_time': item['timer'],
                    'total_step': item['step']
                }

        return [{'username': username, **info} for username, info in result.items()]