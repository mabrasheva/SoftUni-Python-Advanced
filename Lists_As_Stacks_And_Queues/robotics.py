"""
Each robot has a processing time – it is the time in seconds the robot needs to process a product.
When a robot is free, it should take a product for processing and log its name, product, and processing start time.
Each robot processes a product coming from the assembly line. A product is coming from the line each second (so the
first product should appear at [start time + 1 second]). If a product passes the line and there is not a free robot to take it, it should be queued at the end of the line again.
The robots are standing in the line in the order of their appearance.
Input
•	On the first line, you will receive the robots' names and their processing times in the format
"robotName-processTime;robotName-processTime;robotName-processTime..."
•	On the second line, you will get the starting time in the format "hh:mm:ss"
•	Next, until the "End" command, you will get a product on each line.
Output
•	Every time a robot takes a product, you should print: "{robotName} - {product} [hh:mm:ss]"
"""

from collections import deque


def time_string(time_in_seconds):
    hours = time_in_seconds // 3600
    minutes = (time_in_seconds % 3600) // 60
    seconds = (time_in_seconds % 3600) % 60
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


robots_list = input().split(";")
start_time = input()

robots = {}
for robot in robots_list:
    name, time = robot.split("-")
    robots[name] = {
        "needed_processing_time": int(time),
        "current_processing_time": 0,
        "processing_status": "Not processing"
    }

start_time = [int(i) for i in start_time.split(":")]
start_time_in_seconds = start_time[0] * 60 * 60 + start_time[1] * 60 + start_time[2]

products = deque()
while True:
    product = input()
    if product == "End":
        break
    products.append(product)

while products:
    start_time_in_seconds = (start_time_in_seconds + 1) % (24 * 60 * 60)
    product = products.popleft()
    for name, status in robots.items():
        if status["processing_status"] == "Not processing":
            print(f"{name} - {product} [{time_string(start_time_in_seconds)}]")
            status["processing_status"] = "Processing"
            break
    else:
        products.append(product)
    for name, status in robots.items():
        if status["processing_status"] == "Processing":
            status["current_processing_time"] += 1
        if status["needed_processing_time"] <= status["current_processing_time"]:
            status["current_processing_time"] = 0
            status["processing_status"] = "Not processing"
