from deepface import DeepFace
import pandas as pd
import cv2
import matplotlib.pyplot as plt
import os
from matplotlib.pyplot import figure
import time

start = time.process_time() # Start tracking time of the code

# function load_images takes folder as input, and it finds all jpg,png,jpeg,svg images and returns list of dictionaries with image paths
def load_images(folder):
    counter = 0
    images = [] # list where we'll keep all  image dicts
    for img_path in os.listdir(folder): # locating all files inside provided folder
        if img_path.endswith(".jpg") or img_path.endswith(".png") or img_path.endswith(".jpeg") or img_path.endswith(".svg"): # finding all images in folder
            img = cv2.imread(f"{folder}{img_path}")
            img_dict = {"image_name" : img_path,
                        "image" : img} # saving image name and path in dict
            images.append(img_dict)
            counter += 1
            print(f"image {img_path} imported\n{counter} images imported")
        else:
            print("not image file")
    return images



# VGG Face Model
vgg_model_name = "VGG-Face" # choosing the model
vgg_model = DeepFace.build_model(vgg_model_name)


results_list = [] # storing results in this list
images = load_images(folder="your-imgs-folder/")

# function try_except_emotion tries to extract emotion result from model result, 0 if not found
def try_except_emotion(emotion,obj):
    try:
        emot = obj[0]["emotion"][emotion]
    except:
        emot = 0
    return emot


for img in images:
    player_name = img["image_name"]
    img_name = player_name.split(".")[0]
    obj = DeepFace.analyze(img_path=img['image'],actions=["age", "gender", "race", "emotion"],enforce_detection=False)
    print(f"VGG-Face has predicted that is {obj[0]['age']} and his dominant emotion is {obj[0]['dominant_emotion']}")
    figure(figsize=(14, 14))
    plt.imshow(img["image"][:,:,::-1]) # plotting image
    x = 0
    y = 0
    text = f"Img: {img_name} Dominant Emotion: {obj[0]['dominant_emotion']}"

    plt.text(x,y,text,bbox=dict(fill=False,edgecolor='red'),weight="bold",fontdict=dict(size=24))
    plt.savefig(f"{player_name}.jpg")
    plt.show()

    current_result = {
                      "player_name" : player_name,
                      #"image" : img["image"],
                      "dominant_emotion" : obj[0]["dominant_emotion"],
                      #"dominant_race" : obj["dominant_race"],
                      "age" : obj[0]["age"],
                      #"gender" : obj[0]["gender"],
                      "disgust" : try_except_emotion("disgust",obj),
                      "angry" : try_except_emotion("angry",obj),
                      "fear": try_except_emotion("fear",obj),
                      "happy" : try_except_emotion("happy",obj),
                      "sad" : try_except_emotion("sad",obj),
                      "surprise" : try_except_emotion("surprise",obj),
                      "neutral" : try_except_emotion("neutral",obj),}
    results_list.append(current_result)

results_df = pd.DataFrame(results_list)
print(time.process_time() - start)
