import sys
import ast

## Spot devices

from controller import Robot, Supervisor

# Create the robot instance
#robot = Robot()
robot = Supervisor()

# Get references to Spot's motors
# Front left leg
front_left_abduction_motor = robot.getDevice('front left shoulder abduction motor')
front_left_rotation_motor = robot.getDevice('front left shoulder rotation motor')
front_left_elbow_motor = robot.getDevice('front left elbow motor')

# Front right leg
front_right_abduction_motor = robot.getDevice('front right shoulder abduction motor')
front_right_rotation_motor = robot.getDevice('front right shoulder rotation motor')
front_right_elbow_motor = robot.getDevice('front right elbow motor')

# Rear left leg
rear_left_abduction_motor = robot.getDevice('rear left shoulder abduction motor')
rear_left_rotation_motor = robot.getDevice('rear left shoulder rotation motor')
rear_left_elbow_motor = robot.getDevice('rear left elbow motor')

# Rear right leg
rear_right_abduction_motor = robot.getDevice('rear right shoulder abduction motor')
rear_right_rotation_motor = robot.getDevice('rear right shoulder rotation motor')
rear_right_elbow_motor = robot.getDevice('rear right elbow motor')

## Walking

def iterate_gene_move(gene):
    for m in gene:
        front_left_abduction_motor .setPosition(m[0])
        front_left_rotation_motor  .setPosition(m[1])
        front_left_elbow_motor     .setPosition(m[2])
        front_right_abduction_motor.setPosition(m[3])
        front_right_rotation_motor .setPosition(m[4])
        front_right_elbow_motor    .setPosition(m[5])
        rear_left_abduction_motor  .setPosition(m[6])
        rear_left_rotation_motor   .setPosition(m[7])
        rear_left_elbow_motor      .setPosition(m[8])
        rear_right_abduction_motor .setPosition(m[9])
        rear_right_rotation_motor  .setPosition(m[10])
        rear_right_elbow_motor     .setPosition(m[11])
        robot.step(64)

## Genetic algorithm
# I know that a more proper name would be "chromosome" or whatever. I will
# change that later.

IND_N = 10
GEN_N = 100

import math
import random
from functools import partial

gen_rand = lambda : random.random() * 0.8 - 0.4
def get_random_gene():
    return [[gen_rand() for _ in range(12)] for _ in range(12)]


calc_dist = lambda init_pos, end_pos : math.sqrt(math.pow(end_pos[0] - init_pos[0], 2) + math.pow(end_pos[1] - init_pos[1], 2))

# Computes how good the solution is
# For now, let's only use the distance from the beginning
def fitness(gene):

    # Reset position
    robot.getSelf().getField('translation').setSFVec3f([0, 0, 0.7])
    robot.getSelf().getField('rotation').setSFRotation([0, 0, 1, 0])
    robot.getSelf().resetPhysics()

    init_pos = robot.getSelf().getPosition()

    acc_distance = 0

    for _ in range(100):
        iterate_gene_move(gene)
        curr_pos = robot.getSelf().getPosition()
        acc_distance += calc_dist(init_pos, curr_pos)

    end_pos = robot.getSelf().getPosition()

    # The fitness function will be (distance, height)
    # and we want to penalize for both

    dist = calc_dist(init_pos, end_pos)
    print('dist: {:.3f}, acc {:.3f} height: {:.3f} = '.format(dist, acc_distance, end_pos[2]), end='')

    #return (dist, end_pos[2])
    # dist + 
    score = acc_distance * end_pos[2]
    print (score)
    return score

import copy

def offspring(best, _individual):
    #print('----')
    #print(len(best))
    #print(best)
    #print('----')
    #print(len(individual))
    #print(individual)
    #print('----')

    individual = copy.deepcopy(_individual)
    for i, _list in enumerate(best):
        for j, _val in enumerate(_list):
            individual[i][j] = ((_val + individual[i][j]) / 2) + 0.5 * (- 0.0025 + random.random() * 0.005)

    return individual

def next_generation(gene_pool):
    best = gene_pool[0]
    offspring_p = partial(offspring, best)

    # Now, have children with everyone, except the worst who'll be replaced
    gene_pool[1:-1] = list(map(offspring_p, gene_pool[1:-1]))
    gene_pool[-1] = get_random_gene()

    return gene_pool

def evolve():
    init = True
    gene_pool = []

    if init:
        for _ in range(IND_N):
            gene = get_random_gene()
            gene_pool.append(gene)
        init = False

    for g in range(GEN_N):
        print('generation ' + str(g))
        #print(gene_pool)
        _fitness = list(map(fitness, gene_pool))
        gene_fitness = list(zip(gene_pool, _fitness))

        # Select the best
        gene_fitness.sort(key=lambda x: x[1], reverse=True)
        #best = gene_fitness[0]
        #print('Best: {}'.format(best))
        #print(gene_pool)
        #print('-------------------------------')
        gene_pool = list(list(zip(*gene_fitness))[0])
        #print(gene_pool)
        gene_pool = next_generation(gene_pool)

evolve()
print('Bye!')

