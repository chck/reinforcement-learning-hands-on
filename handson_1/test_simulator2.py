#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gym
import argparse


def main(game, episode):
    """ write your code
    """
    ###
    ###
    ###


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This is test simulator by Open AI Gym')
    parser.add_argument("-g", "--game", type=str, help="chosen name of game", default="Alien-v0")
    parser.add_argument("-e", "--episode", type=int, help="episode count of game", default=10)

    args = parser.parse_args()
    main(args.game, args.episode)
