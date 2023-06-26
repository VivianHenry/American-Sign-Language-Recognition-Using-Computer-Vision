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

<img width=800 alt=image src="https://github.com/VivianHenry/American-Sign-Language-Recognition-Using-Computer-Vision/assets/67223688/d292d803-93c4-4806-ba5c-eb0c5e7deb6a">


