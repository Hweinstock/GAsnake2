# Genetic Algorithm Snake

## Description

A visual illustration of a neural network being trained to play snake. 

## Purpose 

This project serves no function other than to explore interesting and complex ideas such as genetic algorithms, neural networks, and together in a form of neuroevolution on something simple like the arcade game snake. 

## Setup

This project is built within the Processing software, but written in Python. In order to run the project, install Processing [here](https://processing.org/download/). As far as I am aware, this project should work on any operating system with Processing installed.   

## Process of Making

With this project, building it was only half the fun. After getting the AI up and running, extensive testing was done to see how the mutation rate, population size, and what input the snake was given affected the snake's ability to learn. 

### The Neural Network 

Because the main purpose of this was to learn, I did not use any library to handle the neural networks for me. Instead, I created a simple file that allowed for 3 layer networks (1 hidden) in `nn.py`. Also, at the time, I didn't know any linear algebra so I wrote `matrices.py` to handle all of that for me while learning about matrix operations and how they work.  

The final Neural Network used in testing had the following structure,  
##### 4 input neurons:  
**left:** A boolean value(1 or 0) describing if there was a wall or tail directly to the left of the head of the snake.  
**right:** A boolean value(1 or 0) describing if there was a wall or tail directly to the right of the head of the snake.  
**straight:** A boolean value(1 or 0) describing if there was a wall or tail directly ahead of the head of the snake.  
**fv(food vector):** The relative turn angle to the food from the head.  

##### 6 hidden neurons. 
We tried making this number very high, but it slowed down the tests, so we kept to low to allow for quicker run-time. This could be another value that would be interesting to experiment with.  

##### 3 output neurons
By the rules of snake, you can continue straight, turn left or turn right. 

### Testing 

The snake was evaluated on a score system invented to better help its learning. Rather than evaluating the score as only food, it represents the overall performance of the snake by considering how quickly it got to food, how much time it 'wasted', and if it every made a blatantly incorrect decision, such as turning away from the food right before getting it.  

Looking at one of the first tests, the results were extremely concerning since it revealed a large flaw or limit to how good the snake could get. Here is a graph illustrating the results:  

![Graph 1](examples/old_input.png?raw=true "Title")

The snake's learning model failed to accurately consider its tail. The snake completely stopped learning since it was not being fed enough information about its tail. So once the snake reached a certain length, it had an essentially random chance to die on every turn. After adjusting this by giving the snake more information abouts its tail, the next test was much more promising:  

![Graph 2](examples/next_test.png?raw=true "Title")

In this test, the snake is still learning around generation 125, whereas in the previous model, it stopped learning around gen 50. This fluctuation clearly indicates the snakes capability to learn was not capped in the same way. While ideally we could have continued to run this test to the same length of the first, the average snake had become so proficient that each gen would take an unrealistic amount of time. The average snake had an average evaluation of close to 1500. Considering it only ran for half the generations and has already improved vastly beyond the previous, we called it a success. We ran more tests and found that it still eventually plateus, but not nearly as quickly, indicating another hurdle to be explored in the snake's learning model. 

## Usage 

This project utilizes all of the default Processing functionality for running/stopping and so on.  
However, if you would like the data collected to be written out to a csv file, press `p` to have the program write out the weights of the best performing Neural Network and the best scores from each round. 

Additionally, if you choose to write out data from a previous run, changing the argument `singleSnakeMode` in the `GAsnake2.pyde`. This will cause the program to run only with a single snake with the best performing Neural Network from the previous run. This can be useful for debugging to see what strategies the snake has learned, and which ones it lacks. 

