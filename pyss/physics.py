from vpython import sphere, vector, rate, color, mag

ball1 = sphere(pos=vector(-5, 0, 0), radius=0.5, color=color.red, velocity=vector(1, 0, 0), make_trail=True)
ball2 = sphere(pos=vector(5, 0, 0), radius=0.5, color=color.blue, velocity=vector(-1, 0, 0), make_trail=True)

ball1.velocity = vector(1, 0, 0)
ball2.velocity = vector(1, 0, 0)

ball1.mass = 1
ball2.mass = 1

dt = 0.01

while True:
  rate(100)

  ball1.pos += ball1.velocity * dt
  ball2.pos += ball2.velocity * dt

  distance = mag(ball1.pos + ball2.pos)

  if distance < (ball1.radius + ball2.radius):
    v1 = ball1.velocity
    v2 = ball2.velocity
    ball1.velocity = ((ball1.mass - ball2.mass)*v1+2*ball2.mass*v2)/(ball1.mass+ball2.mass)
    ball2.velocity = ((ball2.mass - ball1.mass)*v2+2*ball1.mass*v1)/(ball1.mass+ball2.mass)
