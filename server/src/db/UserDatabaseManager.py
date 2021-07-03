from bson.objectid import ObjectId

from .DatabaseManager import DatabaseManager


class UserDatabaseManager(DatabaseManager):
    def __init__(self) -> None:
        super().__init__()
        # Collections
        self.users = self.db.users

        # Local Connection for not calling every request
        self.num_of_user = self.users.count_documents({})

    def user_count(self) -> int:
        try:
            num_of_user = self.users.count_documents({})
            self.total_user = num_of_user
            return num_of_user
        except Exception as e:
            print(e)
        return None

    def get_user(self, user_id: str) -> dict:
        try:
            user_id = ObjectId(user_id)
            try:
                user = self.users.find_one({'_id': user_id})
                if user is not None:
                    user['_id'] = user['_id'].__str__()

                    data = {
                        'status': 'success',
                        'data': user
                    }
                else:
                    data = {
                        'status': 'failed',
                        'reason': 'No data found with this id'
                    }
            except Exception as e:
                data = {
                    'status': 'failed',
                    'reason': str(e)
                }
        except:
            data = {
                'status': 'failed',
                'reason': 'Invalid ID'
            }
        
        return data

    def get_users(self, limit: int = 0, start: int = 0) -> dict:
        try:
            users = list(self.users.find(
                skip=start,
                limit=limit,
                projection=['email',
                            'role',
                            'total_submission',
                            'accepted_submission',
                            ]
            ))

            for user in users:
                user['_id'] = user['_id'].__str__()

            total_user = self.num_of_user

            metadata = {
                'total_user': total_user,
                'user_returned': len(users),
                'started_from': start
            }

            data = {
                'status': 'success',
                'data': users,
                'metadata': metadata
            }
        except Exception as e:
            data = {
                'status': 'failed',
                'reason': str(e)
            }

        return data

    def create_user(self, user_data: dict) -> dict:
        try:
            data = self.users.insert_one(user_data)
            if data is not None:
                inserted_id = data.inserted_id
                data = self.users.find_one({'_id': inserted_id})
                data['_id'] = data['_id'].__str__()
                data = {
                    'status': 'success',
                    'data': data
                }
                self.num_of_user += 1
            else:
                data = {
                    'status': 'failed',
                    'reason': 'User Could not be Created in Database!'
                }
        except Exception as e:
            data = {
                'status': 'failed',
                'reason': str(e)
            }
        return data

    def update_user(self, user_id: str, user_data: dict) -> dict:
        try:
            user_id = ObjectId(user_id)

            try:
                data = self.users.update({'_id': user_id}, {'$set': user_data})
                if data is not None:
                    if data.get('n') == 1:
                        user = self.users.find_one({'_id': user_id})
                        user['_id'] = user['_id'].__str__()
                        data = {
                            'status': 'success',
                            'data': user
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

    def remove_user(self, user_id: str) -> dict:
        try:
            user_id = ObjectId(user_id)
            try:
                data = self.users.delete_one({'_id': user_id})
                if data is not None:
                    if data.deleted_count == 1:
                        data = {
                            'status': 'success',
                            'data': {}
                        }
                        self.num_of_user -= 1
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
