from Tkinter import *
import random

class ColorGame(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.color_list = ['blue','red','green']
        self.user_score = 0
        self.initUI(parent)

    def initUI(self, parent):
        self.var = StringVar()
        self.var.set('e') # intial value to uncheck buttons

        self.fast_button = Checkbutton(self, text = 'fast', variable = self.var, onvalue = 'fast') #'fast' becomes the value of self.var
        self.fast_button.pack()

        self.normal_button = Checkbutton(self, text = 'normal', variable = self.var, onvalue = 'normal')
        self.normal_button.pack()

        self.slow_button = Checkbutton(self, text = 'slow', variable = self.var,onvalue = 'slow')
        self.slow_button.pack()

        self.start_button = Button(self, text = 'START', width = 5, command = self.Start_game)
        self.start_button.pack()

        self.stop_button = Button(self, text = 'STOP', width = 5, command = self.Stop_game)
        self.stop_button.pack()

        self.user_color_label = Label(self, text = 'Your Color', width = 20, height = 2, relief = 'raised')
        self.user_color_label.pack()

        self.score_label = Label(self, text = 'Score', width = 10, relief = 'raised')
        self.score_label.pack()

        self.button_1 = Button(self, text = 'Button 1', width = 20, height = 5, command = self.getValue_Color1)
        self.button_1.pack()

        self.button_2 = Button(self, text = 'Button 2', width = 20, height = 5, command = self.getValue_Color2)
        self.button_2.pack()

        self.button_3 = Button(self, text = 'Button 3', width = 20, height = 5, command = self.getValue_Color3)
        self.button_3.pack()
        self.pack()


    def Start_game(self):

        speed = self.var.get() # getting the selected speed
        if speed == 'fast':
            self.speed = 500
        if speed == 'normal':
            self.speed = 1000
        if speed == 'slow':
            self.speed = 2000
        self.user_color = random.choice(self.color_list) # choose a random color
        self.user_color_label.configure(bg = self.user_color)
        self.stop = False
        self.game_main()

    # main function that configures the UI and updates it depending on selected speed
    def game_main(self):

        # self.user_color = random.choice(self.color_list)
        # self.user_color_label.configure(bg=self.user_color)
        # Uncomment these and comment the ones above if you want the color to change every next frame

        if self.stop:
            return
        score_list = [random.randint(1,100),random.randint(1,100),random.randint(1,100)]
        colors_list = [random.choice(self.color_list),random.choice(self.color_list),random.choice(self.color_list)]
        max_list = [0]
        index = 0
        for color in colors_list:
            if color == self.user_color:
                max_list.append(score_list[index])
            index+=1
        self.max = max(max_list)
        self.button_1.configure(bg = colors_list[0], text = score_list[0], font = ('','12','bold'))
        self.button_2.configure(bg=colors_list[1], text=score_list[1], font=('', '12', 'bold'))
        self.button_3.configure(bg=colors_list[2], text=score_list[2], font=('', '12', 'bold'))

        self.update_idletasks()
        self.updating = self.after(self.speed, self.game_main)

    def getValue_Color1(self):
        if self.button_1.cget('text') == self.max and self.button_1.cget('bg') == self.user_color:
            self.user_score += 10
        else:
            self.user_score -= 5
        self.score_label.configure(text='Score: ' + str(self.user_score))

    def getValue_Color2(self):
        if self.button_2.cget('text') == self.max and self.button_2.cget('bg') == self.user_color:
            self.user_score += 10
        else:
            self.user_score -= 5
        self.score_label.configure(text='Score: ' + str(self.user_score))

    def getValue_Color3(self):
        if self.button_3.cget('text') == self.max and self.button_3.cget('bg') == self.user_color:
            self.user_score += 10
        else:
            self.user_score -= 5
        self.score_label.configure(text='Score: ' + str(self.user_score))


    def Stop_game(self):
        self.stop = True
        self.user_score = 0 # Score reset
        self.score_label.configure(text='Score: ' + str(self.user_score)) # Update score value after reset


def main():

    root = Tk()
    root.title('Color game')
    root.geometry('900x500+100+100')
    app = ColorGame(root)
    root.mainloop()


main()