from time import sleep

def check_divisions(segment):
    counter = 0

    while (segment / 2) >= 1:
        segment /= 2
        counter += 1
        sleep(0.01)

    return counter
