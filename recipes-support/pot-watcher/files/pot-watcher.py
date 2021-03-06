#!/usr/bin/python3

import os
import sys
import numpy as np
import ntpath
#import argparse
import skimage.io
import skimage.transform
import cv2
import time
import imutils
import pexpect
from imutils.video import VideoStream

import mvnc.mvncapi as mvnc

# Number of top prodictions to print
NUM_PREDICTIONS		= 2

# Variable to store commandline arguments
ARGS                = None

# ---- Step 1: Open the enumerated device and get a handle to it -------------

def open_ncs_device():

    # Look for enumerated NCS device(s); quit program if none found.
    devices = mvnc.EnumerateDevices()
    if len( devices ) == 0:
        print( "No devices found" )
        quit()

    # Get a handle to the first enumerated device and open it
    device = mvnc.Device( devices[0] )
    device.OpenDevice()

    return device

# ---- Step 2: Load a graph file onto the NCS device -------------------------

def load_graph( graph_filename, device ):

    # Read the graph file into a buffer
    with open( graph_filename, mode='rb' ) as f:
        blob = f.read()

    # Load the graph buffer into the NCS
    graph = device.AllocateGraph( blob )

    return graph

# ---- Step 3: Pre-process the images ----------------------------------------

def pre_process_image(img):
    scale = 1
    mean = [105.00, 110.00, 115.00]

    # Read & resize image [Image size is defined during training]
    #img = skimage.io.imread( ARGS.image )
    #img = skimage.transform.resize( img, ARGS.dim, preserve_range=True )

    # Convert RGB to BGR [skimage reads image in RGB, but Caffe uses BGR]
    #if( ARGS.colormode == "BGR" ):
    #    img = img[:, :, ::-1]

    # Mean subtraction & scaling [A common technique used to center the data]
    img = img.astype( np.float16 )
    img = ( img - np.float16( mean ) ) * scale

    #img = cv2.resize(img, (224, 224), cv2.INTER_LINEAR)
    #img = img.astype(np.float32)
    #img = np.divide(img, 255.0)

    return img

# ---- Step 4: Read & print inference results from the NCS -------------------

def infer_image( graph, img ):

    # Load the labels file 
    labels =[ line.rstrip('\n') for line in 
                   open( '/root/catagories.txt' ) if line != 'classes\n'] 

    # The first inference takes an additional ~20ms due to memory 
    # initializations, so we make a 'dummy forward pass'.
    graph.LoadTensor( img, 'user object' )
    output, userobj = graph.GetResult()

    # Load the image as a half-precision floating point array
    graph.LoadTensor( img, 'user object' )

    # Get the results from NCS
    output, userobj = graph.GetResult()

    # Sort the indices of top predictions
    order = output.argsort()[::-1][:NUM_PREDICTIONS]

    # Get execution time
    inference_time = graph.GetGraphOption( mvnc.GraphOption.TIME_TAKEN )

    # Print the results
    print( "\n==============================================================" )
    print( "Execution time: " + str( np.sum( inference_time ) ) + "ms" )
    print( "--------------------------------------------------------------" )
    for i in range( 0, NUM_PREDICTIONS ):
        print( "%3.1f%%\t" % (100.0 * output[ order[i] ] )
               + labels[ order[i] ] )
    print( "==============================================================" )

    # Make alert sound if we are boiling
    if labels[order[0]] == 'boiling' and output[order[0]] > 0.65:
        print('beedoo')
        pexpect.run("ssh 192.168.42.1 'aplay /root/beedoo.wav'", events={'(?i)password':'incendia\n'})


# ---- Step 5: Unload the graph and close the device -------------------------

def close_ncs_device( device, graph ):
    graph.DeallocateGraph()
    device.CloseDevice()

def get_image( video_device ):
    frame = video_device.read()
    frame = frame[:, :, ::-1]
    frame = imutils.resize(frame, width=224, height=224)

    #print(frame)
    return frame

def get_image_file( ):
    img = skimage.io.imread( '/root/img.jpg' )
    img = skimage.transform.resize( img, [224, 224], preserve_range=True )
    img = img[:, :, ::-1]

    #print(img)
    return img

def test( ):
    device = open_ncs_device()
    graph = load_graph( "/root/graph", device )
    img = get_image_file()
    img = pre_process_image(img)
    infer_image( graph, img )
    close_ncs_device( device, graph )


# ---- Main function (entry point for this script ) --------------------------

def main():

    # Uncomment to test with an image file
    if False:
        test()
        return

    device = open_ncs_device()
    graph = load_graph( "/root/graph", device )

    #video_device = VideoStream(src=0).start()
    video_device = VideoStream(resolution=(320, 240)).start()
    time.sleep(2.0)
    pexpect.run("ssh 192.168.42.1 'aplay /opt/AlexaPi/src/resources/beep.wav'", events={'(?i)password':'incendia\n'})

    while(True):
        img = get_image(video_device)
        #img = get_image_file()
        img = pre_process_image(img)
        infer_image( graph, img )
        time.sleep(0.5)

    video_device.stop()
    close_ncs_device( device, graph )

# ---- Define 'main' function as the entry point for this script -------------

if __name__ == '__main__':

#    parser = argparse.ArgumentParser(
#                         description="Image classifier using \
#                         Intel® Movidius™ Neural Compute Stick." )
#
#    parser.add_argument( '-g', '--graph', type=str,
#                         default='../../caffe/GoogLeNet/graph',
#                         help="Absolute path to the neural network graph file." )
#
#    parser.add_argument( '-i', '--image', type=str,
#                         default='../../data/images/cat.jpg',
#                         help="Absolute path to the image that needs to be inferred." )
#
#    parser.add_argument( '-l', '--labels', type=str,
#                         default='../../data/ilsvrc12/synset_words.txt',
#                         help="Absolute path to labels file." )
#
#    parser.add_argument( '-M', '--mean', type=float,
#                         nargs='+',
#                         default=[104.00698793, 116.66876762, 122.67891434],
#                         help="',' delimited floating point values for image mean." )
#
#    parser.add_argument( '-S', '--scale', type=float,
#                         default=1,
#                         help="Absolute path to labels file." )
#
#    parser.add_argument( '-D', '--dim', type=int,
#                         nargs='+',
#                         default=[224, 224],
#                         help="Image dimensions. ex. -D 224 224" )
#
#    parser.add_argument( '-c', '--colormode', type=str,
#                         default="BGR",
#                         help="RGB vs BGR color sequence. TensorFlow = RGB, Caffe = BGR" )
#
#
#    ARGS = parser.parse_args()
#
    main()

# ==== End of file ===========================================================
