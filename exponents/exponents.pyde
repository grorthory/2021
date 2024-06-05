size(1200, 1200)
x = 0
for j in range(10):
    x=0
    for i in range(20):
        circle(i*x+50+j*x, i*x+50, 100)
        x=x+5
