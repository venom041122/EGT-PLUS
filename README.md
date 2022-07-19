# EGT-PLUS

Problem:
● Hundreds of millions of people worldwide are affected by neurological disorders.
● According to the UN, there are around 40 million neurologically disabled children 
in India
● Children with neurological diseases suffer a massive loss in academics and can't 
learn new skills.

Solution:
● To solve the problem above problem we will make use of Eye Gaze Technology 
with an AR (Augmented Reality) - based keyboard extension.
● First, the user with a disability will have to just download the extension. This 
extension would be available in apps like Chrome, Email, Edge, etc wherever the 
keyboard will be required. 
● Access to a webcam would be needed. Then with the help of the Eye Gaze 
System pupil-centre/corneal would be detected using a webcam. 
● The computer will calculate the person’s gaze point, i.e., the coordinates of 
where he is looking on the screen based on the relative positions of the pupil 
centre and corneal reflection within the video image of the eye. 
● So by this, a person with a disability can give their input through a webcam and 
can easily communicate through this technology and would be able to learn new 
skills.
● Also In the future, AR-based sound generation can also be added to this 
Extention. Further, this extension has a lot of scopes to improve day by day with 
experiments and feedback.


This is a short & simple project of eye tracking and writing. It makes use of machine learning-based facial mapping (landmarks) with dlib + python + openCV, with eyes projection on a virtual keyboard. The algorithm works in real-time on the video-stream from the webcam.

Logic flow:

1. find face and track the right eye;
2. calibrate the proper range of allowed space for (comfortable) movement; 
(then, frame by frame)
3. track the right eye and project its centroid on a virtual keyboard in a "working window";
4. take inputs and, specifically, "press" the key, using blinking detection;
5. updtate a text string and print on screen (and, by just adding a couple of line, on a file).

