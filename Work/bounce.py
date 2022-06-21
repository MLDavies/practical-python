# bounce.py
#
# Exercise 1.5

'''
Prompt:
A rubber ball is dropped from a height of 100 meters and each time it hits the ground, 
it bounces back up to 3/5 the height it fell. Write a program bounce.py 
that prints a table showing the height of the first 10 bounces.
'''

height = 100
decay = 3/5
bounces = 1

print('Starting height:', height)
while bounces <= 10:
    height = height * decay
    print('Bounce number {} from height {}'.format(bounces, round(height,4)))
    #print(bounces, round(height, 4))
    bounces += 1