import json
import time
delta = 0.0



while(True):
    delta += 1
    with open("coords.json", "r") as a_file:
        json_object = json.load(a_file)
        a_file.close()

    json_object["x"] = delta
    with open("coords.json", "x") as a_file:
        json.dump(json_object, a_file)
        a_file.close()
    time.sleep(1);
    print(delta)