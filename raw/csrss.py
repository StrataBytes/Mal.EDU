import pygame
import sys
import time
import keyboard
import os

"""Welcome to the code! If you wish to build yourself, be sure to read the WHOLE readme in Github."""
"""Please respect the GPLv3 lisense and give credit where it is due ;)"""

def resource_path(relative_path):
    #get absolute path to resource, works for dev and for PyInstaller
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

image_path = resource_path('img.jpg')

def main():
    pygame.init()
    infoObject = pygame.display.Info()
    screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h), pygame.FULLSCREEN)
    bg_image = pygame.image.load(image_path).convert()
    bg_image = pygame.transform.scale(bg_image, (infoObject.current_w, infoObject.current_h))

    #Key blockers
    keyboard.add_hotkey("alt + f4", lambda: None, suppress =True)
    keyboard.add_hotkey("alt + tab", lambda: None, suppress =True)
    keyboard.add_hotkey("win + tab", lambda: None, suppress =True)
    #keyboard.add_hotkey("control + alt + delete", lambda: None, suppress =True)

    #get the center of the screen
    center_x, center_y = infoObject.current_w // 2, infoObject.current_h // 2

    #time want to stop locking the mouse in the center
    unlock_time = time.time() + 5  #5 seconds from now

    running = True
    while running:
        current_time = time.time()

        #lock the mouse in the center for the first 5 seconds
        if current_time < unlock_time:
            pygame.mouse.set_pos(center_x, center_y)
            pygame.event.set_grab(True)  #grab the mouse
        else:
            pygame.event.set_grab(False)  #release the mouse after 5 seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                #debug - escape
            # elif event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_ESCAPE:  
            #         running = False
            elif event.type == pygame.ACTIVEEVENT:  #listen for focus events
                if event.gain == 0:  #if the window loses focus
                    running = False  #stop the program

        screen.blit(bg_image, (0, 0))
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
