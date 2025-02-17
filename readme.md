Cat Scratching Detection System

Description

This system uses YOLO-based object detection to identify when a cat is scratching. When the system detects a cat scratching with a confidence level above 70%, it triggers a music therapy intervention and records a 5-second video.

Usage

Requirements: requirements.txt

Steps to Deploy:
	1.	Set up the environment:
            Install requirements; Ensure your device has a camera and a working sound system.
	2.	Download the weights and music files:
	        Download YOLO weights file (see https://github.com/zhong-kh/Cat-Scratch-Object-YOLO-Detection-Dataset)
	3.	Amend the paths in the code:
	        Update the path variables.
	4.	Run the script:
            Execute the Python script. Once started, the system will continuously detect if a cat is scratching, play music when detected, and record a 5-second video.
            To stop the system, press q.