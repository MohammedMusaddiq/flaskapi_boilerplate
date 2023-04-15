from resources.users.users import UserApi, LoginApi, MeApi


def initialize_routes(api):
    api.add_resource(UserApi, '/users')
    api.add_resource(LoginApi, '/login')
    api.add_resource(MeApi, '/me')
