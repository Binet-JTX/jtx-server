from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, _user_has_module_perms, _user_has_perm

from rest_framework import viewsets, serializers, decorators, exceptions, permissions
from rest_framework.response import Response


class UserManager(BaseUserManager):
    def get_queryset(self):
        return super(UserManager, self).get_queryset()

    def create_user(self, email, password):
        """Create and save a User with the given email and password"""
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """Create and save a User with the given email and password, and give it full privileges"""
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    class Meta:
        app_label = 'jtx_core'
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=128, blank=True)
    last_name = models.CharField(max_length=128, blank=True)
    pseudo = models.CharField(max_length=128, blank=True)
    promotion = models.CharField(max_length=100, blank=True)
    duty = models.CharField(max_length=254, blank=True)

    is_active = models.BooleanField(default=True)
    last_modified = models.DateTimeField(auto_now=True)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def has_perm(self, perm, obj=None):
        if self.is_active and self.is_superuser:
            return True

        return _user_has_perm(self, perm, obj)

    def has_perms(self, perm_list, obj=None):
        for perm in perm_list:
            if not self.has_perm(perm, obj):
                return False
        return True

    def has_module_perms(self, app_label):
        if self.is_active and self.is_superuser:
            return True

        return _user_has_module_perms(self, app_label)

    def get_short_name(self):
        if not self.pseudo:
            return self.first_name

        return self.pseudo

    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ('is_active', 'last_login', 'last_modified')
        write_only_fields = ('password',)
        exclude = ('is_staff', 'is_superuser')
        extra_kwargs = {'password':{'required':False}}

    def create(self, data):
        u = super(UserSerializer, self).create(data)
        u.set_password(data.get('password', '0000'))
        u.save()
        return u



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @decorators.list_route()
    def me(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)

    @decorators.list_route(methods=['put'])
    def change_password(self, request):
        user = request.user

        data = request.data
        if not user.check_password(data['old_password']):
            raise exceptions.PermissionDenied()

        user.set_password(data['password'])
        user.save()
        return Response('Password changed', 200)
