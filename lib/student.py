#!/usr/bin/env python

from user import User

class Student(User):

    def __init__(self, fn, ln):
        super().__init__(fn, ln)
        self.knowledge = []
    
    def learn(self, k):
        self.knowledge = self.knowledge + [k]