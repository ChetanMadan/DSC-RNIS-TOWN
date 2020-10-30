#from carla.client import make_carla_client
import carla


actor_list = []

try:
    client = carla.Client("localhost",2000)
    client.set_timeout(2)
    world = client.get_world()
    print(client.get_available_maps())
    print(world)

finally:
    for actor in actor_list:
        actor.destroy()
    print("all actors destroyed!")
