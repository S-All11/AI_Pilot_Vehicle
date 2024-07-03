import tkinter as tk

class BlockBreakerGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Block Breaker Game")
        self.master.geometry("400x400")

        self.canvas = tk.Canvas(master, width=400, height=400, bg="black")
        self.canvas.pack()

        self.paddle = self.canvas.create_rectangle(160, 380, 240, 390, fill="white")
        self.ball = self.canvas.create_oval(190, 190, 210, 210, fill="white")

        self.ball_speed = [4, -4]
        self.blocks = []

        for i in range(5):
            for j in range(5):
                block = self.canvas.create_rectangle(80 * j, 20 * i, 80 * (j + 1), 20 * (i + 1), fill="blue")
                self.blocks.append(block)

        self.master.bind("<KeyPress-a>", self.move_paddle_left)
        self.master.bind("<KeyPress-d>", self.move_paddle_right)

        self.game_clear = False

        self.update()

    def move_paddle_left(self, event):
        self.canvas.move(self.paddle, -20, 0)

    def move_paddle_right(self, event):
        self.canvas.move(self.paddle, 20, 0)

    def update(self):
        if not self.game_clear:
            self.canvas.move(self.ball, self.ball_speed[0], self.ball_speed[1])

            ball_pos = self.canvas.coords(self.ball)

            if ball_pos[0] <= 0 or ball_pos[2] >= 400:
                self.ball_speed[0] = -self.ball_speed[0]

            if ball_pos[1] <= 0:
                self.ball_speed[1] = -self.ball_speed[1]

            if ball_pos[3] >= 400:
                self.game_over()

            if self.hit_paddle(ball_pos) or self.hit_block(ball_pos):
                self.ball_speed[1] = -self.ball_speed[1]

            if not self.blocks:
                self.game_clear = True
                self.canvas.create_text(200, 200, text="Game Clear", font=("Helvetica", 16), fill="green")

            self.master.after(10, self.update)

    def hit_paddle(self, ball_pos):
        paddle_pos = self.canvas.coords(self.paddle)
        return ball_pos[2] >= paddle_pos[0] and ball_pos[0] <= paddle_pos[2] and ball_pos[3] >= paddle_pos[1]

    def hit_block(self, ball_pos):
        for block in self.blocks:
            block_pos = self.canvas.coords(block)
            if ball_pos[2] >= block_pos[0] and ball_pos[0] <= block_pos[2] and ball_pos[3] >= block_pos[1] and ball_pos[1] <= block_pos[3]:
                self.canvas.delete(block)
                self.blocks.remove(block)
                return True
        return False

    def game_over(self):
        self.canvas.create_text(200, 200, text="Game Over", font=("Helvetica", 16), fill="red")

if __name__ == "__main__":
    root = tk.Tk()
    game = BlockBreakerGame(root)
    root.mainloop()
