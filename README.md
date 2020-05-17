# Genetic Algorithm Snake

## Description

A visual illustration of a neural network being trained to play snake. 

## Purpose 

This project serves no function other than to explore interesting and complex ideas such as genetic algorithms, neural networks, and together in a form of neuroevolution on something simple like the arcade game snake. 

## Process 

With this project, building it was only half the fun. After getting the AI up and running, extensive testing was done to see how the mutation rate, population size, and what input the snake was given affected the snake's ability to learn. 

### Testing 



## Setup

This project is built within the Processing software, but written in Python. In order to run the project, install Processing [here](https://processing.org/download/). As far as I am aware, this project should work on any operating system with Processing installed.   

## Usage 

This project utilizes all of the default Processing functionality for running/stopping and so on.  
However, if you would like the data collected to be written out to a csv file, press `p` to have the program write out the weights of the best performing Neural Network and the best scores from each round. 

Additionally, if you choose to write out data from a previous run, changing the argument `singleSnakeMode` in the `GAsnake2.pyde`. This will cause the program to run only with a single snake with the best performing Neural Network from the previous run. This can be useful for debugging to see what strategies the snake has learned, and which ones it lacks. 

