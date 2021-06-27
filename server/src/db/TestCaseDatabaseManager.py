from bson.objectid import ObjectId

from .DatabaseManager import DatabaseManager


class TestCaseDatabaseManager(DatabaseManager):
    def __init__(self) -> None:
        super().__init__()
        # Collections
        self.problems = self.db.problems


    def get_testcases(self, problem_id: str) -> dict:
        try:
            problem_id = ObjectId(problem_id)

            try:
                data = self.problems.find_one({'_id': problem_id}).get('test_cases')
                if data is not None:
                    data = {
                        'status': 'success',
                        'data': data
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

    def create_testcase(self, problem_id: str, testcase_data: dict) -> dict:
        try:
            problem_id = ObjectId(problem_id)

            try:
                data = self.problems.find_one({'_id': problem_id})['test_cases']
                data.append(testcase_data)
                data = self.problems.update({'_id': problem_id}, {'$set': {'test_cases': data}})
                if data is not None:
                    if data.get('n')==1:
                        data = self.problems.find_one({'_id': problem_id})['test_cases'][-1]
                        data = {
                            'status': 'success',
                            'data': data
                        }
                    else:
                        data = {
                            'status': 'failed',
                            'reason': 'Not Added!'
                        }
                else:
                    data = {
                        'status': 'failed',
                        'reason': 'No Problem found with this specific ID'
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
    

    def update_testcase(self, problem_id:str, testcase_data: dict) -> dict:
        try:
            problem_id = ObjectId(problem_id)

            try:
                data = self.problems.find_one({'_id': problem_id})['test_cases']
                ids = [d['_id'] for d in data]
                if testcase_data['_id'] in ids:
                    target_index = ids.index(testcase_data['_id'])
                    del data[target_index]
                    data.insert(target_index, testcase_data)
                    data = self.problems.update({'_id': problem_id}, {'$set': {'test_cases': data}})
                    if data is not None:
                        if data.get('n')==1:
                            data = self.problems.find_one({'_id': problem_id})['test_cases'][target_index]
                            data = {
                                'status': 'success',
                                'data': data
                            }
                        else:
                            data = {
                                'status': 'failed',
                                'reason': 'Not Updated!'
                            }
                    else:
                        data = {
                            'status': 'failed',
                            'reason': 'No Problem found with this specific ID'
                        }
                else:
                    data = {
                        'status': 'failed',
                        'reason': 'No TestCase found with this specific ID'
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


    def remove_testcase(self, problem_id: str, testcase_id: int) -> dict:
        try:
            problem_id = ObjectId(problem_id)

            try:
                data = self.problems.find_one({'_id': problem_id})['test_cases']
                ids = [d['_id'] for d in data]
                if testcase_id in ids:
                    target_index = ids.index(testcase_id)
                    del data[target_index]
                    data = self.problems.update({'_id': problem_id}, {'$set': {'test_cases': data}})
                    if data is not None:
                        data = {
                            'status': 'success',
                            'data': {}
                        }
                    else:
                        data = {
                            'status': 'failed',
                            'reason': 'No Problem found with this specific ID'
                        }
                else:
                    data = {
                        'status': 'failed',
                        'reason': 'No TestCase found with this specific ID'
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
