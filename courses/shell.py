from rest_framework.renderers import JSONRenderer
from courses.models import Cource
from courses.serializers import CourceSerializer 
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


course = Cource.objects.latest('id')

serializer = CourceSerializer(course)

JSONRenderer().render(serializer.data)

user = User.objects.get(pk=1)
token = Token.objects.create(user=user)

token.key


