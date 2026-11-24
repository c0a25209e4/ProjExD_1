import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") # (1)
    bg_img2 = pg.image.load("fig/pg_bg.jpg") # (2)
    bg_img2 = pg.transform.flip(bg_img2, True, False) # (8)
    kk_img = pg.image.load("fig/3.png") # (3)
    kk_img = pg.transform.flip(kk_img, True, False) 
    kk_rect = kk_img.get_rect() # (10-1)
    kk_rect.center = [300, 200] # (10-2)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        # movement: right, down -> + left, up -> -
        movement = (-1, 0) # (e1-1)
        key_ls = pg.key.get_pressed() # (10-3)
        if key_ls[pg.K_UP]: # (10-4)
            movement = (0, -1)
        if key_ls[pg.K_DOWN]:
            movement = (0, 1)
        # if key_ls[pg.K_LEFT]:
        #     movement = (-1, 0))          
        if key_ls[pg.K_RIGHT]:
            movement = (1, 0)

        kk_rect.move_ip(movement) # (e2)

        x = tmr%3200 # (9)
        screen.blit(bg_img, [-x, 0]) # (5)
        screen.blit(bg_img2, [-x+1600, 0]) # (8)
        screen.blit(bg_img, [-x+3200, 0]) # (9)
        screen.blit(kk_img, kk_rect) # (10-5)
        pg.display.update()
        tmr += 1        
        clock.tick(200) # (6)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()