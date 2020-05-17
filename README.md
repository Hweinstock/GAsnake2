# Genetic Algorithm Snake

## Description

A visual illustration of a neural network being trained to play snake. 

## Purpose 

This project serves no function other than to explore interesting and complex ideas such as genetic algorithms, neural networks, and together in a form of neuroevolution on something simple like the arcade game snake. 

## Process 

With this project, building it was only half the fun. After getting the AI up and running, extensive testing was done to see how the mutation rate, population size, and what input the snake was given affected the snake's ability to learn. 

### Testing 

The first test was extremely concerning since it revealed a large flaw or limit to how good the snake could get. Here is a graph illustrating the results:  

![Graph 1](examples/old_input.png?raw=true "Title")

The snake's learning mode failed to accurately consider its tail. The snake completely stopped learning since it was not being fed enough information about its tail. So once the snake reached a certain length, it had an essentially random chance to die on every turn. After adjusting this by giving the snake more information abouts its tail, the next test was much more promising:  

![Graph 2](examples/next_test.png?raw=true "Title")

In this test, the snake is still learning around generation 125, whereas in the previous model, it stopped learning around gen 50. This fluctuation clearly indicates the snakes capability to learn was not capped in the same way. While ideally we could have continued to run this test to the same length of the first, the average snake had become so proficient that each gen would take a considerable amount of time. The average snake had an average evaluation of close to 1500. Considering it only ran for half the generations and has already improved vastly beyond the previous, we called it a success. We ran more tests and found that it still eventually plateus, but not nearly as quickly, indicating another hurdle to be explored in the snake's learning model. 

## Setup

This project is built within the Processing software, but written in Python. In order to run the project, install Processing [here](https://processing.org/download/). As far as I am aware, this project should work on any operating system with Processing installed.   

## Usage 

This project utilizes all of the default Processing functionality for running/stopping and so on.  
However, if you would like the data collected to be written out to a csv file, press `p` to have the program write out the weights of the best performing Neural Network and the best scores from each round. 

Additionally, if you choose to write out data from a previous run, changing the argument `singleSnakeMode` in the `GAsnake2.pyde`. This will cause the program to run only with a single snake with the best performing Neural Network from the previous run. This can be useful for debugging to see what strategies the snake has learned, and which ones it lacks. 

