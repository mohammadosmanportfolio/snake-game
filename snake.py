from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        for pos in STARTING_POSITIONS:
            segment = Turtle('square')
            segment.color('white')
            segment.penup()
            segment.setpos(pos)
            segment.speed('fastest')
            self.segments.append(segment)

    def make_snake_bigger(self):
        segment = Turtle('square')
        segment.color('white')
        segment.penup()
        last_segment_heading = self.segments[len(self.segments) - 1].heading()
        new_segment_coordinates = self.get_new_segment_coordinates(last_segment_heading=last_segment_heading)
        segment.setpos(new_segment_coordinates)
        self.segments.append(segment)

    def reset(self):
        for seg in self.segments:
            seg.setpos(1000, 1000)
        self.segments.clear()
        for pos in STARTING_POSITIONS:
            segment = Turtle('square')
            segment.color('white')
            segment.penup()
            segment.setpos(pos)
            segment.speed('fastest')
            self.segments.append(segment)

    def get_new_segment_coordinates(self, last_segment_heading):
        last_segment = self.segments[len(self.segments) - 1]
        match last_segment_heading:
            case 0:
                return (last_segment.xcor() - 20, last_segment.ycor())
            case 180:
                return (last_segment.xcor() + 20, last_segment.ycor())
            case 90:
                return (last_segment.xcor(), last_segment.ycor() - 20)
            case 270:
                return (last_segment.xcor(), last_segment.ycor() + 20)
        
    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[seg - 1].pos()
            current_segment = self.segments[seg]
            current_segment.setpos(new_pos)
        self.segments[0].forward(MOVING_DISTANCE)
                
    def up(self):
        head_of_snake = self.segments[0]
        if head_of_snake.heading() != DOWN:
            head_of_snake.setheading(UP)

    def down(self):
        head_of_snake = self.segments[0]
        if head_of_snake.heading() != UP:
            head_of_snake.setheading(DOWN)
    
    def left(self):
        head_of_snake = self.segments[0]
        if head_of_snake.heading() != RIGHT:
            head_of_snake.setheading(LEFT)

    def right(self):
        head_of_snake = self.segments[0]
        if head_of_snake.heading() != LEFT:
            head_of_snake.setheading(RIGHT)

    def hit_body(self):
        head_of_snake = self.segments[0]
        for segment in self.segments[1:]:
            if head_of_snake.distance(segment) < 10:
                return True
        return False