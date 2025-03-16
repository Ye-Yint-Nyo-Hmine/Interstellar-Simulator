import numpy as np
import pygame
import random
from Interstellar.matter import Particle
from Interstellar.gravity import calculate_gravity
import sys


# Set up the window
WIDTH, HEIGHT, LENGTH = 1000, 800, 1000 # *Note: Length is defined to be used for 3D
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interstellar Simulator")
print("For updates: visit [https://github.com/Ye-Yint-Nyo-Hmine/Interstellar-Simulator]")
FPS = 60

# physics sets
deltaTime = 1e-20 # appropriate time for dt
particles = [] # stores matter inside
field = -1 # set render of field to True


def add_particle(x, y, z, mass, radius=None, vx=0, vy=0, vz=0, color=(255, 255, 255)):
    
    """
    :param x, y, z: x, y, z scalar positions of particle
    :param mass: mass of the particle (eg. around 1e24 for earth)
    :param vx, vy, vz: initial scalar velocity x, y, z of the particle
    :parm color: this should be pretty self-explanatory

    Description:
    This is a wrapper function that adds particle
    
    *Radius conditioning:
    1. Unlike other simulations, this one can handle a blackhole, therefore a radius can be adjusted by the user.
    2. Based on Einstein field equations & Schwarzschild radius, a radius can be set lower than schwarzschild radius to create a blackhole
    eg. Creating a blackhole
    add_particle(300, 300, 0, 5e47, radius=5) <- See that radius is confined to be lower to create a black hole

    """
    
    if radius != None:
        particles.append(Particle(x, y, z, mass, rad=radius, vx=vx, vy=vy, color=color))
    else:
        particles.append(Particle(x, y, z, mass, vx=vx, vy=vy, vz=vz, color=color))
        
    

def init_particles(num_particles=50, x_range=100, y_range=100, z_range=100, mass_range=[1e24, 5e24], vx=0, vy=0, vz=0, color=(255, 255, 255)):
    """
    :param num_particles: number of particles to generate
    :param x_range, y_range, z_range: the range away from border of the window to spawn matter
    :param mass_range: a 1d array of 2 elements defining lower and upper bound for the mass of generating particles
    :param vx, vy, vz: the initial scalar velocities for *all matter generated
    :param color: color for all matter generated
    
    Description:
    A wrapper function that generates particles random positions
    """
    for _ in range(num_particles):
        x = random.randint(x_range, WIDTH - x_range)
        y = random.randint(y_range, HEIGHT - y_range)
        z = random.randint(z_range, LENGTH - z_range)
        mass = random.uniform(mass_range[0], mass_range[1])
        add_particle(x, y, z, mass, vx=vx, vy=vy, vz=vz, color=color)


def samples(sample):
    """
    :param num: the sample name to be used
    
    Description:
    This function can be called to easily used already coordinated matter simulations
    
    It includes:
    - stable_sun_orbit --> an orbit of a sun with 3 dozens of planets (w/mass close to Earth)
    
    Usage:
    eg.
    samples("stable_sun_orbit")
    
    """
    def stable_sun_orbit():
        init_particles(30, mass_range=[1e+23, 5e+28], color=(110, 250, 255))
        add_particle(400, 400, 400, 2e30, color=(255,160, 0))
        
    def blackhole_with_earth():
        Blackhole = add_particle(400, 400, 0, 4e47, radius=5)
        Earth = add_particle(100, 200, 400, 5e24, color=(100, 200, 255))

    def sun_with_100_planets():
        Sun = add_particle(400, 400, 400, 2e30, color=(255, 180, 10))
        Planets = init_particles(100, mass_range=[1e22, 1e28], color=(80, 180, 250))

    def black_holes_2():
        Blackhole_A = add_particle(100, 800, 0, 4e47, radius=5)
        Blackhole_B = add_particle(800, 100, 0, 4e47, radius=5)
        Planets = init_particles(100)
        

    def stellar_nursery():
        Planets = init_particles(1000)    

        
    exec(f"{sample}()")


def update_particles():
    """
    Description:
    
    It calculates the gravitational attraction between particles, and update each particle base on deltaTime
    *Note: Forces are not normalize for higher realistic rendering, see gravity.py for more detail
    """
    forces = calculate_gravity(particles)
    for i in range(len(particles)):
        particles[i].vel += forces[i] / particles[i].mass * deltaTime

    for particle in particles:
        particle.update(deltaTime)
    
    
def draw_matters():
    """
    Description:
    It renders all matter for the simulation
    
    Feature:
    field can be toggled on/off with key press "f"
    if field is turned on, you can see the Einstein field's relativistic depth of each particle.
    To see it in full effect, try rendering a blackhole.
    
    *Note: Einstein field's relativistic depth is not to scale, 
        as pygame doesn't support rendering blackhole's field, and its too big for you to see
    """
    global particles, field
    
    
    particles = sorted(particles, key=lambda obj: obj.pos[2])
    for particle in particles:
        if field == 1:
            Z = 2 * np.sqrt(particle.r_s * (particle.r - particle.r_s))
            for i in range(len(Z)):
                opt_r = (particle.R[0][-i])/4e19
                pygame.draw.circle(WIN, (255-(5*i), (255-(20*i)), 10*i), ((particle.pos[0]), particle.pos[1]), particle.radius + opt_r)
            
            
            pygame.draw.circle(WIN, (20, 0, 20), ((particle.pos[0]), particle.pos[1]), particle.r_s//4e19)
            if particle.r_s//4e15 < particle.radius:
                pygame.draw.circle(WIN, particle.color, ((particle.pos[0]), particle.pos[1]), particle.radius)
        else:
            pygame.draw.circle(WIN, particle.color, ((particle.pos[0]), particle.pos[1]), particle.radius)

def update_win():
    """
    Description:
    Updates background, particles, and draw matter 
    
    """
    global particles
    WIN.fill((0, 0, 0))
    
    update_particles()
    draw_matters()
    
    
    

def runner(field_toggle=False):
    """
    Description:
    
    Main function that runs the simulation
    
    """
    global deltaTime, particles, field
    run = True
    clock = pygame.time.Clock()
    cd = 0
    
    if field_toggle:
        field = 1


    while run:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                break
        if keys[pygame.K_a]:
            deltaTime *= 1/2
            print(deltaTime)
        if keys[pygame.K_d]:  
            deltaTime *= 1.5
            print("DT: ", deltaTime)
        if keys[pygame.K_r]:  
            deltaTime = 1e-15
            particles = []
        if keys[pygame.K_t]:  
            init_particles(10)
            print("Num particles: ", len(particles))
        if keys[pygame.K_f]:
            if cd == 0:
                print("Field: ", field)
                field *= -1
                cd = 10
        
        
        update_win()
        clock.tick(FPS)
        if cd > 0:
            cd -= 1
        pygame.display.update()



if __name__ == '__main__':
    samples("stable_sun_orbit")
    runner()




