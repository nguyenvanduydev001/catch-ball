import pygame
import sys
import cv2
from cvzone.HandTrackingModule import HandDetector
import random
from pygame import mixer

width = 1366
height = 768

# opencv code
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# Hand Detector
detector = HandDetector(maxHands=1, detectionCon=0.8)

# Initialize the pygame
pygame.init()

# background sounds
mixer.music.load('music/nhacnen.mp3')
mixer.music.play(loops=-1)

closedHand_sound = mixer.Sound('music/slap.mp3')
catching_sound = mixer.Sound('music/catching_sound.wav')

# Define the screen
screen = pygame.display.set_mode((width, height))

# Timer
clock = pygame.time.Clock()
currentTime = 1

# Title and Icon
pygame.display.set_caption("Catch Ball")
icon = pygame.image.load('images/ball_32.png').convert_alpha()
pygame.display.set_icon(icon)
backgroundImg = pygame.image.load('images/Catch_Ball.png').convert()

# Player
playerPosition = [370, 480]
playerMovement = [0, 0]
x = width / 2 - 64
y = height / 2 - 64
openHandImg = pygame.image.load('images/openHand.png').convert_alpha()
openHandImg = pygame.transform.scale(openHandImg, (128, 128))
openHand_rect = openHandImg.get_rect(topleft=(x, y))

closedHandImg = pygame.image.load('images/closedHand.png').convert_alpha()
closedHandImg = pygame.transform.scale(closedHandImg, (128, 128))
closedHand_rect = closedHandImg.get_rect(topleft=(x, y))

# Insects
InsectImg = []
InsectX = []
InsectY = []
insect_rect = []
insectMoveX = []
insectMoveY = []
numberOfInsects = 10
for i in range(numberOfInsects):
    InsectX.append(random.randint(0, 1366))
    InsectY.append(random.randint(0, 768))
    InsectImg.append(pygame.image.load('images/ball_32.png').convert_alpha())
    insect_rect.append(InsectImg[i].get_rect(topleft=(InsectX[i], InsectY[i])))
    insectMoveX.append(10)
    insectMoveY.append(8)

# Game Texts
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
gameOver_font = pygame.font.Font('freesansbold.ttf', 100)
textX = 10
textY = 10

# Game State
game_over = False
game_over_start_time = 0

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def show_timer():
    global game_over_start_time

    if not game_over:
        remaining_time = int(60 - currentTime / 1000)
    else:
        remaining_time = 0

    if remaining_time >= 10:
        timer = font.render("Time: " + str(remaining_time), True, (255, 255, 255))
    else:
        timer = font.render("Time: " + str(remaining_time), True, (255, 0, 0))

    screen.blit(timer, (1210, 10))

    if remaining_time <= 0 and not game_over:
        game_over_start_time = pygame.time.get_ticks()
        game_over_screen()

def game_over_screen():
    global game_over
    game_over = True
    game_over_text = gameOver_font.render("Game Over!", True, (255, 0, 0))
    screen.blit(game_over_text, (width / 2 - 300, height / 2 - 30))

indexes_for_closed_fingers = [8, 12, 16, 20]

# Game Loop
catch_insect_with_openHand = False
fingers = [0, 0, 0, 0]
while True:
    screen.blit(backgroundImg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cap.release()
            cv2.destroyAllWindows()
            pygame.quit()
            sys.exit()

    # opencv code
    success, frame = cap.read()
    hands, frame = detector.findHands(frame)

    if hands:
        lmList = hands[0]
        positionOfTheHand = lmList['lmList']
        openHand_rect.left = width - positionOfTheHand[9][0] * 1.5
        openHand_rect.top = (positionOfTheHand[9][1] - 200) * 1.5
        closedHand_rect.left = (positionOfTheHand[9][0] - 200) * 1.5
        closedHand_rect.top = (positionOfTheHand[9][1] - 200) * 1.5

        hand_is_closed = 0
        for index in range(0, 4):
            if positionOfTheHand[indexes_for_closed_fingers[index]][1] > positionOfTheHand[indexes_for_closed_fingers[index] - 2][1]:
                fingers[index] = 1
            else:
                fingers[index] = 0
            if fingers[0] * fingers[1] * fingers[2] * fingers[3]:
                if hand_is_closed and catch_insect_with_openHand == False:
                    closedHand_sound.play()
                hand_is_closed = 0
                screen.blit(closedHandImg, closedHand_rect)
                if not game_over:
                    for iteration in range(numberOfInsects):
                        if openHand_rect.colliderect(insect_rect[iteration]) and catch_insect_with_openHand:
                            score_value += 1
                            catching_sound.play()
                            catch_insect_with_openHand = False
                            insect_rect[iteration] = InsectImg[iteration].get_rect(topleft=(random.randint(0, 1366), random.randint(0, 768)))

                catch_insect_with_openHand = False
            else:
                screen.blit(openHandImg, openHand_rect)
                hand_is_closed = 1
                for iterate in range(numberOfInsects):
                    if openHand_rect.colliderect(insect_rect[iterate]):
                        catch_insect_with_openHand = True

    cv2.imshow("webcam", frame)

    for i in range(numberOfInsects):
        insect_rect[i].right += insectMoveX[i]
        if insect_rect[i].right <= 16:
            insectMoveX[i] += 10
        elif insect_rect[i].right >= width:
            insectMoveX[i] -= 10

        insect_rect[i].top += insectMoveY[i]
        if insect_rect[i].top <= 0:
            insectMoveY[i] += 8
        elif insect_rect[i].top >= height - 32:
            insectMoveY[i] -= 8
        screen.blit(InsectImg[i], insect_rect[i])

    show_score(textX, textY)
    if not game_over:
        currentTime = pygame.time.get_ticks()
    show_timer()

    if game_over:
        game_over_screen()
        if pygame.time.get_ticks() - game_over_start_time > 5000:  # 5000 milliseconds = 5 seconds
            pygame.time.wait(5000)  # Wait for 5 seconds before exiting
            break  # Exit the game loop

    pygame.display.update()
    clock.tick(60)

# End game and cleanup
cap.release()
cv2.destroyAllWindows()
pygame.quit()
sys.exit()
