enemies = 1

def increase_enemy():
    global enemies
    enemies += 2
    print(f"Enemies inside the function = {enemies}")
          
increase_enemy()
print(f"Enemies outside the function = {enemies}")