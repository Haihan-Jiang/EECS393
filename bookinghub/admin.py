from django.contrib import admin
from .models import Post, room, User, reservation, hotel, hotelStaff


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish',
                    'status')
    list_filter = ('status', 'created', 'publish', 'author')

    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

@admin.register(room)
class PostAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'status', 'slug', 'roomType', 'roomID',
                    'price', )
    list_filter = ('status', )
    search_fields = ('hotel', 'roomID', 'roomType')
    prepopulated_fields = {'slug': ('hotel', 'roomType', 'roomID')}
    ordering = ('status', 'price')

@admin.register(User)
class PostAdmin(admin.ModelAdmin):
    list_display = ('userID', 'userPassword', 'slug', 'gender', 'name', 'expectedMinPrice', 'expectedMaxPrice', 'status')
    list_filter = ('status', )
    search_fields = ('userID', 'name', 'expectedMinPrice', 'expectedMaxPrice')
    prepopulated_fields = {'slug': ('name', )}
    ordering = ('status', 'expectedMinPrice')

@admin.register(reservation)
class PostAdmin(admin.ModelAdmin):
    list_display = ('reservationID', 'reserveTime', 'status', 'roomNumber', 'hotelName', 'price', 'slug', 'checkIn', 'checkOut')
    list_filter = ('status', )
    search_fields = ('reservationID', 'reserveTime', 'status', 'hotelName')
    prepopulated_fields = {'slug': ('hotelName', )}
    ordering = ('status', 'price', 'reserveTime')

@admin.register(hotel)
class PostAdmin(admin.ModelAdmin):
    list_display = ('hotelName', 'location', 'rating', 'price', 'contactEmail', 'contactPhoneNumber', 'slug', 'hotelStaff')
    list_filter = ('rating', )
    search_fields = ('hotelName', 'rating', 'price', )
    prepopulated_fields = {'slug': ('hotelName', )}
    ordering = ('rating', 'price', )

@admin.register(hotelStaff)
class PostAdmin(admin.ModelAdmin):
    list_display = ('staffID', 'name', 'contactEmail', 'contactPhoneNumber', 'slug', )
    list_filter = ('staffID', )
    search_fields = ('hotelName', 'rating', 'price', )
    prepopulated_fields = {'slug': ('name', )}
    ordering = ('staffID',)
