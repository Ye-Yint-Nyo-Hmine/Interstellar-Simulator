
# ***Interstellar Simulator***
<p align="center">
    <a><img src="https://github.com/Ye-Yint-Nyo-Hmine/Interstellar-Simulator/blob/main/logos/logo.png?raw=true" alt="Logo" width="400" height="400" style="border-radius: 35px;"></a>
</p>


## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Demos](#demos)
4. [Dependencies](#dependencies)
5. [Usage](#usage)
   - [Running the Simulator](#running-the-simulator)
   - [Example Usage](#example-usage)
   - [Controls](#controls)
6. [Main Functions](#main-functions)
7. [Science](#science)
8. [License](#license)]
9. [Contribution](#contribution)

## Overview
Intersetellar Simulator is an intuitive and one of the first python 3D intersteller simulations. With immense capabilities such as simulating planets, blackholes, and more, while still being fast, Interstellar Simulator is a great tool for researchers. The foundations of Interstellar Simulator are also based in scientifical equations with minimum changes. In other words, it's insanely realistic

## Features
- [x] Realistic gravity simulation using Newtonian physics  
- [x] Black hole simulation with relativistic effects  
- [x] Predefined sample simulations for easy setup  
- [x] Simulate Realistic Blackholes using Schwarschild equations
- [x] Adjustable time scaling for fast or slow motion  
- [x] Particle generation with custom mass, velocity, and position  
- [x] Toggleable Einstein field rendering for gravitational depth visualization  
- [x] Interactive controls for real-time adjustments  
- [x] Scalable system supporting multiple celestial bodies  
- [x] Supports orbital mechanics and multi-body interactions  
- [x] Efficient computation using NumPy for performance optimization  
- [x] Visual rendering powered by Pygame  

## Demos

<p>
    <video width="320" height="240" controls>
        <source src="https://github.com/Ye-Yint-Nyo-Hmine/Interstellar-Simulator/blob/main/logos/Orbit.mp4?raw=true" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    

<video width="320" height="240" controls>
        <source src="https://github.com/Ye-Yint-Nyo-Hmine/Interstellar-Simulator/blob/main/logos/asteroids.mp4?raw=true" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    
<video width="320" height="240" controls>
        <source src="https://github.com/Ye-Yint-Nyo-Hmine/Interstellar-Simulator/blob/main/logos/sun_planets_moons.mp4?raw=true" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</p>



## Dependencies
This program requires the following Python libraries:
- `pygame` (for visualization)
- `numpy` (for numerical computations)

Install dependencies using:
```sh
pip install pygame numpy
```

## Usage
### Running the Simulator
To start a default simulation:
```sh
python example_simulation.py
```

### Example Usage
You can use the simulator in your own scripts. Example:
```python
from Interstellar.InterstellarSim import *

samples("stable_sun_orbit")
runner(field_toggle=True)
```

### Controls
- `A` - Decrease time step (slower simulation)
- `D` - Increase time step (faster simulation)
- `R` - Reset simulation
- `T` - Add more particles
- `F` - Toggle gravitational field rendering

## Main Functions
### `add_particle(x, y, z, mass, radius=None, vx=0, vy=0, vz=0, color=(255, 255, 255))`
Adds a new particle to the simulation. Allows setting mass, velocity, and optional Schwarzschild radius for black holes.

### `init_particles(num_particles=50, x_range=100, y_range=100, z_range=100, mass_range=[1e24, 5e24])`
Generates multiple particles randomly within specified ranges.

### `samples(sample_name)`
Loads predefined simulations:
- `stable_sun_orbit` – A sun with orbiting planets.
- `blackhole_with_earth` – A black hole interacting with Earth.
- `sun_with_100_planets` – A sun with 100 planets.
- `black_holes_2` – Two black holes colliding.
- `stellar_nursery` – A dense field of celestial bodies.

### `runner(field_toggle=False)`
Starts the simulation loop, with an option to toggle field rendering.

## Science
From various research papers, this program acculmulates all the neccessary elements such as the following for realistic simulation.

- Newton’s Law of Universal Gravitation for calculating gravitational forces.
- Schwarzschild Radius for defining event horizons of black holes.
- Relativistic Gravitational Potential for field depth visualization.

## License
This project is licensed under the MIT License.

## Contributions
Developed by **Ye Yint Hmine**.
Feel free to fork the repository and contribute improvements!

---
Enjoy simulating the universe! 🚀

