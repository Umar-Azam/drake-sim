# Author : Umar Azam
# Date   : 7th June 2023
# %%
# import numpy as np
# import matplotlib.pyplot as plt
# %%
# Testing plotting functionality with a simple parabola
# x = np.linspace(-5, 5, 1000)
# y = x**2
# plt.plot(x, y)

# %%
import numpy as np
import os
import time

import meshcat
import meshcat.geometry as g
from meshcat.animation import Animation
import meshcat.transformations as tf

# %%
vis = meshcat.Visualizer()

# %%
vis.url()

# %%


vis["box1"].set_object(g.Box([0.1, 0.2, 0.3]))


anim = Animation()

with anim.at_frame(vis, 0) as frame:
    # `frame` behaves like a Visualizer, in that we can
    # call `set_transform` and `set_property` on it, but
    # it just stores information inside the animation
    # rather than changing the current visualization
    frame["box1"].set_transform(tf.translation_matrix([0, 0, 0]))
with anim.at_frame(vis, 30) as frame:
    frame["box1"].set_transform(tf.translation_matrix([0, 1, 0]))
    
# `set_animation` actually sends the animation to the
# viewer. By default, the viewer will play the animation
# right away. To avoid that, you can also pass `play=false`. 
vis.set_animation(anim)



#%%

vis["/Cameras/default"].set_transform(tf.translation_matrix([0, 0, 1]))
# %%
anim = Animation()

with anim.at_frame(vis, 0) as frame:
    frame["/Cameras/default"].set_transform(tf.translation_matrix([0, 0, 0]))
with anim.at_frame(vis, 30) as frame:
    frame["/Cameras/default"].set_transform(tf.translation_matrix([0, 0, 1]))

# we can repeat the animation playback with the 
# repetitions argument:
vis.set_animation(anim, repetitions=2)


# %%

anim = Animation()

camera_path = "/Cameras/default/rotated/<object>"

with anim.at_frame(vis, 0) as frame:
    frame[camera_path].set_property("zoom", "number", 1)
with anim.at_frame(vis, 30) as frame:
    frame[camera_path].set_property("zoom", "number", 0.5)
with anim.at_frame(vis, 60) as frame:
    frame[camera_path].set_property("zoom", "number", 1)
    
# While we're animating the camera zoom, we can also animate any other
# properties we want. Let's simultaneously translate the box during 
# the same animation:
with anim.at_frame(vis, 0) as frame:
    frame["box1"].set_transform(tf.translation_matrix([0, -1, 0]))
with anim.at_frame(vis, 60) as frame:
    frame["box1"].set_transform(tf.translation_matrix([0, 1, 0]))

vis.set_animation(anim)














# %%

vis["sphere"].set_object(g.Sphere(0.1), 
                         g.MeshLambertMaterial(
                             color=0xff22dd,
                             reflectivity=0.8))

# %%

verts = np.random.random((3, 100000)).astype(np.float32)

vis.set_object(g.Points(
    g.PointsGeometry(verts, color=verts),
    g.PointsMaterial()
))
# %%
arr = np.linspace(-1,1,100000)
arr = arr +  0.1*np.random.random(arr.shape)
arr = np.array([arr, np.zeros(arr.shape), np.zeros(arr.shape)])
# %%
vis.set_object(g.Points(g.PointsGeometry(arr, color=np.ones(arr.shape)),g.PointsMaterial()))
# %%
vis.set_transform(tf.translation_matrix([0,0.0,0.3]))

# %%
arr = np.linspace(0,2*np.pi,1000)
points = np.array([ np.array([0.1*np.cos(t), 0.1*np.sin(t),0]) for t in arr]).T
# %%

# %%
vis.set_object(g.Points(g.PointsGeometry(points, color=np.ones(points.shape)),g.PointsMaterial()))
# %%
vis.set_transform(tf.translation_matrix([0,0.0,0.3]))

# %%
#%%

vis["robot"].set_object(g.Box([0.15, 0.35, 0.4]))

# %%
vis["robot"]["head"].set_object(g.Box([0.2, 0.2, 0.2]))
vis["robot"]["head"].set_transform(tf.translation_matrix([0, 0, 0.32]))

# %%

for x in np.linspace(0, np.pi, 100):
    vis["robot"].set_transform(tf.translation_matrix([np.sin(x), 0, 0]))
    time.sleep(0.01)

# %%

vis.delete()

# %%

for x in np.linspace(0, np.pi, 100):
    vis.set_transform(tf.translation_matrix([np.sin(x), 0, 0]))
    time.sleep(0.01)

# %%
vis.set_object(g.Sphere(0.1))
#vis.set_object(g.Box([0.2, 0.2, 0.2]))

for theta in np.linspace(0, 2 * np.pi, 200):
    vis.set_transform(tf.rotation_matrix(theta, [0, 0, 1]))
    time.sleep(0.005)

# %%
vis.delete()
vertices = np.random.random((3, 10)).astype(np.float32)
vis['lines_segments'].set_object(g.LineSegments(g.PointsGeometry(vertices)))


# %%
vis.delete()
vertices = np.array([[0.1,0.2,0.2,0.15],[0.1,0.2,0.2,0.3],[0.1,0.2,0.2,0.4]]).astype(np.float32)
vis['lines_segments'].set_object(g.LineSegments(g.PointsGeometry(vertices))),g.LineBasicMaterial({ 'color' : 0x0000ff } )
# %%
num_points = 20
radius = 0.1
tmp_arr = np.linspace(0,2*np.pi,2*num_points)
point3d = np.array([radius*np.cos(tmp_arr),radius*np.sin(tmp_arr),radius*np.zeros(tmp_arr.shape)])

# %%
tmp = np.zeros((point3d.shape[0],2*point3d.shape[1])) 
tmp[:,::2] = tmp[:,::2] + point3d
tmp[:,1::2] = tmp[:,1::2] + point3d

point3d = tmp[:,1:]
#%%

vis['lines_segments'].set_object(g.LineSegments(g.PointsGeometry(point3d)) )

#%%
for t in np.linspace(0,0.1,100):
    vis.set_transform(tf.translation_matrix([0,0,t]))
    time.sleep(0.01)

#%%
# %%
