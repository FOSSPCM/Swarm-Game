"""
Swarm Game
Written by Mac Young on April 8, 2023.
"""
import arcade
import random

# Constants
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800
PLAYER_SPRITE = "images/fox.png"
ENEMY_SPRITE = "images/poison.png"
FRIEND_SPRITE = "images/diamond.png"
P_SPRITE_SCALE = 0.25
FRIENDS = 50
ENEMY_SPAWN = 0.45
FRIEND_SPAWN = 1.25

# This class handles the enemies and friends that fy on screen.
class flying_sprite(arcade.Sprite):
    def update(self):
        super().update()
        if self.right < 0: self.remove_from_sprite_lists()
        if self.top < 0: self.remove_from_sprite_lists()

# game_core is where the magic happpens.
class game_core(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, title="Swarm Game")
        # Starting location of player
        self.x = WINDOW_WIDTH / 2
        self.y = WINDOW_HEIGHT / 2
        # Sprite lists
        self.enemies_list = arcade.SpriteList()
        self.friends_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        # Pausing the game
        self.paused = False
    
    # Initial game setup.
    def setup(self):
        # Drawing our player character.
        self.player = arcade.Sprite(PLAYER_SPRITE, P_SPRITE_SCALE)
        self.player.center_x = self.x
        self.player.center_y = self.height / 2
        self.all_sprites.append(self.player)
        
        # How many friends left to get
        self.friends_left = FRIENDS
        
        # Are we dead?
        self.player_down = False
        
        # Did we win?
        self.success = False
        
        # Spawn a new enemy ever 0.3 seconds.
        arcade.schedule(self.add_enemy, ENEMY_SPAWN)
        
        # Spawn a new friend every one and a half seconds.
        arcade.schedule(self.add_friend, FRIEND_SPAWN)
        
        # Load some sound effects.
        self.death_sound = arcade.load_sound("sfx/lightning.wav")
        self.pickup_sound = arcade.load_sound("sfx/shortbeep.wav")
        self.win_sound = arcade.load_sound("sfx/startup.wav")
    
    # on_update executes some checks to make sure things function properly as sprites fly and collide 
    # wwith the player. It also handles the win condition.
    def on_update(self, delta_time: float):
        # If we are paused, don't do anything.
        if self.paused: return
        
        # If we haven't won yet, then check to see if we crashed into an enemy and died.
        if self.friends_left > 0 and self.player_down == False:
            if self.player.collides_with_list(self.enemies_list):
                self.player.remove_from_sprite_lists()
                self.player_down = True
                arcade.play_sound(self.death_sound)
        
        # Check to see if we picked up a jewel.
        if self.player_down == False:
            friend_hit_list = arcade.check_for_collision_with_list(self.player, self.friends_list)
            for f in friend_hit_list:
                f.remove_from_sprite_lists()
                self.friends_left -= 1
                if self.friends_left < 0: self.friends_left = 0
                arcade.play_sound(self.pickup_sound)
        
        # Check to see if we won.
        if self.friends_left == 0 and self.success == False:
            arcade.unschedule(self.add_enemy)
            arcade.unschedule(self.add_friend)
            self.success = True
            arcade.play_sound(self.win_sound)
            
        self.all_sprites.update()
        
    # on_draw is the function used for drawing the sprites and text on screen.
    def on_draw(self):
        self.clear()
        arcade.start_render()
        
        # The indicator for how many jewels to pick up.
        arcade.draw_text(
            f"Jewels left: {self.friends_left}", 20, 20, arcade.color.WHITE, 16,
            font_name = "Kenny Pixel",
        )
        
        # What you see when you win.
        if self.friends_left == 0:
            arcade.draw_text(
                "Congratulations!", 0, ((WINDOW_WIDTH/2) * 1.25), arcade.color.GREEN, 
                24, width=WINDOW_WIDTH, align="center",
            )
        
        self.all_sprites.draw()
        
    # on_mouse_motion checks to see if the mouse moved, and if so, update the player character
    # to show up at the mouse cursor's new position.
    def on_mouse_motion(self, x, y, dx, dy):
        self.player.center_x = x
        self.player.center_y = y
    
    # on_key_press handles keyboard buttons. Q to Quit, and P to Pause.
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.Q: arcade.close_window()
        if symbol == arcade.key.P:
            self.paused = not self.paused
            if self.paused:
                arcade.unschedule(self.add_enemy)
                arcade.unschedule(self.add_friend)
            else:
                arcade.schedule(self.add_enemy, ENEMY_SPAWN)
                arcade.schedule(self.add_friend, FRIEND_SPAWN)
    
    # add_enemy creates an enemy and adds it to the list.
    def add_enemy(self, delta_time: float):
        enemy = flying_sprite(ENEMY_SPRITE)
        h_vel = 0
        v_vel = 0
        
        # Placement of the new sprite as well as its velocity.
        placement = random.randint(1, 4)
        if placement == 1:      # From right      
            enemy.left = random.randint(self.width, self.width + 10)
            enemy.top = random.randint(10, self.height - 10)
            h_vel = random.randint(-8, -1) 
        elif placement == 2:    # From left
            enemy.right = random.randint(-10, 0)
            enemy.top = random.randint(10, self.height - 10)
            h_vel = random.randint(1, 8)
        elif placement == 3:    # From above
            enemy.left = random.randint(10, self.width - 10)
            enemy.top = random.randint(self.height, self.height + 10)
            v_vel = random.randint(-8, -1)
        else:                   # From below
            enemy.left = random.randint(10, self.width - 10)
            enemy.bottom = random.randint(-10, 0)
            v_vel = random.randint(1, 8)
        
        # Apply the settings.
        enemy.velocity = (h_vel, v_vel)
        self.enemies_list.append(enemy)
        self.all_sprites.append(enemy)
        
    # add_friend creates a friend and adds it to the list. It's identical to add_enemy.
    def add_friend(self, delta_time: float):
        friend = flying_sprite(FRIEND_SPRITE)
        h_vel = 0
        v_vel = 0
        
        # Placement of the new sprite as well as its velocity.
        placement = random.randint(1, 4)
        if placement == 1:      # From right      
            friend.left = random.randint(self.width, self.width + 10)
            friend.top = random.randint(10, self.height - 10)
            h_vel = random.randint(-8, -1) 
        elif placement == 2:    # From left
            friend.left = random.randint(-10, 0)
            friend.top = random.randint(10, self.height - 10)
            h_vel = random.randint(1, 8)
        elif placement == 3:    # From above
            friend.left = random.randint(10, self.width - 10)
            friend.top = random.randint(self.height, self.height + 10)
            v_vel = random.randint(-8, -1)
        else:                   # From below
            friend.left = random.randint(10, self.width - 10)
            friend.bottom = random.randint(-10, 0)
            v_vel = random.randint(1, 8)
            
        # Apply the settings.
        friend.velocity = (h_vel, v_vel)
        self.friends_list.append(friend)
        self.all_sprites.append(friend)

game = game_core()
game.setup()
arcade.run()