#!/usr/bin/env python3
""" The Top students """


def top_students(mongo_collection):
    """
    returns all students sorted by average score
    params: mongo_collection: collection object
    return: List of students with their average scores in descending order
    """
    student = [
        {
            "$unwind": "$topics"
        },
        {
            "$group": {
                "_id": "$_id",
                "name": {"$first": "$name"},
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        },
        {
            "$project": {
                "_id": 1,
                "name": 1,
                "averageScore": 1
            }
        }

    ]

    result = list(mongo_collection.aggregate(student))

    return result
