#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 15:44:23 2025

@author: slava
"""

import numpy as np

def GenerateSwitchTimes(T, tt, mu, lambd):
    curr_state = np.where(pi0==1)[0][0]
    switch_times = {}
    switch_times[0] = curr_state
    curr_time = 0
    while(curr_time<T):
        if(0 == curr_state):
            wait =  np.random.exponential(1/mu)
        else:   
            wait =  np.random.exponential(1/lambd)
    
        curr_state = 1-curr_state
        curr_time = curr_time+wait
        switch_times[curr_time] = curr_state
            
    return switch_times


def GetSingleCompTrjectory(T, tt, mu, lambd):
    switch_times = GenerateSwitchTimes(T, tt, mu, lambd)
    mykeys = np.array(list(switch_times.keys()))
    times = np.linspace(0,T,tt)
    data = -1*np.ones(tt) 
    for i in range(tt):
        time = times[i]
        idd = np.searchsorted(mykeys, time, side='left') - 1
        data[i] = switch_times[mykeys[idd]]
    
    return data

            

n = 1      # num of components
T = 1000   # time  horyzon
tt = 500    # num of intervals in [0,T]
N = 1000   # num of simulations
pi0 = np.array([1,0]) # initial distribution

lambd = 1
mu = 2



ell = np.zeros((N,tt))
for j in range(N):    
    trj = np.zeros((n,tt))
    for i in range(n):
        trj[i,:] = GetSingleCompTrjectory(T, tt, mu, lambd)
    
    ell[j,:] = np.array(np.sum(trj,axis=0)>0, int)

r = np.mean(ell,0)

print(r)













