from camera import operate_camera
from multiprocessing import Process

if __name__ == '__main__':
    print("How many cameras do you have?")
    n = int(input());
    cam_processes = []
    for i in range(0, n):
        cam_processes.append(Process(target=operate_camera, args=(i,)))
    
    for process in cam_processes:
        process.start()

    for process in cam_processes:
        process.join()