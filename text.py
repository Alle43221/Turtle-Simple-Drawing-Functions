
import turtle

class Figures:
    def draw_square(side_length):
        side_length_adjusted = side_length
        for i in range(1, 5):
            skk.forward(side_length_adjusted)
            skk.right(90)

    def draw_rectangle(side1_length, side2_length):
        side1_length_adjusted = side1_length
        side2_length_adjusted = side2_length
        skk.forward(side1_length_adjusted)
        skk.right(90)
        skk.forward(side2_length_adjusted)
        skk.right(90)
        skk.forward(side1_length_adjusted)
        skk.right(90)
        skk.forward(side2_length_adjusted)
 
    def draw_isosceles_triangle(side1_length, side2_length):
        skk.forward(side2_length)
        skk.left(105)
        skk.forward(side1_length)
        skk.left(150)
        skk.forward(side1_length)

    def draw_heart():
        skk.begin_fill()
        skk.left(90)
        skk.forward(100)
        skk.circle(50, 230)
        skk.forward(100)
        skk.left(85)
        skk.forward(100)
        skk.circle(50, 230)
        skk.forward(100)
        skk.end_fill()

    def draw_spiral():
        skk.pensize(10)
        for i in range(0, 8):
            skk.circle(90-i*10, 180)

    def draw_concentric_cicles(number_of_circles):
        for i in range(1, number_of_circles+1):
            skk.circle(10*i, 360)



if __name__ == '__main__':
    wn = turtle.Screen()
    wn.bgcolor("red")
    wn.title("Turtle")
    skk = turtle.Turtle()
    skk.shape("turtle")
    skk.color("white")


    #Figures.draw_square(100)
    #Figures.draw_rectangle(100, 200)
    #Figures.draw_isosceles_triangle(200, 100)
    #Figures.draw_heart()
    #Figures.draw_spiral()
    #Figures.draw_concentric_cicles(7)


    turtle.done()
