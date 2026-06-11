import math

def main():
    #list of all names
    can_names=["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303"]
    can_radiuses=[6.0, 6.83, 7.62, 8.1, 10.32, 10.79, 11.91, 12.06, 13.02, 14.29, 15.72, 16.51]
    can_heights=[10.0, 11.91, 11.91, 11.91, 17.78, 19.05, 25.4, 25.4, 27.94, 30.48, 33.02, 33.02]
    can_cost_per_can=[0.28, 0.43, 0.45, 0.56, 0.68, 0.72, 0.86, 0.91, 1.01, 1.14, 1.25, 1.47]
    best_store = None
    best_cost = None
    max_store_eff = -1
    max_cost_eff = -1 
    for i in range(len(can_names)):
        name=can_names[i]
        radius=can_radiuses[i]
        height=can_heights[i]
        cost=can_cost_per_can[i]
        storage_efficiency=can_efficiency(radius, height)
        cost_effeiciency=can_efficiency( radius, height, cost)

        print(f"{name} {storage_efficiency:.2f} {cost_effeiciency:.0f}")
        
        
          

        if storage_efficiency > max_store_eff:
                max_store_eff=storage_efficiency
                best_store=name
        if cost_effeiciency > max_cost_eff:
                max_cost_eff=cost_effeiciency
                best_cost=name
        print(f"the best storage efficiency is {best_store} with {max_store_eff:.2f}")
        print(f"the best cost efficiency is {best_cost} with {max_cost_eff:.2f}")

    
  
def can_efficiency(name,radius, height, cost_per_can):
    volume=can_vol(radius, height)
    area=can_area(radius, height)
    storage_efficiency=volume/area
    print(f"{name}: volume:{volume:.2f} area:{area:.2f} storage efficiency:{storage_efficiency:.2f} cost per can:{cost_per_can:.2f}")
    return storage_efficiency
def can_vol(radius, height):
    volume=math.pi*radius**2*height
    return volume 
def can_area(radius, height):
    area=2*math.pi*radius*(radius+height)
    return area 
main()    