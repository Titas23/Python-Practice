import random 

white_balls = [num for num in range(1, 60)]

white_ball_selection = random.sample(white_balls, 5)
for i in range(5):
    white_ball_selection[i] = str(white_ball_selection[i])
print("White Balls:", " ".join(white_ball_selection))

power_ball = random.randint(1, 35)
print("Powerball:", power_ball)



