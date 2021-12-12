# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 21:02:39 2021

@author: keisu
"""

import pygame
import sys
import VariableExplanation

class GameRoot(object):#テトリスの根幹
    #定数
    #windowサイズ
    WINDOW_SIZE = (800,600)
    #ゲームの状態
    is_game_launched = False
    is_game_closed = False
    #背景のパス
    ouspenski_cathedral_path = r'Images\OuspenskiCathedral\OuspenskiCathedral(400x300)PxcelArt.png'
    def start_game(self,):
        GameRoot.is_game_launched = True
        pygame.init()
        #
        DrawGame()
        GameRoutine()
    def close_game(self,):
        #ここでデータ保存?
        pygame.quit()#初期化を解除
        GameRoot.is_game_closed = False
        sys.exit()#終了
    
class DrawGame(GameRoot):#描画クラス
    def __init__(self,):
        #背景を読み込み
        #オムスク大聖堂
        self.ouspenski_cathedral = pygame.image.load(GameRoot.ouspenski_cathedral_path)
        #背景を400x300から800x600にする
        self.ouspenski_cathedral = pygame.transform.scale(self.ouspenski_cathedral,(800,600))
        #####
        #ウィンドウを作成
        self.create_window()
        #スタート画面を描画
        self.draw_start_screen()
    def create_window(self,):#windowを作成する。
        self.window = pygame.display.set_mode(GameRoot.WINDOW_SIZE)#作成
        pygame.display.set_caption('Tetris')#windowのタイトル
    def draw_start_screen(self,):
        #オムスクの大聖堂を背景にする
        self.window.blit(self.ouspenski_cathedral,(0,0))
        
class GameRoutine(GameRoot):
    def __init__(self,):
        while True:
            pygame.display.update()#画面をアップデート
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_root.close_game()

class TetriminoOperation(GameRoot):#テトリミノの操作
    def __init__(self,):
        pass
    def check_if_tetrimino_crash(self,):#テトリミノが上下左右でぶつかるか調べる。
        pass
    def up_operation(self,):#テトリミノを上へ移動させる
        pass
    def down_operation(self,):#テトリミノを下へ移動させる
        pass
    def right_operation(self,):#テトリミノを右へ移動させる
        pass
    def left_operation(self,):#テトリミノを左へ移動させる
        pass
    def delete_tetrimino(self,):#テトリミノを削除する
        pass
    def put_tetrimino(self,):#新しいテトリミノを置く
        pass
    def fix_tetrimino(self,):#テトリミノを固定する
        pass

if __name__ == '__main__':
    game_root = GameRoot()
    game_root.start_game()