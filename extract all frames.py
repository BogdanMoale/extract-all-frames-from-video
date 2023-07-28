import cv2
import os

def extract_frames(video_path, output_directory):
    # Open the video file
    video = cv2.VideoCapture(video_path)
    
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)
    
    # Initialize variables
    frame_count = 0
    success = True
    
    # Loop through the video frames
    while success:
        # Read the next frame
        success, frame = video.read()
        
        if success:
            # Save the frame as an image file
            frame_path = os.path.join(output_directory, f"frame{frame_count}.jpg")
            cv2.imwrite(frame_path, frame)
            
            # Increment the frame count
            frame_count += 1
    
    # Release the video file
    video.release()

# Example usage
video_path = input("Enter the path to your video file: ")

#output_directory = "C:\\Users\\Bogdan\\Desktop\\frames"
output_directory = input("Enter the path for output: ")
print("Proccesing. . .")
extract_frames(video_path, output_directory)
print("Done. The images were saved in: "+ output_directory)
print("Press enter key to close console")
input()
