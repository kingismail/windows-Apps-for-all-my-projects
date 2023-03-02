
# tic tac toe game by Ismail
# The code king
# copyright reserved 2023
# more updates coming soon
#coded with passion


# tic tac toe remaster
from typing import Union

import pygame
from pygame.surface import Surface, SurfaceType
from pygame import mixer

pygame.init()
pygame.mixer.pre_init(4410, -16, 2, 512)

WIDTH = 600
HEIGHT = 650

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("tic tac toe")

mixer.music.load("sounds/music.mp3")
mixer.music.play(-1)

# image variables

player_o_blue = pygame.image.load("images/o_blue.png")
player_o_red = pygame.image.load("images/o_red.png")
player_x_red = pygame.image.load("images/x_red.png")
player_x_blue = pygame.image.load("images/x_blue.png")

# get images and rescale

player_o_blue = pygame.transform.scale(player_o_blue, (190, 190))
player_o_red = pygame.transform.scale(player_o_red, (190, 190))
player_x_red = pygame.transform.scale(player_x_red, (190, 190))
player_x_blue = pygame.transform.scale(player_x_blue, (190, 190))

white_background = pygame.transform.scale(pygame.image.load("images/white_back.png").convert_alpha(), (600, 650))
rect = white_background.get_rect(center=(WIDTH//2, HEIGHT//2))
alpha = 0
banner = pygame.image.load("images/menu_banner.png")
banner = pygame.transform.scale(banner, (400, 100))
anim_1 = pygame.image.load("images/anim_1.png")
anim_2 = pygame.image.load("images/anim_2.png")

anim_1 = pygame.transform.scale(anim_1, (200, 200))
anim_2 = pygame.transform.scale(anim_2, (200, 200))


sound_on = pygame.transform.scale(pygame.image.load("images/sound4.jpg"), (50, 50))
sound_off = pygame.transform.scale(pygame.image.load("images/no_sound.png"), (50, 50))

sound_images = []

click_sound_effect = mixer.Sound("sounds/click2.mp3")

# position dictionary

images = [player_o_blue, player_o_red, player_x_blue, player_x_red]
player_turn = images[0]
player_chosen_x = False
player_chosen_o = False
player_font_size = 60
button_color = "black"
started = False
player_1_chose_o = False
player_1_chose_x = False
game_font = pygame.font.Font("freesansbold.ttf", 30)
player_to_play = 1
plays = []
passed_background = False
menu_chose1 = 280
menu_height = 90
clicks = 0
button_play_color = "black"
button_play_text = "white"

button_exit_color = "dark grey"
button_exit_text = "black"

sound_turned_on = True
sound_turned_off = False

restarted = 0
restarted_bool = False


board_skeleton = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]


def create_grid():

    count = 0

    x_pos = [0, 0, 200, 400]
    y_pos = [200, 400, 0, 0]
    width = [600, 600, 5, 5]
    height = [5, 5, 600, 600]

    for line in range(4):

        pygame.draw.rect(screen, (0, 0, 0), (x_pos[count], y_pos[count], width[count], height[count]))
        count += 1


def change_player():

    global player_turn

    if player_1_chose_o:
        if player_turn == images[2]:
            player_turn = images[1]

        elif player_turn == images[1]:
            player_turn = images[2]

    if player_1_chose_x:
        if player_turn == images[0]:  # [player_o_blue, player_o_red, player_x_blue, player_x_red]
            player_turn = images[3]

        elif player_turn == images[3]:
            player_turn = images[0]


def place_plays():

    for placed_play in plays:
        screen.blit(placed_play[2], (placed_play[0], placed_play[1]))


def chose_player():

    global player_chosen_x, player_chosen_o, player_font_size, button_color, started, player_turn, player_1_chose_x
    global player_1_chose_o, game_font, restarted, restarted_bool

    player_font = pygame.font.Font("freesansbold.ttf", player_font_size)

    pygame.draw.rect(screen, (0, 0, 0), (WIDTH // 2 - 260, HEIGHT // 2 - 110, 520, 220))
    pygame.draw.rect(screen, (255, 255, 255), (WIDTH // 2 - 250, HEIGHT // 2 - 100, 500, 200))
    pygame.draw.rect(screen, (0, 0, 0), (300, 225, 10, 200))

    player1 = game_font.render("player 1", False, "red")
    player2 = game_font.render("player 2", False, "blue")

    screen.blit(player1, (120, 230))
    screen.blit(player2, (370, 230))

    pygame.draw.rect(screen, "red", (98, 300, 70, 80), border_radius=10)
    pygame.draw.rect(screen, "red", (190, 300, 70, 80), border_radius=10)

    x = player_font.render("X", False, "black")
    o = player_font.render("O", False, "black")

    if not player_chosen_x or player_chosen_o:
        screen.blit(x, (112, 300))
        screen.blit(o, (202, 300))

    if pygame.mouse.get_pressed()[0]:
        mouse_pos = pygame.mouse.get_pos()

        if 98 < mouse_pos[0] < 168:
            if 300 < mouse_pos[1] < 380:
                player_chosen_x = True

        if 190 < mouse_pos[0] < 260:
            if 300 < mouse_pos[1] < 380:
                player_chosen_o = True

        if player_chosen_x or player_chosen_o:
            if 270 < mouse_pos[0] < 350:
                if 330 < mouse_pos[1] < 370:
                    button_color = "yellow"
                    started = True
                    restarted = 0
                    restarted_bool = False

    if player_chosen_x:
        pygame.draw.rect(screen, "white", (90, 300, 200, 90))
        pygame.draw.rect(screen, "red", (130, 290, 90, 120), border_radius=10)
        pygame.draw.rect(screen, "blue", (380, 290, 90, 120), border_radius=10)
        player_font_size = 80
        screen.blit(x, (150, 300))
        screen.blit(o, (395, 300))
        player_turn = images[3]
        player_1_chose_x = True

        pygame.draw.rect(screen, button_color, (270, 330, 80, 40), border_radius=5)
        start = game_font.render("Start", False, "white")
        screen.blit(start, (277, 332))

    if player_chosen_o:
        pygame.draw.rect(screen, "white", (90, 300, 200, 90))
        pygame.draw.rect(screen, "red", (130, 290, 90, 120), border_radius=10)
        pygame.draw.rect(screen, "blue", (380, 290, 90, 120), border_radius=10)
        player_font_size = 80
        screen.blit(o, (145, 300))
        screen.blit(x, (400, 300))
        player_turn = images[1]  # [player_o_blue, player_o_red, player_x_blue, player_x_red]
        player_1_chose_o = True

        pygame.draw.rect(screen, "black", (270, 330, 80, 40), border_radius=5)
        start = game_font.render("Start", False, "white")
        screen.blit(start, (277, 332))


def show_texts():

    global game_font

    players_turn = game_font.render(f'player = player {player_to_play}       coded by Ismail', False, "black")
    screen.blit(players_turn, (10, 610))


def check_win():

    if board_skeleton[0][0] == 1 and board_skeleton[0][1] == 1 and board_skeleton[0][2] == 1:
        return [100, 50, 100, 550]

    elif board_skeleton[1][0] == 1 and board_skeleton[1][1] == 1 and board_skeleton[1][2] == 1:
        return [300, 50, 300, 550]

    elif board_skeleton[2][0] == 1 and board_skeleton[2][1] == 1 and board_skeleton[2][2] == 1:
        return [500, 50, 500, 550]

    elif board_skeleton[0][0] == 1 and board_skeleton[1][0] == 1 and board_skeleton[2][0] == 1:
        return [50, 100, 550, 100]

    elif board_skeleton[0][1] == 1 and board_skeleton[1][1] == 1 and board_skeleton[2][1] == 1:
        return [50, 300, 550, 300]

    elif board_skeleton[0][2] == 1 and board_skeleton[1][2] == 1 and board_skeleton[2][2] == 1:
        return [50, 500, 550, 500]

    elif board_skeleton[0][0] == 1 and board_skeleton[1][1] == 1 and board_skeleton[2][2] == 1:
        return [50, 50, 550, 550]

    elif board_skeleton[0][2] == 1 and board_skeleton[1][1] == 1 and board_skeleton[2][0] == 1:
        return [550, 50, 50, 550]

    elif board_skeleton[0][0] == 2 and board_skeleton[0][1] == 2 and board_skeleton[0][2] == 2:
        return [100, 50, 100, 550]

    elif board_skeleton[1][0] == 2 and board_skeleton[1][1] == 2 and board_skeleton[1][2] == 2:
        return [300, 50, 300, 550]

    elif board_skeleton[2][0] == 2 and board_skeleton[2][1] == 2 and board_skeleton[2][2] == 2:
        return [500, 50, 500, 550]

    elif board_skeleton[0][0] == 2 and board_skeleton[1][0] == 2 and board_skeleton[2][0] == 2:
        return [50, 100, 550, 100]

    elif board_skeleton[0][1] == 2 and board_skeleton[1][1] == 2 and board_skeleton[2][1] == 2:
        return [50, 300, 550, 300]

    elif board_skeleton[0][2] == 2 and board_skeleton[1][2] == 2 and board_skeleton[2][2] == 2:
        return [50, 500, 550, 500]

    elif board_skeleton[0][0] == 2 and board_skeleton[1][1] == 2 and board_skeleton[2][2] == 2:
        return [50, 50, 550, 550]

    elif board_skeleton[0][2] == 2 and board_skeleton[1][1] == 2 and board_skeleton[2][0] == 2:
        return [550, 50, 50, 550]


def exit_restart_buttons_logics():

    global running, restarted, restarted_bool

    if pygame.mouse.get_pressed()[0]:
        press_pos = pygame.mouse.get_pos()

        if 210 < press_pos[0] < 290:
            if 350 < press_pos[1] < 390:
                restarted += 1
                restart()

        if 300 < press_pos[0] < 340:
            if 350 < press_pos[1] < 390:
                running = False

    if restarted > 0:
        restart()
        restarted_bool = True


def winner_found():

    global alpha, running, started

    menu_font = pygame.font.Font("freesansbold.ttf", 20)
    started = False

    alpha = 200

    pygame.draw.rect(screen, (0, 0, 0), (WIDTH // 2 - 260, HEIGHT // 2 - 110, 520, 220))
    pygame.draw.rect(screen, (255, 255, 255), (WIDTH // 2 - 250, HEIGHT // 2 - 100, 500, 200))
    restart_game = menu_font.render("Restart", False, "white")
    quit_game = menu_font.render("Quit", False, "white")

    if player_to_play == 2:
        winner_font = game_font.render(f"player {player_to_play - 1} wins", False, "black")
        screen.blit(winner_font, (200, 300))
        pygame.draw.rect(screen, "black", (300, 350, 80, 40), border_radius=5)
        pygame.draw.rect(screen, "black", (210, 350, 80, 40), border_radius=5)
        screen.blit(quit_game, (318, 355))
        screen.blit(restart_game, (215, 355))

    elif player_to_play == 1:
        winner_font = game_font.render(f"player {player_to_play + 1} wins", False, "black")
        screen.blit(winner_font, (200, 300))
        pygame.draw.rect(screen, "black", (300, 350, 80, 40), border_radius=5)
        pygame.draw.rect(screen, "black", (210, 350, 80, 40), border_radius=5)
        screen.blit(quit_game, (318, 355))
        screen.blit(restart_game, (215, 355))

    exit_restart_buttons_logics()


def restart():

    global started, alpha, plays, board_skeleton, player_chosen_x, player_chosen_o

    # for all_plays in plays:
    # plays.remove(all_plays)

    plays = []
    board_skeleton = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

    started = False


def game_menu():

    global passed_background, menu_chose1, menu_height, clicks
    global button_play_text, button_exit_text, button_play_color, button_exit_color
    global passed_background, sound_turned_on, sound_turned_off

    if not passed_background:
        screen.blit(white_background, (0, 0))
        screen.blit(banner, (WIDTH//2 - banner.get_width()//2, 50))
        screen.blit(anim_1, (0, 200))
        screen.blit(anim_2, (410, 480))
        pygame.draw.rect(screen, "grey", (200, 250, 200, 300), border_radius=5)
        pygame.draw.rect(screen, "white", (210, 260, 180, 280), border_radius=5)
        pygame.draw.rect(screen, "grey", (200, 220, 230, 20), border_top_right_radius=5)
        pygame.draw.rect(screen, "grey", (415, 220, 20, menu_height))

        pygame.draw.rect(screen, button_play_color, (220, 270, 160, 60))
        pygame.draw.rect(screen, "dark grey", (220, 360, 160, 60))
        pygame.draw.rect(screen, button_exit_color, (220, 460, 160, 60))
        pygame.draw.rect(screen, "grey", (405, menu_chose1, 9, 40))

        pygame.draw.rect(screen, "black", (10, 530, 20, 100))
        pygame.draw.rect(screen, "black", (10, 620, 100, 20))

        pygame.draw.rect(screen, "black", (500, 0, 90, 20))
        pygame.draw.rect(screen, "black", (570, 10, 20, 90))

        play_start = game_font.render("Play", False, button_play_text)
        screen.blit(play_start, (270, 280))

        credits_shown = game_font.render("Credits", False, "silver")
        screen.blit(credits_shown, (250, 370))

        quit_play = game_font.render("Quit", False, button_exit_text)
        screen.blit(quit_play, (270, 470))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN]:
            if menu_chose1 == 280 and clicks == 0:
                menu_chose1 = 470
                button_play_color = "dark grey"
                button_play_text = "black"
                button_exit_color = "black"
                button_exit_text = "white"

            if menu_height == 90:
                menu_height = 270

        if keys[pygame.K_UP]:

            if menu_chose1 == 470:
                menu_chose1 = 280
                button_exit_color = "dark grey"
                button_exit_text = "black"
                button_play_color = "black"
                button_play_text = "white"

            if menu_height == 270:
                menu_height = 90

        if keys[pygame.K_KP_ENTER] and button_play_color == "black":
            passed_background = True

        if sound_turned_on:
            screen.blit(sound_on, (490, 400))
            sound_font = game_font.render("sound: on", False, "black")
            screen.blit(sound_font, (450, 360))
            # sound_turned_off = False

        elif sound_turned_off:
            screen.blit(sound_off, (490, 400))
            sound_font = game_font.render("sound: off", False, "black")
            screen.blit(sound_font, (450, 360))
            # sound_turned_on = False

        if pygame.mouse.get_pressed()[0]:
            mouse_pos2 = pygame.mouse.get_pos()
            if 490 < mouse_pos2[0] < 540:
                if 400 < mouse_pos2[1] < 450:
                    if sound_turned_on:
                        if pygame.mouse.get_pressed()[0]:
                            sound_turned_off = True
                            sound_turned_on = False

                    elif sound_turned_off:
                        if pygame.mouse.get_pressed()[0]:
                            sound_turned_on = True
                            sound_turned_off = False


def mouse_hover_effect():

    global button_play_color, button_play_text, passed_background
    global button_exit_text, button_exit_color, started, running

    mouse_pos3 = pygame.mouse.get_pos()
    if 220 < mouse_pos3[0] < 380:
        if 270 < mouse_pos3[1] < 330:
            button_play_color = "black"
            button_play_text = "white"
            if pygame.mouse.get_pressed()[0]:
                passed_background = True

        else:
            button_play_color = "dark grey"
            button_play_text = "black"

    if 220 < mouse_pos3[0] < 380:
        if 460 < mouse_pos3[1] < 520:
            button_exit_color = "black"
            button_exit_text = "white"
            if pygame.mouse.get_pressed()[0]:
                running = False

        else:
            button_exit_color = "dark grey"
            button_exit_text = "black"
        # if pygame.mouse.get_pressed()[0]:


def declair_draw():

    global alpha

    menu_font = pygame.font.Font("freesansbold.ttf", 20)

    alpha = 200
    white_background.set_alpha(alpha)
    screen.blit(white_background, (0, 0))

    pygame.draw.rect(screen, (0, 0, 0), (WIDTH // 2 - 260, HEIGHT // 2 - 110, 520, 220))
    pygame.draw.rect(screen, (255, 255, 255), (WIDTH // 2 - 250, HEIGHT // 2 - 100, 500, 200))

    restart_game = menu_font.render("Restart", False, "white")
    quit_game = menu_font.render("Quit", False, "white")
    pygame.draw.rect(screen, "black", (300, 350, 80, 40), border_radius=5)
    pygame.draw.rect(screen, "black", (210, 350, 80, 40), border_radius=5)
    screen.blit(quit_game, (318, 355))
    screen.blit(restart_game, (215, 355))
    draw_font = game_font.render(f"Draw", False, "black")
    screen.blit(draw_font, (250, 290))

    exit_restart_buttons_logics()


running = True

while running:

    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            click_sound_effect.play()
            # print(f"{pos[0]//200}, {pos[1]//200}")
            new_pos = ()
            test1 = new_pos + (((pos[0] // 200) * 200) + 5,) + (((pos[1] // 200) * 200) + 5,) + (images[0],)
            test2 = new_pos + (((pos[0] // 200) * 200) + 5,) + (((pos[1] // 200) * 200) + 5,) + (images[1],)
            test3 = new_pos + (((pos[0] // 200) * 200) + 5,) + (((pos[1] // 200) * 200) + 5,) + (images[2],)
            test4 = new_pos + (((pos[0] // 200) * 200) + 5,) + (((pos[1] // 200) * 200) + 5,) + (images[3],)
            if started:
                if test1 not in plays and test2 not in plays and test3 not in plays and test4 not in plays:
                    play = new_pos + (((pos[0] // 200) * 200) + 5, ) + (((pos[1] // 200) * 200) + 5, ) + (player_turn, )

                    change_player()
                    plays.append(play)
                    # print(play)

                    if player_to_play == 1:
                        player_to_play = 2

                    elif player_to_play == 2:
                        player_to_play = 1

                    for position in plays:
                        if player_to_play == 1:
                            board_skeleton[pos[0] // 200][pos[1] // 200] = 2

                        elif player_to_play == 2:
                            board_skeleton[pos[0] // 200][pos[1] // 200] = 1
                    """""
                    if 490 < pos[0] < 540:
                        if 400 < pos[1] < 450:
                            if sound_turned_on:
                                # if event.type == pygame.MOUSEBUTTONUP:
                                sound_turned_off = True
                                sound_turned_on = False

                            elif sound_turned_off:
                                # if event.type == pygame.MOUSEBUTTONUP:
                                sound_turned_on = True
                                #sound_turned_off = False
"""""
                #print(plays)
                # for played in plays:
                # print(played[0])

    create_grid()
    place_plays()

    if not started:
        chose_player()

    show_texts()
    # print(check_win())

    if check_win():
        if not restarted_bool:
            pygame.draw.line(screen, "yellow", (check_win()[0], check_win()[1]), (check_win()[2], check_win()[3]), width=20)
            white_background.set_alpha(alpha)
            screen.blit(white_background, (0, 0))
            winner_found()

    if not passed_background:
        # print(board_skeleton)
        game_menu()
        mouse_hover_effect()

    if sound_turned_off:
        mixer.music.play(-1)

    # print(number_of_plays)
    if len(plays) > 8 and not check_win():
        declair_draw()

    pygame.display.flip()

pygame.display.quit()
