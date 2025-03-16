

def calculate_gravity(particles):
    """
    :param particles: the list of particles
    
    Description:
    
    It calculates gravity, check for black hole consumption and collision
    """
    
    import numpy as np
    from stellar.universal_constants import G
    positions = np.array([p.pos for p in particles])  # Shape (len(particles), 3)
    masses = np.array([p.mass for p in particles])  # Shape (len(particles),)
    forces = np.zeros_like(positions)  # Initialize forces array (same shape as positions)
    radii = np.array([p.radius for p in particles]) # Shape (len(particles),)
    scharwzschild_radii = np.array([p.r_s/4e19 for p in particles]) # Shape (len(particles),) *Note: 4e19 to scale for rendering purposes
    classifications = np.array([p.classi for p in particles])


    for i in range(len(particles)):
        delta_pos = positions - positions[i]  # Shape (NUM_PARTICLES, 2)
        dist_sq = np.sum(delta_pos**2, axis=1)  # Squared distances (shape (NUM_PARTICLES,))
        dist = np.sqrt(dist_sq)
        
        
        black_hole_consumption = dist < (scharwzschild_radii + scharwzschild_radii[i])
        for j in np.where(black_hole_consumption)[0]:
            if i != j:
                try:
                    # Identify the particle with the larger mass
                    if particles[i].mass > particles[j].mass:
                        particles[i].mass += particles[j].mass  # Add mass to the larger particle
                        particles[j].mass = 1e-10
                        particles[j].radius *= 1/particles[i].radius  # Remove the smaller particle
                        
                        break
                    else:
                        particles[j].mass += particles[i].mass  # Add mass to the larger particle
                        particles[i].mass = 1e-10
                        particles[i].radius *= 1/particles[j].radius  # Remove the smaller particle
                        
                        break
                except:
                    continue
        
        
        if classifications[i] != "Blackhole":
            collided = dist <= radii + radii[i]
            for j in np.where(collided)[0]:
                if i != j:
                    # Impulse collision: m1v1 + m2v2 = m1vf + m2vf
                    try:
                        v_f = ((particles[i].mass*particles[i].vel) + (particles[j].mass*particles[j].vel))// (particles[i].mass + particles[j].mass)
                        particles[i].vel, particles[j].vel = v_f, -v_f
                        if particles[i].mass > particles[j].mass:
                            particles[i].mass += particles[j].mass  # Add mass to the larger particle
                            particles[j].mass = 1e-10
                            particles[j].radius *= 1/particles[i].radius  # Remove the smaller particle
                            
                            break
                        else:
                            particles[j].mass += particles[i].mass  # Add mass to the larger particle
                            particles[i].mass = 1e-10
                            particles[i].radius *= 1/particles[j].radius  # Remove the smaller particle
                            
                            break
                    except:
                        continue

        # Gravitational force magnitude (ensure no division by zero or NaNs)
        force_magnitude = (G * masses[i] * masses) / dist_sq

        # safe conditioning
        force_magnitude = np.nan_to_num(force_magnitude, nan=0.0)
        
        force_direction = delta_pos  # Normalize delta_pos to get direction vectors
        forces[i] = np.sum(force_magnitude[:, np.newaxis] * force_direction, axis=0)

    return forces

    