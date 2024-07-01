import sys
from PyQt5 import QtWidgets, QtGui, QtCore, uic


Ui_MainWindow, QMainWindow = uic.loadUiType("Game_window_energybar.ui")

class MyWindowClass(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindowClass, self).__init__(parent)
        self.setupUi(self)
        self.doctor = False
        self.walking = False
        self.sleeping = False
        self.playing = False
        self.eating = False
        self.happiness = 100  
        self.health = 100  
        self.energy = 100  
        self.mood = 100  
        self.idle_pixmaps = [] 
        self.sleeping_pixmaps = []  
        self.walking_pixmaps = []  
        self.playing_pixmaps = []  

       
        self.load_images_and_animations()

        self.feed_Button.clicked.connect(self.btn_feedClicked)
        self.walk_Button.clicked.connect(self.btn_walkClicked)
        self.play_Button.clicked.connect(self.btn_playClicked)
        self.doctor_Button.clicked.connect(self.btn_doctorClicked)

        # //Setup timers for decreasing statuses
        self.energy_timer = QtCore.QTimer(self)
        self.energy_timer.timeout.connect(self.decrease_energy)
        self.energy_timer.start(1000)  # Decrease energy every second (juust for presentation)

        self.hunger_timer = QtCore.QTimer(self)
        self.hunger_timer.timeout.connect(self.decrease_hunger)
        self.hunger_timer.start(2000)  # Decrease hunger every 2 seconds

        self.mood_timer = QtCore.QTimer(self)
        self.mood_timer.timeout.connect(self.decrease_mood)
        self.mood_timer.start(2000)  # Decrease mood every 2 seconds

        # //Setup a timer for health decrease when hunger is critical
        self.health_loss_timer = QtCore.QTimer(self)
        self.health_loss_timer.timeout.connect(self.decrease_health_due_to_hunger)
        self.health_loss_timer.start(20000)  # Check hunger every 20 seconds

        # //Setup cooldown timers
        self.feed_cooldown_timer = QtCore.QTimer(self)
        self.feed_cooldown_timer.setSingleShot(False)
        self.feed_cooldown_timer.timeout.connect(self.reset_feed_button)
        self.feed_button_cooldown = 20000  

        self.doctor_cooldown_timer = QtCore.QTimer(self)
        self.doctor_cooldown_timer.setSingleShot(True)
        self.doctor_cooldown_timer.timeout.connect(self.reset_doctor_button)
        self.doctor_button_cooldown = 20000 

        self.walk_play_cooldown_timer = QtCore.QTimer(self)
        self.walk_play_cooldown_timer.setSingleShot(True)
        self.walk_play_cooldown_timer.timeout.connect(self.reset_walk_play_buttons)
        self.walk_play_button_cooldown = 20000  

        # //Initialize idle timer
        self.idle_timer = QtCore.QTimer(self)
        self.idle_timer.timeout.connect(self.restart_idle_timer)
        self.idle_timeout_ms = 20000  
        self.idle_timer.start(self.idle_timeout_ms)

        # //Initialize animation frame indices
        self.current_walking_frame = 0
        self.current_playing_frame = 0
        self.current_sleeping_frame = 0
        self.current_idle_frame = 0

    def load_images_and_animations(self):
        # //Load images into buttons
        self.load_image_into_button()

        # //List of image file paths for idle animation frames
        self.idle_frames = [
            r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\Idle (1).png",
            r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\Idle (3).png",
            r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\Idle (4).png",
            r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\Idle (5).png",
            r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\Idle (6).png",
            r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\Idle (7).png",
            r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\Idle (8).png",
            r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\Idle (9).png",
            r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\Idle (10).png"
        ]

        # //List of image file paths for sleeping animation frames
        self.sleeping_frames = [
            r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\Dead (5).png",
            r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\Dead (6).png",
            r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\Dead (7).png",
            r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\Dead (8).png"
        ]

        # //List of image file path for walking animation frames
        self.walking_frames = [
            r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\Walk (1).png",
            r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\Walk (2).png",
            r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\Walk (3).png",
            r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\Walk (4).png",
            r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\Walk (5).png",
            r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\Walk (6).png",
            r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\Walk (7).png",
            r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\Walk (8).png",
            r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\Walk (9).png",
            r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\Walk (10).png"
        ]

        # //List of image file path for playing animation frames
        self.playing_frames = [
            r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\Jump (1).png",
            r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\Jump (2).png",
            r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\Jump (3).png",
            r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\Jump (10).png",
            r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\Jump (11).png"
        ]

        # //Create QPixmap for idle, sleeping, walking, and playing frames
        self.idle_pixmaps = [QtGui.QPixmap(frame) for frame in self.idle_frames]
        self.sleeping_pixmaps = [QtGui.QPixmap(frame) for frame in self.sleeping_frames]
        self.walking_pixmaps = [QtGui.QPixmap(frame) for frame in self.walking_frames]
        self.playing_pixmaps = [QtGui.QPixmap(frame) for frame in self.playing_frames]

        # Initialize label_6 with the first frame of idle animation
        if self.idle_pixmaps:
            self.current_idle_frame = 0
            self.label_6.setPixmap(self.idle_pixmaps[self.current_idle_frame])
            self.label_6.setScaledContents(True)

            # Setup a timer for idle animation
            self.idle_animation_timer = QtCore.QTimer(self)
            self.idle_animation_timer.timeout.connect(self.next_idle_frame)
            self.idle_animation_timer.start(250)

    def load_image_into_button(self):
       
        pixmap_feed = QtGui.QPixmap(r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\food.png")
        pixmap_walk = QtGui.QPixmap(r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\walk.png")
        pixmap_play = QtGui.QPixmap(r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\play.png")
        pixmap_medic = QtGui.QPixmap(r"C:\Users\Mariy\Desktop\V-Pet Game\Sourses\help.png")

       
        button_size = self.feed_Button.size()  # <-- For all buttons have the same size
        pixmap_feed = pixmap_feed.scaled(button_size, QtCore.Qt.KeepAspectRatio)
        pixmap_walk = pixmap_walk.scaled(button_size, QtCore.Qt.KeepAspectRatio)
        pixmap_play = pixmap_play.scaled(button_size, QtCore.Qt.KeepAspectRatio)
        pixmap_medic = pixmap_medic.scaled(button_size, QtCore.Qt.KeepAspectRatio)

        # Set images as icons for buttons
        self.feed_Button.setIcon(QtGui.QIcon(pixmap_feed))
        self.feed_Button.setIconSize(button_size)

        self.walk_Button.setIcon(QtGui.QIcon(pixmap_walk))
        self.walk_Button.setIconSize(button_size)

        self.play_Button.setIcon(QtGui.QIcon(pixmap_play))
        self.play_Button.setIconSize(button_size)

        self.doctor_Button.setIcon(QtGui.QIcon(pixmap_medic))
        self.doctor_Button.setIconSize(button_size)

    def next_idle_frame(self):  # < -- Advance to the next frame in idle animation
       
        self.current_idle_frame = (self.current_idle_frame + 1) % len(self.idle_pixmaps)
        self.label_6.setPixmap(self.idle_pixmaps[self.current_idle_frame])

    def next_sleeping_frame(self):
        
        self.current_sleeping_frame = (self.current_sleeping_frame + 1) % len(self.sleeping_pixmaps)
        self.label_6.setPixmap(self.sleeping_pixmaps[self.current_sleeping_frame])

    def next_walking_frame(self):
        
        self.current_walking_frame = (self.current_walking_frame + 1) % len(self.walking_pixmaps)
        self.label_6.setPixmap(self.walking_pixmaps[self.current_walking_frame])

    def next_playing_frame(self):
        
        self.current_playing_frame = (self.current_playing_frame + 1) % len(self.playing_pixmaps)
        self.label_6.setPixmap(self.playing_pixmaps[self.current_playing_frame])

    def btn_feedClicked(self): # <-- # Restore hunger, decrease energy, and start cooldown timer
        
        if not self.feed_cooldown_timer.isActive():
            self.happiness = min(self.happiness + 20, 100)
            self.progressBar.setValue(self.happiness)
            self.decrease_energy(20)  
            self.restart_idle_timer()
            self.feed_cooldown_timer.start(self.feed_button_cooldown)

    def btn_walkClicked(self): # < -- # Restore mood, decrease energy, and start cooldown timer
        
        if not self.walk_play_cooldown_timer.isActive():
            self.mood = min(self.mood + 35, 100)
            self.progressBar_2.setValue(self.mood)
            self.decrease_energy(30)  
            self.restart_idle_timer()
            self.walk_play_cooldown_timer.start(self.walk_play_button_cooldown)

            # Start the walking animation
            self.start_animation(self.walking_pixmaps, self.next_walking_frame)

    def btn_playClicked(self): # <-- # Restore mood, decrease energy, and start cooldown timer
        
        if not self.walk_play_cooldown_timer.isActive():
            self.mood = min(self.mood + 20, 100)
            self.progressBar_2.setValue(self.mood)
            self.decrease_energy(25)  
            self.restart_idle_timer()
            self.walk_play_cooldown_timer.start(self.walk_play_button_cooldown)

            # Start the playing animation
            self.start_animation(self.playing_pixmaps, self.next_playing_frame)

    def btn_doctorClicked(self): # << -- # Doctor's visit restores health to max value and start cooldown timer
        
        if not self.doctor_cooldown_timer.isActive():
            self.health = min(self.health + 100, 100)
            self.progressBar_3.setValue(self.health)
            self.restart_idle_timer()
            self.doctor_cooldown_timer.start(self.doctor_button_cooldown)

    def start_animation(self, pixmap_list, next_frame_func):
        # Start an animation given a list of QPixmap objects and a function to advance frames
        if pixmap_list:
            # Stop any running animations
            self.stop_animations()

            # Setup a timer for the animation
            self.animation_timer = QtCore.QTimer(self)
            self.animation_timer.timeout.connect(next_frame_func)
            # Adjust the timeout interval based on the animation speed
            self.animation_timer.start(200) 

            # Show the first frame of animation immediately
            self.current_animation_frame = 0
            self.label_6.setPixmap(pixmap_list[self.current_animation_frame])
            self.label_6.setScaledContents(True)

    def decrease_energy(self, amount=1):
        self.energy = max(self.energy - amount, 0)
        self.progressBar_4.setValue(self.energy)
        print(f"Energy: {self.energy}")  
        if self.energy == 0:
            print("Starting sleep animation...")
            self.start_sleep_animation()

    def decrease_hunger(self):
        self.happiness = max(self.happiness - 1, 0)
        self.progressBar.setValue(self.happiness)
        if self.happiness == 0:
            QtWidgets.QMessageBox.information(self, "Game Over", "Your pet is too hungry!", QtWidgets.QMessageBox.Ok)

        if self.happiness <= 50:
            self.decrease_health_due_to_hunger()

    def decrease_mood(self):
        self.mood = max(self.mood - 1, 0)
        self.progressBar_2.setValue(self.mood)
        if self.mood == 0:
            QtWidgets.QMessageBox.information(self, "Game Over", "Your pet is too sad!", QtWidgets.QMessageBox.Ok)

    def decrease_health_due_to_hunger(self):   # <-- # Decrease health due to critical hunger
        
        self.health = max(self.health - 3, 0)
        self.progressBar_3.setValue(self.health)

    def start_sleep_animation(self):
        # //Start sleeping animation when energy is 0
        if not self.sleeping and self.sleeping_pixmaps:
            print("Starting sleeping animation")
            self.sleeping = True
        # //Start sleeping animation logic here
            self.start_animation(self.sleeping_pixmaps, self.next_sleeping_frame)

        # //Stop energy decrease timer while sleeping
            self.energy_timer.stop()
        # //Stop other timers that decrease energy or mood
            # self.hunger_timer.stop() # optional
            self.mood_timer.stop()

        # Start timer to recover energy 
            self.sleep_recovery_timer = QtCore.QTimer(self)
            self.sleep_recovery_timer.timeout.connect(self.recover_energy)
            self.sleep_recovery_timer.start(1000)  # < -- Recover energy every 1000 ms (1 second)

    def recover_energy(self): # < --  # Increment energy by 5 points every second during sleep
   
        if self.energy < 100:
            self.energy = min(self.energy + 5, 100)
            self.progressBar_4.setValue(self.energy)

    # // Stop recovering energy if energy reaches maximum
        if self.energy == 100:
            self.sleep_recovery_timer.stop()

    def reset_feed_button(self):
        self.feed_cooldown_timer.stop()

    def reset_doctor_button(self):
        self.doctor_cooldown_timer.stop()

    def reset_walk_play_buttons(self):
        self.walk_play_cooldown_timer.stop()

    def restart_idle_timer(self):
        self.idle_timer.stop()
        self.idle_timer.start(self.idle_timeout_ms)

    def stop_animations(self):
        
        if hasattr(self, 'idle_animation_timer') and self.idle_animation_timer.isActive():
            self.idle_animation_timer.stop()
        if hasattr(self, 'animation_timer') and self.animation_timer.isActive():
            self.animation_timer.stop()
        if hasattr(self, 'sleep_recovery_timer') and self.sleep_recovery_timer.isActive():
            self.sleep_recovery_timer.stop()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myWindow = MyWindowClass()
    myWindow.show()
    sys.exit(app.exec_())