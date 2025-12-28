#!/usr/bin/env python3
"""
Return all students sorted by average score
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score
    
    Args:
        mongo_collection: pymongo collection object
    
    Returns:
        List of students with averageScore added, sorted by average
    """
    pipeline = [
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]
    
    return list(mongo_collection.aggregate(pipeline))
