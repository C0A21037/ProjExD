import pygame as pg
import sys
import time, random

def main():
    color_red = pg.Color(255, 0, 0)
    color_white = pg.Color(255, 255, 255)
    color_green = pg.Color(0, 255, 0)
    screen = pg.display.set_mode((600, 400))
    screen.fill(color_white)
    pg.display.set_caption("蛇")
    arr = [([0] * 41) for i in range(61)]  
    x = 10  # 蛇の初期x座標
    y = 10  # 蛇の初期y座標
    foodx = random.randint(1, 60)  # 食べ物のx座標
    foody = random.randint(1, 40)  # 食べ物のy座標
    arr[foodx][foody] = -1
    snake_lon = 3  # 蛇の長さ
    way = 1  # 蛇の運動方向
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> efc9f0313274c01e2930c0ead7c177eb070853b7
    fonto = pg.font.Font(None,80)
    fonto2 = pg.font.Font(None,30)
    appnum = 3 #りんごゲットのノルマ(坂本)
    app = fonto2.render((f"APPLE:{appnum}"),True,(0,0,0)) #残りのりんごの獲得ノルマ表示(坂本)
    clear = fonto.render("Game Clear",True,(0,0,255))#ゲームクリアの表示(坂本)
    gover = fonto.render("Game Over",True,(255,0,0))#ゲームオーバーの表示(坂本)
    game = True #ゲームが続いているかのフラグ(坂本)
<<<<<<< HEAD
=======
    while True:
        if game:#ゲームオーバーでない限り(坂本)
            screen.fill(color_white)
            screen.blit(app,(50,50))#スクリーンに表示(坂本)
            time.sleep(0.1)
            for event in pg.event.get(): 
                if event.type == pg.QUIT:
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if (event.key == pg.K_RIGHT) and (way != 2):  # 右
                        way = 1
                    if (event.key == pg.K_LEFT) and (way != 1):  # 左
                        way = 2
                    if (event.key == pg.K_UP) and (way != 4):  # 上
                        way = 3
                    if (event.key == pg.K_DOWN) and (way != 3):  # 下に移動
                        way = 4
            if way == 1:
                x += 1
            if way == 2:
                x -= 1
            if way == 3:
                y -= 1
            if way == 4:
                y += 1
            if (x > 60) or (y > 40) or (x < 1) or (y < 1):  # 死亡(壁にぶつかったら)
                screen.bulit(gover,(160,150))#ゲームオーバーの表示
                pg.display.update()
                game = False #ゲームオーバーのフラグ
            arr[x][y] = snake_lon
            for a, b in enumerate(arr, 1):
                for c, d in enumerate(b, 1):
                    # 食べ物は-1，空地は0，蛇の位置は正数
                    if (d > 0):
                        # print(a,c) #蛇の座標を表示
                        arr[a - 1][c - 1] = arr[a - 1][c - 1] - 1
                        pg.draw.rect(screen, color_green, ((a - 1) * 10, (c - 1) * 10, 10, 10))
                    if (d < 0):
                        pg.draw.rect(screen, color_red, ((a - 1) * 10, (c - 1) * 10, 10, 10))
            if (x == foodx) and (y == foody):   #蛇が食べ物を食べったら
                snake_lon += 1    #長さ+1
                appnum -= 1 #ノルマのりんご数を1減らす(坂本)
                app = fonto2.render((f"APPLE:{appnum}"),True,(0,0,0)) #残りのりんごの獲得ノルマ表示(坂本)
                while (arr[foodx][foody] != 0):    #新しい食べ物を表示
                    foodx = random.randint(1, 60)
                    foody = random.randint(1, 40)
                arr[foodx][foody] = -1
                pg.display.update()
                if appnum < 1:                   #りんごのノルマを達成していたら(坂本)
                    screen.blit(clear,(150,160)) #クリア表示(坂本)
                    pg.display.update()
                    game = False #ゲームオーバーのフラグ(坂本)

            time.sleep(0.1)
            for event in pg.event.get():  # 监听器
                if event.type == pg.QUIT:
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if (event.key == pg.K_RIGHT) and (way != 2):  # 右
                        way = 1
                    if (event.key == pg.K_LEFT) and (way != 1):  # 左
                        way = 2
                    if (event.key == pg.K_UP) and (way != 4):  # 上
                        way = 3
                    if (event.key == pg.K_DOWN) and (way != 3):  # 下に移動
                        way = 4
            if way == 1:
                x += 1
            if way == 2:
                x -= 1
            if way == 3:
                y -= 1
            if way == 4:
                y += 1
            if (x > 60) or (y > 40) or (x < 1) or (y < 1) or (arr[x][y] > 0):  # 死亡(壁、自分の体をぶつかったら)
                sys.exit()
            arr[x][y] = snake_lon
            for a, b in enumerate(arr, 1):
                for c, d in enumerate(b, 1):
                    # 食べ物は-1，空地は0，蛇の位置は正数
                    if (d > 0):
                        # print(a,c) #蛇の座標を表示
                        arr[a - 1][c - 1] = arr[a - 1][c - 1] - 1
                        pg.draw.rect(screen, color_green, ((a - 1) * 10, (c - 1) * 10, 10, 10))
                    if (d < 0):
                        pg.draw.rect(screen, color_red, ((a - 1) * 10, (c - 1) * 10, 10, 10))
            if (x == foodx) and (y == foody):   #蛇が食べ物を食べったら
                snake_lon += 1    #長さ+1
                while (arr[foodx][foody] != 0):    #新しい食べ物を表示
                    foodx = random.randint(1, 60)
                    foody = random.randint(1, 40)
                arr[foodx][foody] = -1
            pg.display.update()
=======
    life = 3 # ライフの数
    pg.mixer.music.load("優雅なお猫様.mp3")  # BGMのロード
    pg.mixer.music.play(100)  # BGMを100回再生
    get = pg.mixer.Sound("レトロアクション.mp3")  # 餌ゲット時のSEのロード
    end = pg.mixer.Sound("しょげる.mp3")  # 終了時のSEのロード

>>>>>>> efc9f0313274c01e2930c0ead7c177eb070853b7
    while True:
        screen.fill(color_white)
        time.sleep(0.1)

        for i in range(life):
            H_sfc = pg.image.load("Hart.png")
            H_sfc = pg.transform.rotozoom(H_sfc, 0, 0.15)
            H_rct = H_sfc.get_rect()
            H_rct.center = i*50+30, 30
            # scrn_sfcにtori_rctに従って，tori_sfcを貼り付ける
            screen.blit(H_sfc, H_rct)

        for event in pg.event.get():  # 监听器
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if (event.key == pg.K_RIGHT) and (way != 2):  # 右
                    way = 1
                if (event.key == pg.K_LEFT) and (way != 1):  # 左
                    way = 2
                if (event.key == pg.K_UP) and (way != 4):  # 上
                    way = 3
                if (event.key == pg.K_DOWN) and (way != 3):  # 下に移動
                    way = 4
        if way == 1:
            x += 1
        if way == 2:
            x -= 1
        if way == 3:
            y -= 1
        if way == 4:
            y += 1
        if (x > 60) or (y > 40) or (x < 1) or (y < 1) or (arr[x][y] > 0):  # 死亡(壁、自分の体をぶつかったら)
            end.play()  # 終了時のSE
            time.sleep(1)  # 1秒停止
            sys.exit()
        arr[x][y] = snake_lon
        for a, b in enumerate(arr, 1):
            for c, d in enumerate(b, 1):
                # 食べ物は-1，空地は0，蛇の位置は正数
                if (d > 0):
                    # print(a,c) #蛇の座標を表示
                    arr[a - 1][c - 1] = arr[a - 1][c - 1] - 1
                    pg.draw.rect(screen, color_green, ((a - 1) * 10, (c - 1) * 10, 10, 10))
                if (d < 0):
                    pg.draw.rect(screen, color_red, ((a - 1) * 10, (c - 1) * 10, 10, 10))
        if (x == foodx) and (y == foody):   #蛇が食べ物を食べったら
            get.play()  # 餌ゲット時のSE
            snake_lon += 1    #長さ+1
            while (arr[foodx][foody] != 0):    #新しい食べ物を表示
                foodx = random.randint(1, 60)
                foody = random.randint(1, 40)
            arr[foodx][foody] = -1
            life -= 1
        if life == 0:
            end.play()  # 終了時のSE
            time.sleep(1)  # 1秒停止
            sys.exit()  # 終了
        pg.display.update()
>>>>>>> 6274ec18f7c4163a5904d5738df7ad2b92f299d4



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()        
