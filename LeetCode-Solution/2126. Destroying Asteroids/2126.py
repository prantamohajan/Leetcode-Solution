class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        asteroids.sort()
        max_asteroid = asteroids[-1] 
        
        currentMass = mass
        for asteroidMass in asteroids:
            if currentMass >= asteroidMass:
                currentMass += asteroidMass
            else:
                return False
            if currentMass >= max_asteroid:
                return True
        
        return True