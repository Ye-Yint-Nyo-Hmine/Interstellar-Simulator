class Particle:
    def __init__(self, x, y, z, mass, rad=None, vx=0, vy=0, vz=0, color=(255, 255, 255)):
        """
        :param x, y, z: scalar 3D positions
        :param mass: scalar mass 
        :param rad: radius of the particle, used to be defined when creating blackhole #! Do not define this for other particles except blackhole
        :param vx, vy, vz: scalar initial 3d velocities
        :param color: color for particle to be rendered
        
        Description:
        
        Create a scientifically accurate particle
        
        """
        from stellar.universal_constants import G, c
        import numpy as np
        
        self.pos = np.array([x, y, z], dtype=float)
        self.mass = mass
        self.vel = np.array([vx, vy, vz], dtype=float)
        self.r_s = (2 * G * self.mass) / c**2
        self.color = color
        if self.mass >= 1e42:
            self.classi = "Blackhole"
        else:
            self.classi = "particle"
        
        if rad != None: # radius definition, used for blackholes
            self.radius = rad
        else:
            self.radius = (((self.mass / 1e13)** (2/6)) // 50000 ) + 1
            
        self.r = np.linspace(self.r_s * 1.05, 10 * self.r_s, 10)  # Radial distance
        self.theta = np.linspace(0, 2 * np.pi, 10)
        self.R, self.THETA = np.meshgrid(self.r, self.theta)
        
    def update(self, dt):
        self.pos += self.vel * dt
        