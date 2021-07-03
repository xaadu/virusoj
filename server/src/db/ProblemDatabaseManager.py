from bson.objectid import ObjectId

from .DatabaseManager import DatabaseManager


class ProblemDatabaseManager(DatabaseManager):
    def __init__(self) -> None:
        super().__init__()
        # Collections
        self.problems = self.db.problems

        # Local Connection for not calling every request
        self.num_of_problem = self.problems.count_documents({})

    def problem_count(self) -> int:
        try:
            num_of_problem = self.problems.count_documents({})
            self.total_problem = num_of_problem
            return num_of_problem
        except Exception as e:
            print(e)
        return None

    def get_problem(self, problem_id: str) -> dict:
        try:
            problem_id = ObjectId(problem_id)

            try:
                problem = self.problems.find_one({'_id': problem_id})
                if problem is not None:
                    problem['_id'] = problem['_id'].__str__()
                    problem['test_cases']=[test_case for test_case in problem.get('test_cases') if test_case.get('sample')]

                    data = {
                        'status': 'success',
                        'data': problem
                    }
                else:
                    data = {
                        'status': 'failed',
                        'reason': 'No data found with this specific ID'
                    }
            except Exception as e:
                data = {
                    'status': 'failed',
                    'reason': str(e)
                }
        except Exception as e:
            data = {
                'status': 'falied',
                'reason': 'Invalid ID'
            }
        return data

    def get_problems(self, limit: int = 0, start: int = 0, user_email: str = None) -> dict:
        try:
            if user_email is None:
                problems = list(self.problems.find(
                                                    skip=start, 
                                                    limit=limit, 
                                                    projection=['title', 
                                                                'total_submission',
                                                                'accepted_submission',
                                                                'creator_email',
                                                    ]
                                                ))
            else:
                problems = list(self.problems.find({'creator_email': user_email},
                                                    skip=start, 
                                                    limit=limit, 
                                                    projection=['title', 
                                                                'total_submission',
                                                                'accepted_submission',
                                                                'creator_email',
                                                    ]
                                                ))

            for problem in problems:
                problem['_id'] = problem['_id'].__str__()
                
            if user_email is None:
                total_problem = self.num_of_problem
            else:
                total_problem = self.problems.count({'creator_email': user_email})

            metadata = {
                'total_problem': total_problem,
                'problem_returned': len(problems),
                'started_from': start
            }

            data = {
                'status': 'success',
                'data': problems,
                'metadata': metadata
            }
        except Exception as e:
            data = {
                'status': 'failed',
                'reason': str(e)
            }

        return data

    def create_problem(self, problem_data: dict) -> dict:
        try:
            data = self.problems.insert_one(problem_data)
            if data is not None:
                inserted_id = data.inserted_id
                data = self.problems.find_one({'_id': inserted_id})
                data['_id'] = data['_id'].__str__()
                data = {
                    'status': 'success',
                    'data': data
                }
                self.num_of_problem+=1
            else:
                data = {
                    'status': 'failed',
                    'reason': 'problem Could not be Created in Database!'
                }
        except Exception as e:
            data = {
                'status': 'failed',
                'reason': str(e)
            }
        return data
    

    def update_problem(self, problem_id:str, problem_data: dict) -> dict:
        try:
            problem_id = ObjectId(problem_id)

            try:
                data = self.problems.update({'_id': problem_id}, {'$set': problem_data})
                if data is not None:
                    if data.get('n')==1:
                        problem = self.problems.find_one({'_id': problem_id})
                        problem['_id'] = problem['_id'].__str__()
                        data = {
                            'status': 'success',
                            'data': problem
                        }
                    else:
                        data = {
                            'status': 'failed',
                            'reason': 'Not Updated!'
                        }
                else:
                    data = {
                        'status': 'failed',
                        'reason': 'No data found with this specific ID'
                    }
            except Exception as e:
                data = {
                    'status': 'failed',
                    'reason': str(e)
                }
        except Exception as e:
            data = {
                'status': 'falied',
                'reason': 'Invalid ID'
            }
        return data


    def remove_problem(self, problem_id: str) -> dict:
        try:
            problem_id = ObjectId(problem_id)
            try:
                data = self.problems.delete_one({'_id': problem_id})
                if data is not None:
                    if data.deleted_count == 1:
                        data = {
                            'status': 'success',
                            'data': {}
                        }
                        self.num_of_problem-=1
                    else:
                        data = {
                            'status': 'failed',
                            'reason': 'Might be wrong ID'
                        }
                else:
                    data = {
                        'status': 'failed',
                        'reason': 'Something Blew Up'
                    }
            except Exception as e:
                data = {
                    'status': 'failed',
                    'reason': str(e)
                }
        except Exception as e:
            data = {
                'status': 'falied',
                'reason': 'Invalid ID'
            }
        return data
