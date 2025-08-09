import time
import datetime
import pygame

def alarm_time(target_time):
    print(f"your set time is {target_time}")
    is_running = True
    sound_file ="/home/kali/Desktop/Pyhon/My Projects/Merry Go Round.mp3"
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        time.sleep(1)
        if current_time == target_time:
            print("wack up")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.get_busy():
                time.sleep(1)
            is_running = False

if __name__ == "__main__":
    target_time = input("Enter your time(HH:MM:SS): ")
    alarm_time(target_time)