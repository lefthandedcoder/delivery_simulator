# Name: Christian Dye, WGU Student ID: 003130178
import truck
import datetime

print('Welcome to the WGUPS Delivery Simulator! Today is ' + str(datetime.date.today()))
print('\n')
truck1 = truck.get_truck1()
truck2 = truck.get_truck2()
truck3 = truck.get_truck3()

truck.load_trucks()
print('Trucks loaded!')
print('\n')
truck.get_route(truck1.package_list, truck1.route)
truck.get_shortest_path(truck1.route, truck1.optimized_route, 0)
truck.truck1.total_distance = truck.get_distance(truck1.optimized_route, truck1.distance_list)
truck.get_route(truck2.package_list, truck2.route)
truck.get_shortest_path(truck2.route, truck2.optimized_route, 0)
truck.truck2.total_distance = truck.get_distance(truck2.optimized_route, truck2.distance_list)
truck.get_route(truck3.package_list, truck3.route)
truck.get_shortest_path(truck3.route, truck3.optimized_route, 0)
truck.truck3.total_distance = truck.get_distance(truck3.optimized_route, truck3.distance_list)
print('Truck routes generated!')
print('Truck paths optimized!')
print('\n')
truck.get_delivered_list(truck1.distance_list, truck1.depart_time, truck1.package_list)
truck.get_delivered_list(truck2.distance_list, truck2.depart_time, truck2.package_list)
truck.get_delivered_list(truck3.distance_list, truck3.depart_time, truck3.package_list)
truck.get_status()
