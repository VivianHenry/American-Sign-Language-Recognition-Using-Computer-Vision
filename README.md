<h1>American Sign Language Recognition Using Computer Vision</h1>

<h2>Introduction</h2>

This is a Python program to interpret American Sign Language gestures, in real time, thereby facilitating communication between sign language and non-sign language conversationalists. This implementation overlays several landmarks upon the users’ hand and tracks the absolute and relative positions of these landmarks to recognize gestures. The input to the system is a live camera feed. The system consists of four subprograms:

<ul>
  <li>The creation of a hand tracking module.</li>
  <li>The interpretation of ASL numbers.</li>
  <li>The interpretation of ASL letters.</li>
  <li>The formation of words using the fingerspelling method.</li>
</ul>

Since this implementation works on static frames, a drawback and potential area of improvement is the lack of accommodation for gestures with associated motion such as for letters ‘J’ and ‘Z’.

<img alt="image" src="https://github.com/VivianHenry/American-Sign-Language-Recognition-Using-Computer-Vision/assets/67223688/d292d803-93c4-4806-ba5c-eb0c5e7deb6a">

<h2>Methodology</h2>

Since the backbone of this approach is the hand tracking and landmark placement, the first task would be to implement an accurate hand tracking module that provides these landmarks and their positions in the frame. In order to implement the hand tracking module, I used MediaPipe. MediaPipe is a multi-modal, cross-platform library developed by Google that provides various ready-to-use machine learning solutions, intended for computer vision tasks. MediaPipe Hands, provided by MediaPipe, is a high-fidelity hand tracking solution that employs machine learning to infer 21 3-D landmarks from just a single frame. What makes this solution work well is the fact that it utilizes a ML pipeline consisting of multiple models working concurrently. Initially, a palm detection model is executed over the whole image since palms are significantly simpler to detect in comparison to hands with articulated fingers. Palms are also smaller objects, thereby allowing the non-maximum suppression algorithm to work well even when there are multiple palms in the frame, participating in occlusion cases. Additionally, palms can be modeled using square bounding boxes (anchors). Using these techniques, an average precision of 95.7% is obtained. Once the palm is detected, the subsequent hand landmark model performs precise key-point localization of 21 3-D hand-knuckle coordinates within the detected hand regions using regression.

Another library that I will be using for this project is OpenCV. OpenCV, originally developed by Intel, is a library of programming functions designed for image processing and real-time computer vision tasks. It is an open-sourced, cross-platform library written in C/C++. OpenCV-Python is a Python wrapper for the original OpenCV C++ implementation that makes use of Numpy. Numpy is a highly optimized library for numerical operations with a MATLAB-style syntax. All the OpenCV array structures are converted to and from Numpy arrays. 

<h2>Results</h2>

<img width="262" src="https://github.com/VivianHenry/American-Sign-Language-Recognition-Using-Computer-Vision/assets/67223688/76a87a4c-7720-401c-a7f9-5c4efaf24f87">

<img width="265" src="https://github.com/VivianHenry/American-Sign-Language-Recognition-Using-Computer-Vision/assets/67223688/8140243a-a2ab-4564-a0a1-ce4e7f871ef0">

<img width="263" src="https://github.com/VivianHenry/American-Sign-Language-Recognition-Using-Computer-Vision/assets/67223688/421c07ab-a108-492a-bb8e-1f2422f34adb">

<img width="263" src="https://github.com/VivianHenry/American-Sign-Language-Recognition-Using-Computer-Vision/assets/67223688/cdb0e184-2e25-4cdf-845f-b863176058d2">

<img width="263" src="https://github.com/VivianHenry/American-Sign-Language-Recognition-Using-Computer-Vision/assets/67223688/8c3d2d8f-1c69-4b6d-bff9-37c016643c3f">

<img width="263" src="https://github.com/VivianHenry/American-Sign-Language-Recognition-Using-Computer-Vision/assets/67223688/66298def-9c73-4b21-a750-ce8eedbdb151">

<img width="800" src="https://github.com/VivianHenry/American-Sign-Language-Recognition-Using-Computer-Vision/assets/67223688/0321ea68-b4d0-44ac-a38a-3fdd8ccfc674">

<img width="800" src="https://github.com/VivianHenry/American-Sign-Language-Recognition-Using-Computer-Vision/assets/67223688/79482116-6230-4f2a-9ee1-30125d9492c7">

<h2>Conclusion</h2>

As seen above, the system is working as intended. The prevalent benefit of this approach, in my opinion, is the lack of training dataset collection and model creation. Since this model is solely dependent on the relative position of the hand and fingers, a characteristic that is fixed by the internationally adopted ASL guidelines, it can be ascertained that this model will not inculcate additional, possibly erroneous, features which is a possibility with artificial neural networks. 

While the implementation was largely successful, there arose a few challenges that inhibited a perfect implementation. Firstly, letters ‘J’ and ‘Z’ have motions associated with them and since the system is designed to interpret static frames, these letters could not be recognized. ‘Z’ has an approximate relative frequency of just about 0.078% in the English language and ‘J’ has an approximate relative frequency of 0.16%. While the effect of not having ‘Z’ is minimal, an elementary solution for ‘J’ was required. For this purpose, an imprecise version of the standard for ‘J’ was implemented that worked with limited accuracy. Secondly, due to conflicts in the number and alphabet gestures, the recognition systems for these had to be alienated from each other. Thirdly, while words were successfully formed, the formation of complete sentences, and by extension paragraphs, is checked due to the lack of gestures for common punctuations such as ‘.’, ‘!’, ‘?’, etc. Finally, while the bare recognition of number and letter gestures are completed in almost instant time, a deliberate delay had to be induced in the word formation subprogram. This delay had to be induced to allow users time to switch between gestures, without the system interpreting transitional gestures as intended gestures.
