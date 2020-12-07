# annotator
Label and track C. elegans neurons.

## Installation

1. Clone git repository: 
  ```bash
  git clone https://github.com/venkatachalamlab/annotator.git
  ```  
  
2. Make sure that following Python libraries are installed (prefer conda over pip):
    - docopt
    - flask
    - gevent
    - numpy
    - scikit-image
    - opencv
    - h5py
    - pandas
    - dataclasses
    - av
    
3. Open a command line interface and nagivate to the annotator repository. Install (development mode):  
  ```bash
  (base) annotator> python setup.py develop
  ```


## Running annotator

1. Open a command-line interface as administrator (command prompt, anaconda prompt, terminal, etc.) and navigate to dataset folder. 


2. Enter the following command:  
`annotator --dataset=."` 
* Note: If installation is complete, you should get this message: `Starting a server on port 5000`

3. Open a web browser window and enter `http://localhost:5000/`.  
* Note: If image is not loaded but you got the server connection message, one common reason could be an incorrect dataset path.  
<p align="center">
  <img width="600" height="313" src="https://user-images.githubusercontent.com/31863323/84575872-73e39280-ad7e-11ea-8bd5-486091d5c54b.png">
</p>

## Working with annotator

Before annotating your dataset it's always good to do a hard reload, to do so open your browser's console, in Chrome the keyboard shortcut is ctrl+shift+J. Right click on the reload button and select Empty Cache and Hard Reload. You can close the console now. 

1. You can use the following hotkeys if you are focused on the image ( by clicking on it):  
```
f:           forward in time by 1 frmae
shift + f:   forward in time by 10 frames
d:           backwards in time by 1 frmae
shift + d:   backwards in time by 10 frames
v:           increase z by 0.05
shift + v    increase z by 0.20
ctrl + v     increase z by 0.01
c:           decrease z by 0.05
shift + c:   decrease z by 0.20
ctrl + c:    decrease z by 0.01
r:           next view (currently "slice", "mip", or "volume")
e:           previous view
o:           toggle fill circles
a:           toggle all / nearby annotations
0-9:         run selected macro
```

2. Use light blue scrollbars or your mouse to locate neurons. "slice" view is ideal for this purpose.  
<p align="center">
  <img width="600" height="398" src="https://user-images.githubusercontent.com/31863323/84576582-e0ad5b80-ad83-11ea-9713-c7f658f07c1c.png">
</p>

3. If neurons are not bright enough, use colored scrollbars to adjust lookup table.  
<p align="center">
  <img width="900" height="290" src="https://user-images.githubusercontent.com/31863323/84576821-7d242d80-ad85-11ea-86ec-9499f5c11047.png">
</p>

4. Use pink scrollbar or `f-d` hotkeys or `jump_to_frame` macro (explained later) to explore different time points.

## Annotating neurons

1. You can annotate a neuron by double clicking on its location or by using a macro (explained later).

2. When an annotation is selected, its information are shown in window "Annotation".  
<p align="center">
  <img width="600" height="350" src="https://user-images.githubusercontent.com/31863323/84582387-48ca6480-adb9-11ea-84da-a3e574f0c206.png">
</p>

3. Each neuron should have a unique track number through out the entire dataset. If you want to annotate another neuron, create a new track by clicking on `+` in "Tracks" window.  
* Note: New track is not automatically selected when created. To select a track uncheck-check it in "Tracks" window.

## Macros

Annotating a neuron at different time points, Creating and selecting a new track, Finding the best point to represent a neuron is easier if they are done by hotkeys. In "Annotation window" you can choose different macros and assign them to number keys.  
<p align="center">
  <img width="600" height="350" src="https://user-images.githubusercontent.com/31863323/84582630-88df1680-adbc-11ea-8a85-3ca309e11e66.png">
</p>

### useful macros

1. `insert_local_max`: Finds the closest maximum to the current location and labels it with the current track number. Its arguments specify the search area. You can have different keys for this macro with different arguments to use them for neurons of different size.  
* Note: When you click on different parts of the image, you can see their coordinates in "Annotation window". Choose a averag sized neuron and take advantage of this feature to get an idea about the dimentions of a neuron. Use this information to set parameters for this macro.

2. `jump_to_frame`: Jumps to the specified time point. When annotating multiple time points, it is useful to have a key for each time point.

3. `create_track`: Creates a new track and selects it. 


Example:  
In the above picture, the current track is 1. If I click on any part of the image and then press key '2', it jumps to t=12. I then click on the center of a neuron (roughly), by pressing "1", it automatically finds the brighest point close to wheren I clicked and labels it. Now I use key "3" to jump to t=185. Since the track number is not changed, if I find the same neuron and press "1", it labels it. Now pressing key "4" creates a new track and selects it so I can jump back to t=12 by pessing key '2' and find a new neuron to label.


## Saving and Loading

On the top right on "Annotation window" there are two buttons to save annotations and load them. Annotation are save in the dataset directory. 
