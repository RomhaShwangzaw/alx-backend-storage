#!/usr/bin/env python3
"""Sort by score module"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score

    Arg:
        mongo_collection: a pymongo collection object

    Return:
        a list of students sorted by average score
    """
    students = list(mongo_collection.find())
    for student in students:
        totalScore = 0
        count = 0
        for topic in student.get('topics'):
            totalScore += topic.get('score')
            count += 1
        averageScore = totalScore / count
        mongo_collection.update_one(
                {'name': student.get('name')},
                {'$set': {'averageScore': averageScore}})

    newStudents = list(mongo_collection.find()
                       .sort('averageScore', -1))
    return list(newStudents)
