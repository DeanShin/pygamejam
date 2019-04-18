class Button():

    def __init__(self, pygame, x, y, w, h, hasfunction=True, button_id=-1):
        self.rect = pygame.Rect(x, y, w, h)
        self.mode = 0
        self.thickness = 2
        self.active = False
        self.hasfunction = hasfunction
        self.button_id = button_id

    def update_text(self, text_sur):
        self.text_surface = text_sur
        self.text_pos = ((self.rect[0]+(self.rect[2]/2)-self.text_surface.get_width()/2), \
        (self.rect[1]+(self.rect[3]/2)-self.text_surface.get_height()/2))

    def handle_event(self, pygame, event):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if self.rect.collidepoint(event.pos):
                self.mode = 2
                # print("Boop.")
                # print(self.button_id)
                return self.button_id
        

    def hover_check(self, mouse_pos):
        if self.hasfunction: 
            if self.rect.collidepoint(mouse_pos):
                self.mode = 1
                return self.button_id  
            else:
                self.mode = 0
        return False # Check the next button.
        # From here, return temp var in order to display cost to upgrade for player

    def draw(self, pygame, sur, ic=(15,15,255), hc=(255,0,255), ac=(0,127,255)):
        if self.mode == 0: color = ic
        elif self.mode == 1:
            color = hc
            self.mode = 0
        else: color = ac
        # Blit the rect.
        pygame.draw.rect(sur, color, self.rect, 0)
        # Blit the text.
        sur.blit(self.text_surface, self.text_pos)
