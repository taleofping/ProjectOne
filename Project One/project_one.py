import pygame as pg
import random

pg.init()
displaysurf = pg.display.set_mode((800,600))
pg.display.set_caption("Project's One")


sound_battle = pg.mixer.Sound('battle.ogx')
sound_title = pg.mixer.Sound('title.ogx')
sound_die = pg.mixer.Sound('You_Died.ogg')
sound_shot = pg.mixer.Sound('shot.ogg')
sound_hit = pg.mixer.Sound('hit.ogg')

title = pg.image.load('map0.png')

map_all = [pg.image.load('map1.png'),pg.image.load('map2.png')
            ,pg.image.load('map3.png'),pg.image.load('map4.png')
            ,pg.image.load('map5.png'),pg.image.load('map6.png')
            ,pg.image.load('map7.png'),pg.image.load('map8.png')
            ,pg.image.load('map9.png'),pg.image.load('map10.png')]

char = [pg.image.load('char_f.png'),pg.image.load('char_b.png'),pg.image.load('char_l.png'),pg.image.load('char_r.png')]
move_f = [pg.image.load('char_fw1.png'),pg.image.load('char_fw2.png'),pg.image.load('char_fw3.png')]
move_b = [pg.image.load('char_bw1.png'),pg.image.load('char_bw2.png'),pg.image.load('char_bw3.png')]
move_l = [pg.image.load('char_lw1.png'),pg.image.load('char_lw2.png'),pg.image.load('char_lw3.png')]
move_r = [pg.image.load('char_rw1.png'),pg.image.load('char_rw2.png'),pg.image.load('char_rw3.png')]


class player(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walk_count = 0
        self.x_change = 0
        self.y_change = 0
        self.a = 3
        self.move_f1 = False
        self.move_b1 = False
        self.move_l1 = False
        self.move_r1 = False
        self.hitbox = (self.x+4,self.y+5,32,32)
        self.hp = 5
    def anime(self,displaysurf):
        if self.walk_count + 1 >= 18:
            self.walk_count = 0
        if self.move_l1:
            displaysurf.blit(move_l[self.walk_count//6],(self.x,self.y))
            self.walk_count += 1
            self.a = 2
        elif self. move_r1:
            displaysurf.blit(move_r[self.walk_count//6],(self.x,self.y))
            self.walk_count += 1
            self.a = 3
        elif self.move_b1:
            displaysurf.blit(move_b[self.walk_count//6],(self.x,self.y))
            self.walk_count += 1
            self.a = 1
        elif self.move_f1:
            displaysurf.blit(move_f[self.walk_count//6],(self.x,self.y))
            self.walk_count += 1
            self.a = 0
        else :
            displaysurf.blit(char[self.a],(self.x,self.y))
        self.hitbox = (self.x+4,self.y+5,32,32)
        pg.draw.rect(displaysurf,(255,0,0),(self.hitbox[0],self.hitbox[1]-20,30,10))
        pg.draw.rect(displaysurf,(0,255,0),(self.hitbox[0],self.hitbox[1]-20,30-(6*(5-self.hp)),10))
        

bat1 = [pg.image.load('bat1_1.png'),pg.image.load('bat1_2.png'),pg.image.load('bat1_3.png')]
bat2 = [pg.image.load('bat2_1.png'),pg.image.load('bat2_2.png'),pg.image.load('bat2_3.png')]
bee = [pg.image.load('bee_1.png'),pg.image.load('bee_2.png'),pg.image.load('bee_3.png')]
bird1 = [pg.image.load('bird1_1.png'),pg.image.load('bird1_2.png'),pg.image.load('bird1_3.png')]
bird2 = [pg.image.load('bird2_1.png'),pg.image.load('bird2_2.png'),pg.image.load('bird2_3.png')]
bird3 = [pg.image.load('bird3_1.png'),pg.image.load('bird3_2.png'),pg.image.load('bird3_3.png')]
eye = [pg.image.load('eye_1.png'),pg.image.load('eye_2.png'),pg.image.load('eye_3.png')]
merman = [pg.image.load('merman_1.png'),pg.image.load('merman_2.png'),pg.image.load('merman_3.png')]
spider1 = [pg.image.load('spider1_1.png'),pg.image.load('spider1_2.png'),pg.image.load('spider1_3.png')]
spider2 = [pg.image.load('spider2_1.png'),pg.image.load('spider2_2.png'),pg.image.load('spider2_3.png')]
spider3 = [pg.image.load('spider3_1.png'),pg.image.load('spider3_2.png'),pg.image.load('spider3_3.png')]
monster = [bat1,bat2,bee,bird1,bird2,bird3,eye,merman,spider1,spider2,spider3]


class enemy(object):
    def __init__(self, x, y, w, h , end ,monster_type):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.end = end
        self.path = [self.x, self.end]
        self.walk_count = 0
        self.vel = -(random.randint(2,5))
        self.hp = 3
        self.visible = True
        self.hitbox = (self.x+4,self.y+5,32,32)
        self.monster_type = monster_type
    def anime(self,displaysurf):
        self.move()
        if self.visible:
            if self.walk_count + 1 >= 36:
                self.walk_count = 0  
            if self.vel<0:
                displaysurf.blit(monster[self.monster_type][self.walk_count//12],(self.x,self.y))
                self.walk_count += 1
            pg.draw.rect(displaysurf,(255,0,0),(self.hitbox[0],self.hitbox[1]-20,15,10))
            pg.draw.rect(displaysurf,(0,255,0),(self.hitbox[0],self.hitbox[1]-20,15-(5*(3-self.hp)),10))
            self.hitbox = (self.x+4,self.y+5,32,32)
        else:
            self.hitbox = (0,0,32,32)
    def move(self):
        if self.vel < 0:
            self.x += self.vel
            self.walk_count += 1
    def hit(self):
        global score
        if self.hp > 1:
            self.hp -= 1
        else:
            self.visible = False
            score += 1
        

class gun(object):
    def __init__(self,x,y,rad,color,facing):
        self.x = x
        self.y = y
        self.rad = rad
        self.color = color
        self.facing = facing
        self.vel = 8 * facing  
    def anime(self,displaysurf):
        pg.draw.circle(displaysurf, self.color, (self.x, self.y),self.rad)
        
        
def redraw():
    text = font.render('SCORE : '+str(score),1,(0,255,0))
    text2 = fontBig.render('HIGH SCORE : '+str(highscore),1,(0,255,0))
    loadStage(stage)
    displaysurf.blit(text,(5,5))
    displaysurf.blit(text2,(5,35))
    one.anime(displaysurf)
    mon.anime(displaysurf)
    mon2.anime(displaysurf)
    mon3.anime(displaysurf)
    mon4.anime(displaysurf)
    for bullet in bullets:
        bullet.anime(displaysurf)
    pg.display.update()
    
    
def loadStage(stage):
    if stage == 0:
        return displaysurf.blit(title,(0,0))
    if stage == 1:
        return displaysurf.blit(map_all[0],(0,0))
    if stage == 2:
        return displaysurf.blit(map_all[1],(0,0))
    if stage == 3:
        return displaysurf.blit(map_all[2],(0,0))
    if stage == 4:
        return displaysurf.blit(map_all[3],(0,0))
    if stage == 5:
        return displaysurf.blit(map_all[4],(0,0))
    if stage == 6:
        return displaysurf.blit(map_all[5],(0,0))
    if stage == 7:
        return displaysurf.blit(map_all[6],(0,0))
    if stage == 8:
        return displaysurf.blit(map_all[7],(0,0))
    if stage == 9:
        return displaysurf.blit(map_all[8],(0,0))
    if stage == 10:
        return displaysurf.blit(map_all[9],(0,0))
    

def restart():
    global score,stage,mon,mon2,mon3,mon4
    one.hp = 5
    one.x = 0
    one.y = 436
    one.x_change = 0
    one.y_change = 0
    score = 0
    
    stage = random.randint(1,10)
    mon = enemy(random.randint(800,1000),random.randint(375,398),40,40,0,random.randint(0,10))
    mon2 = enemy(random.randint(800,1000),random.randint(403,424),40,40,0,random.randint(0,10))
    mon3 = enemy(random.randint(800,1000),random.randint(429,460),40,40,0,random.randint(0,10))
    mon4 = enemy(random.randint(800,1000),random.randint(465,486),40,40,0,random.randint(0,10))
    sound_battle.play(-1)
    sound_die.stop()
    

stage = 0
run = True
game_end = False
one = player(0,436)
mon = enemy(-10,-10,40,40,0,random.randint(0,10))
mon2 = enemy(-10,-10,40,40,0,random.randint(0,10))
mon3 = enemy(-10,-10,40,40,0,random.randint(0,10))
mon4 = enemy(-10,-10,40,40,0,random.randint(0,10))
bullets=[]
score = 0
highscore = 0
font = pg.font.SysFont('comicsans',40)
fontBig = pg.font.SysFont('comicsans',30)
facing = 1

while run:
    pg.time.delay(10)
    if one.hitbox[1] < mon.hitbox[1] + mon.hitbox[3] and one.hitbox[1] + one.hitbox[3] >mon.hitbox[1]:
            if one.hitbox[0] + one.hitbox[2]> mon.hitbox[0] and one.hitbox[0] < mon.hitbox[0] +mon.hitbox[2]:
                if one.hp > 0:
                    one.hp -= 1
                    sound_hit.play()
                    mon.visible = False
                    mon.hitbox = (0,0,32,32)
                    if one.hp == 0:
                        sound_battle.stop()
                        sound_die.play()
                        pg.time.delay(2000)
                        restart()
    if one.hitbox[1] < mon2.hitbox[1] + mon2.hitbox[3] and one.hitbox[1] + one.hitbox[3] >mon2.hitbox[1]:
            if one.hitbox[0] + one.hitbox[2]> mon2.hitbox[0] and one.hitbox[0] < mon2.hitbox[0] +mon2.hitbox[2]:
                if one.hp > 0:
                    one.hp -= 1
                    sound_hit.play()
                    mon2.visible = False
                    mon2.hitbox = (0,0,32,32)
                    if one.hp == 0:
                        sound_battle.stop()
                        sound_die.play()
                        pg.time.delay(2000)
                        restart()
    if one.hitbox[1] < mon3.hitbox[1] + mon3.hitbox[3] and one.hitbox[1] + one.hitbox[3] >mon3.hitbox[1]:
            if one.hitbox[0] + one.hitbox[2]> mon3.hitbox[0] and one.hitbox[0] < mon3.hitbox[0] +mon3.hitbox[2]:
                if one.hp > 0:
                    one.hp -= 1
                    sound_hit.play()
                    mon3.visible = False
                    mon3.hitbox = (0,0,32,32)
                    if one.hp == 0:
                        sound_battle.stop()
                        sound_die.play()
                        pg.time.delay(2000)
                        restart()
    if one.hitbox[1] < mon4.hitbox[1] + mon4.hitbox[3] and one.hitbox[1] + one.hitbox[3] >mon4.hitbox[1]:
            if one.hitbox[0] + one.hitbox[2]> mon4.hitbox[0] and one.hitbox[0] < mon4.hitbox[0] +mon4.hitbox[2]:
                if one.hp > 0:
                    one.hp -= 1
                    sound_hit.play()
                    mon4.visible = False
                    mon4.hitbox = (0,0,32,32)
                    if one.hp == 0:
                        sound_battle.stop()
                        sound_die.play()
                        pg.time.delay(2000)
                        restart()
    
                    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    for bullet in bullets:
        if bullet.y - bullet.rad < mon4.hitbox[1] + mon4.hitbox[3] and bullet.y + bullet.rad > mon4.hitbox[1]:
            if bullet.x + bullet.rad > mon4.hitbox[0] and bullet.x - bullet.rad < mon4.hitbox[0] +mon4.hitbox[2]:
                mon4.hit()
                bullets.pop(bullets.index(bullet))
        elif bullet.y - bullet.rad < mon3.hitbox[1] + mon3.hitbox[3] and bullet.y + bullet.rad > mon3.hitbox[1]:
            if bullet.x + bullet.rad > mon3.hitbox[0] and bullet.x - bullet.rad < mon3.hitbox[0] +mon3.hitbox[2]:
                mon3.hit()
                bullets.pop(bullets.index(bullet))
        elif bullet.y - bullet.rad < mon2.hitbox[1] + mon2.hitbox[3] and bullet.y + bullet.rad > mon2.hitbox[1]:
            if bullet.x + bullet.rad > mon2.hitbox[0] and bullet.x - bullet.rad < mon2.hitbox[0] +mon2.hitbox[2]:
                mon2.hit()
                bullets.pop(bullets.index(bullet))
        elif bullet.y - bullet.rad < mon.hitbox[1] + mon.hitbox[3] and bullet.y + bullet.rad > mon.hitbox[1]:
            if bullet.x + bullet.rad > mon.hitbox[0] and bullet.x - bullet.rad < mon.hitbox[0] +mon.hitbox[2]:
                mon.hit()
                bullets.pop(bullets.index(bullet))

        if bullet.x < 800 and bullet.x > 0 :
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    
    keys=pg.key.get_pressed()
    if keys[pg.K_SPACE]:
        if len(bullets) < 1:
            sound_shot.play()
            bullets.append(gun(round(one.x + 20),(one.y + 20), 6, (0,0,0), facing))           
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_RIGHT:
            facing = 1
            one.x_change = 3
            one.move_r1 = True
            one.move_f1 = False
            one.move_b1 = False
            one.move_l1 = False
        if event.key == pg.K_LEFT:
            facing = -1
            one.x_change = -3
            one.move_l1 = True
            one.move_f1 = False
            one.move_b1 = False
            one.move_r1 = False
        if event.key == pg.K_UP:
            one.y_change = -2
            one.move_b1 = True
            one.move_f1 = False
            one.move_l1 = False
            one.move_r1 = False
        if event.key == pg.K_DOWN:
            one.y_change = 2
            one.move_f1 = True
            one.move_b1 = False
            one.move_l1 = False
            one.move_r1 = False
    if event.type == pg.KEYUP:
        if event.key == pg.K_RIGHT or event.key == pg.K_LEFT:
            one.x_change = 0
            one.move_f1 = False
            one.move_b1 = False
            one.move_l1 = False
            one.move_r1 = False
        if event.key == pg.K_UP or event.key == pg.K_DOWN:
            one.y_change = 0
            one.move_f1 = False
            one.move_b1 = False
            one.move_l1 = False
            one.move_r1 = False

    one.x += one.x_change
    one.y += one.y_change
    
    
    redraw()
    if score >= highscore:
        highscore = score
    if one.y < 375:
        one.y = 375
    if one.y > 486:
        one.y = 486
    if one.x < 0:
        one.x = 1
    if one.x > 800-30:
        sound_title.stop()
        if stage == 0:
            sound_battle.play(-1)
        stage = random.randint(1,10)
        monster_type = random.randint(0,10)
        loadStage(stage)
        mon = enemy(random.randint(800,1000),random.randint(375,398),40,40,0,random.randint(0,10))
        mon2 = enemy(random.randint(800,1000),random.randint(403,424),40,40,0,random.randint(0,10))
        mon3 = enemy(random.randint(800,1000),random.randint(429,460),40,40,0,random.randint(0,10))
        mon4 = enemy(random.randint(800,1000),random.randint(465,486),40,40,0,random.randint(0,10))
        one.x,one.y = 0,one.y
    if stage == 0 :
        sound_title.play(-1)
   
        
        
pg.quit()