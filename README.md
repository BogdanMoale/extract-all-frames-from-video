# extract-all-frames-from-video
This Python script utilizes the OpenCV library to extract frames from a video and save them as individual image files. It prompts the user to input the path to the video file and the output directory where the frames will be saved. Here's a step-by-step explanation of the code:

1. Import the required libraries:
    import cv2
    import os
    
2. Define the function extract_frames that takes two arguments: video_path (the path to the video file) and output_directory (the directory where frames will be saved as images).

3. Open the video file using cv2.VideoCapture(video_path). The VideoCapture object is used to capture frames from the video.

4. Create the output directory if it doesn't exist using os.makedirs(output_directory, exist_ok=True).

5. Initialize variables: frame_count to keep track of the frame number and success to indicate whether reading the frame was successful.

6. Loop through the video frames using a while loop. The loop will continue until there are no more frames to read.

7. Read the next frame using success, frame = video.read(). The read() method returns a tuple containing a boolean value (success) indicating whether the frame was read successfully and the frame data itself (frame).

8. Check if the frame was read successfully (success is True). If so, save the frame as an image file using cv2.imwrite(frame_path, frame). The frame is saved as a JPEG image with the file name in the format "frameX.jpg", where X represents the frame number.

9. Increment the frame_count to keep track of the frame number.

10. After the loop ends (when there are no more frames to read), release the video file using video.release() to free up resources.

11. The script prompts the user to input the video file path and the output directory path.

12. Calls the extract_frames function with the provided video path and output directory.

13. Prints a message indicating that the processing is done and the location where the images were saved.

14. Waits for the user to press the Enter key to close the console.

Please note that you need to have OpenCV installed (cv2) and have the appropriate video codec libraries installed for this script to work correctly.