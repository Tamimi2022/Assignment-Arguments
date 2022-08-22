# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# Part 1
def greet(name = 'Attamimi', greeting_template = 'Hello, <name>!'):
    return greeting_template.replace('<name>', name)


# Part 2
def force(mass, body='earth'):
    
    bodies = dict({
        'sun': 274,
        'jupiter': 24.92,
        'neptune': 11.15,
        'saturn': 10.4,
        'earth': 9.8,
        'uranus': 8.87,
        'venus': 8.87,
        'mars': 3.71,
        'mercury': 3.7,
        'moon': 1.62,
        'pluto': 0.6
    })
  
    return round(mass * bodies[body], 1) # 1 Desimal


# Part 3
def pull(m1, m2, d):
    G = 6.674 * (10 ** - 11) # G is the gravitational constant
    return G * ((m1 * m2) / (d ** 2))

print(greet())