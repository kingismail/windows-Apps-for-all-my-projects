
# © Ismail; 2023 copyright all right reserved 

import pygame
import time
import math 

pygame.init()

WIDTH, HEIGHT = 363, 690

screen = pygame.display.set_mode((WIDTH, HEIGHT))
creds = pygame.transform.scale(pygame.image.load("images/creds2.jpg"), (363, 400))
creds3 = pygame.transform.scale(pygame.image.load("images/cred3.jpg"), (363, 690))
app_font = pygame.font.Font("fonts/Digital 3.ttf", 60)

button_number = 1

pressed = []

pressed_clean = []

clicked = 0
currently_clicked = 0

button_clicked = False
Button_released = True

results = ""
output = 0
syntax_error = False

exit_count = 0

current_seconds = []
wants_to_view_credits = False

exiting = False

class Display:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw_display(self):
        display_screen = pygame.draw.rect(screen, "silver", (self.x, self.y, WIDTH - 20, 200), border_radius=10)
        pygame.draw.rect(screen, ("black") ,(self.x + 5, self.y + 5, WIDTH - 30, 190), border_radius=10)

display = Display(10, 10)


class Buttons:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw_button_zone(self):
        button_zone = pygame.draw.rect(screen, "teal", (self.x, self.y, WIDTH - 20, HEIGHT - 230), border_radius=10)

buttons = Buttons(10, 220)


def create_all_buttons():

    global pressed, pressed_clean, Button_released, results, output
    global wants_to_view_credits, syntax_error


    button_lable_font = pygame.font.Font("fonts/freesansbold.ttf", 30)

    pre_rect = []

    button_number = 1
    button_count = 0

    x_positions = [17, 100, 183, 266, 17, 100, 183, 266, 17, 100, 183, 266, 17, 100, 183,266, 17, 100, 183, 266]
    y_positions = [225, 225, 225, 225, 330, 330, 330, 330, 415, 415, 415, 415, 500, 500, 500, 500, 585, 585, 585, 585]
    colors = ["grey", "grey", "grey", "grey", "grey", "grey", "grey", "black", "grey", "grey", "grey", "black", "grey", "grey", "grey", "black","black", "grey", "black", "white"]
    widths = [80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80,80, 80, 80, 80, 80, 80, 80]
    height = [80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80,80, 80, 80, 80 ]
    values = ["%", "creds", "C", "del", "7", "8", "9", "÷", "4", "5", "6", "x", "1", "2", "3", "-", ".", "0", "+", "=" ]
    value_color = ["black", "black", "black", "black", "black", "black", "black", "white", "black", "black", "black", "white", "black", "black", "black", "white", "white", "black", "white", "black"]
    count = 0
    hover_color = ["yellow", "yellow", "yellow", "yellow", "dark grey", "dark grey", "dark grey", "blue", "dark grey", "dark grey", "dark grey", "blue", "dark grey", "dark grey", "dark grey", "blue", "blue", "dark grey", "blue", "red"]

    button_list = []

    button_list_hover = 0

    forbiden_buttons = [2, 3, 4, 20]

    for i in range(20):
        
        button_list.append([x_positions[i], y_positions[i]])

    #print(button_list)

    for button in range(len(x_positions)):
        button_show = pygame.draw.rect(screen, colors[count], (x_positions[count], y_positions[count], widths[count], height[count]), border_radius=5)
        button_text = button_lable_font.render(values[count], False, value_color[count])
        screen.blit(button_text, ((x_positions[count] + 40) -  button_text.get_width() / 2, (y_positions[count] + 40) - button_text.get_height() / 2))
        pre_rect.append((x_positions[count],y_positions[count],values[count]),)
        count += 1

    # changing of the colors during hover and press

        pos = pygame.mouse.get_pos()
    
        for button_pressed in button_list:
            if pos[0] > button_show.x and pos[0] < button_show.x + 80:
                if pos[1] > button_show.y and pos[1] < button_show.y + 80:
                    if button_show.x == button_list[button_count][0] and button_show.y == button_list[button_count][1]:

                        pygame.draw.rect(screen, hover_color[button_number - 1],(button_show.x, button_show.y, 80, 80), border_radius=5)
                        button_text = button_lable_font.render(values[button_number - 1], False, value_color[button_number - 1])
                        screen.blit(button_text, ((button_show.x + 40) -  button_text.get_width() / 2, (button_show.y + 40)- button_text.get_height() / 2))

                        if pygame.mouse.get_pressed()[0]:
                            press_pos = pygame.mouse.get_pos()
                            
                            if press_pos[0] > button_show.x and press_pos[0] < button_show.x + 80:
                                if press_pos[1] > button_show.y and press_pos[1] < button_show.y + 80:
                                    if button_show.x == button_list[button_count][0] and button_show.y == button_list[button_count][1]:

                                        if Button_released and len(pressed) < 12 and button_number not in forbiden_buttons:
                                            pressed_clean.append(values[button_number - 1])
                                            Button_released = False


                                        if button_number == 20:
                                            if len(results) > 0:
                                                try:
                                                 output = eval(results)

                                                except:
                                                    syntax_error = True
                                                    
     
                                            else:
                                                output = 0

                                        if button_number == 3:
                                            if len(pressed) > 0:
                                                pressed.remove(pressed[0])
                                                output = 0

                                        if button_number == 2:
                                            wants_to_view_credits = True
                                            
                                        if button_number == 4 and Button_released and len(pressed) > 0:
                                            pressed.remove(pressed[len(pressed) - 1])
                                            Button_released = False
                                            
                    else:
                        button_number += 1

                    button_count += 1

        if button_number == 20:
            button_number = 0


def show_typings():

    global app_font, Button_released, button_clicked, results, pressed, button_number

    global pressed, pressed_clean

    if len(pressed_clean):
        pressed.append(pressed_clean[0])
        for i in pressed_clean:
            pressed_clean.remove(i)

    if len(pressed) > -1:
        pressed_final = "".join(pressed).replace("÷", "/").replace("√", "sqrt(")
        
        results = str(pressed_final).replace("x", "*").replace("÷", "/").replace("%", "/100")
        typed_text = app_font.render(pressed_final, False, "white")
        screen.blit(typed_text, (20, 60))


        if time.gmtime()[5] %2 == 0:
            
            type_cursor = app_font.render("|", False, "red")
            screen.blit(type_cursor, (typed_text.get_width() + 25, 60))

        
def show_output():

    global output

    output_results = app_font.render(str(output), False, "white")
    screen.blit(output_results, (WIDTH - 20 - output_results.get_width(), 150))

def end_screen():

    global current_seconds, running

    global exit_count, game_font

    pygame.draw.rect(screen, ("black") ,(display.x + 5, display.y + 5, WIDTH - 30, 190), border_radius=10)


    name_font = pygame.font.Font("fonts/Digital 3.ttf", 80)
    name = name_font.render("ISMAIL", False, "white")
    screen.blit(name, (WIDTH // 2 - name.get_width() // 2, 60))

    latest_seconds = time.gmtime()[5]

    if latest_seconds %2 == 0:
        exit_count += 2

    
    if len(current_seconds) < 2:
        current_seconds.append(time.gmtime()[5])


    if exit_count == 68:
        running = False


def credits_screen():

    global wants_to_view_credits

    pygame.draw.rect(screen, "white", (0, 0, WIDTH, HEIGHT))

    credits_font = pygame.font.Font("fonts/freesansbold.ttf", 15)

    header_text = app_font.render("Credits", False, "black")
    header_underline = app_font.render("-------", False, "black")
    screen.blit(header_text, (WIDTH// 2 - header_text.get_width() // 2, 20))
    screen.blit(header_underline, (WIDTH// 2 - header_text.get_width() // 2, 55))

    cred_text = credits_font.render("Coded by: ISMAIL", False, "black")
    screen.blit(cred_text, (WIDTH // 2 - cred_text.get_width() // 2, 130))

    cred_text2 = credits_font.render("©CG 2023 copyright all rights reserved", False, "black")
    screen.blit(cred_text2, (WIDTH // 2 - cred_text2.get_width() // 2, 600))

    screen.blit(creds, (0, 200))

    back_button = pygame.draw.rect(screen, "red", (WIDTH - 70, 30, 50, 50), border_radius=5)
    back_text = credits_font.render("back", False, "black")
    screen.blit(back_text, (back_button.x  + back_text.get_width() - 25,43))


    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()

        if back_button.collidepoint(pos):
            wants_to_view_credits = False

def syntax_error_detected():

    global current_seconds, running, results

    global exit_count, game_font, syntax_error, pressed

    pygame.draw.rect(screen, ("black") ,(display.x + 5, display.y + 5, WIDTH - 30, 190), border_radius=10)


    name_font = pygame.font.Font("fonts/Digital 3.ttf", 40)
    name = name_font.render("syntax/math error!", False, "white")
    screen.blit(name, (WIDTH // 2 - name.get_width() // 2, 90))

    latest_seconds = time.gmtime()[5]

    if latest_seconds %2 == 0:
        exit_count += 2

    if exit_count == 68:
        if len(pressed) > 0:
            pressed = []
            #pressed.remove(pressed[0])
            output = 0

        syntax_error = False
        exit_count = 0
 
     
running = True

while running:

    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exiting = True

        if event.type == pygame.MOUSEBUTTONDOWN:
             pass

        if event.type == pygame.MOUSEBUTTONUP:
            clicked += 1
            Button_released = True

    Display.draw_display(display)
    Buttons.draw_button_zone(buttons)

    create_all_buttons()

    show_typings()

    if button_number == 20:
        button_number = 0

    if len(str(output)) > 9:
        output = round(output, 10)


    show_output()

    if syntax_error:
        syntax_error_detected()

    if exiting:
        end_screen()

    if wants_to_view_credits:
        credits_screen()
    
    pygame.display.flip()

pygame.quit()

