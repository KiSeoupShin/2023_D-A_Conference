import subprocess

subprocess.run(["python", "inference_propainter.py", "--video", "inputs/object_removal/street_1/street_video.mp4", 
                "--mask", "inputs/object_removal/street_1_mask", "--resize_ratio", "0.5", "--fp16"])
