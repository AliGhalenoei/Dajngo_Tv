from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Comment)
admin.site.register(SaveMovie)
admin.site.register(LikeMovie)

@ admin.register(UploadPartSeryal)
class SelectPartSeryalAdmin(admin.ModelAdmin):
    list_display =('seyal' , 'num_part')

admin.site.register(SeryalMovie)
admin.site.register(CommentSeryal)
admin.site.register(SaveSeryal)
admin.site.register(LikeSeryal)

