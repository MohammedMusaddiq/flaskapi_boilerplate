from resources.extensions import ma


class UserSchema(ma.Schema):
    id = ma.String()

    class Meta:
        fields = ("id", "email")
