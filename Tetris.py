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
    is_game_start_screen = False
    #画像のパス
    #オムスク大聖堂
    OUSPENSKI_CATHEDRAL_PATH = r'Images\OuspenskiCathedral\OuspenskiCathedral(400x300)PxcelArt.png'
    #Tetrisロゴ(タイトル画面の)
    TETRIS_TITLE_LOGO_PATH = r'Images\Title\Tetris.png'
    def start_game(self,):
        GameRoot.is_game_launched = True
        pygame.init()
        #
        #ウィンドウを作成
        draw_game.create_window()
        #スタート画面を描画
        draw_game.draw_start_screen()
        #ゲームルーティーンを開始
        game_routine.start_game_routine()
    def close_game(self,):
        #ここでデータ保存?
        pygame.quit()#初期化を解除
        #ゲームの状態
        GameRoot.is_game_launched = False
        GameRoot.is_game_start_screen = False
        sys.exit()#終了
    
class DrawGame(GameRoot):#描画クラス
    def __init__(self,):
        #画像を読み込み
        #オムスク大聖堂(背景)
        self.ouspenski_cathedral = pygame.image.load(GameRoot.OUSPENSKI_CATHEDRAL_PATH)
        #Tetrisロゴ
        self.tetris_title_logo = pygame.image.load(GameRoot.TETRIS_TITLE_LOGO_PATH)
        #
        #読み込んだ画像を適切な大きさにする
        #背景(オムスク大聖堂)を400x300から800x600にする(WINDOW_SIZEにする)
        self.ouspenski_cathedral = pygame.transform.scale(self.ouspenski_cathedral,GameRoot.WINDOW_SIZE)
        self.tetris_title_logo = pygame.transform.scale(self.tetris_title_logo,(650,150))
        #####
    def create_window(self,):#windowを作成する。
        self.window = pygame.display.set_mode(GameRoot.WINDOW_SIZE)#作成
        pygame.display.set_caption('Tetris')#windowのタイトル
    def draw_start_screen(self,):#タイトル画面の作成
        GameRoot.is_game_start_screen = True
        #オムスクの大聖堂を背景にする
        self.window.blit(self.ouspenski_cathedral,(0,0))
        #タイトル追加(TETRIS)
        self.window.blit(self.tetris_title_logo,(75,0))
class GameRoutine(GameRoot):
    def __init__(self,):
        pass
    def start_game_routine(self,):
        while True:
            pygame.display.update()#画面をアップデート
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_root.close_game()
    def game_mode_selection(self,):
        pass
                    
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
    #インスタンスをあらかじめ作成
    draw_game = DrawGame()#画像を読み込む
    game_routine = GameRoutine()
    #
    game_root.start_game()