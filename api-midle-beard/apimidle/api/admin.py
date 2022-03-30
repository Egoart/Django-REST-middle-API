from django.contrib import admin
from api.models import (
                        User, 
                        Address, 
                        Company, 
                        Geo, 
                        Todos, 
                        Photo,
                        Album,
                        Post,
                        Comment)


admin.site.register(User)

admin.site.register(Address)

admin.site.register(Company)

admin.site.register(Geo)

admin.site.register(Todos)

admin.site.register(Photo)

admin.site.register(Album)

admin.site.register(Post)

admin.site.register(Comment)