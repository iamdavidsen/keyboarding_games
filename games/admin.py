from django.contrib import admin

from games.models import Game, Package, Category


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['title',  ]


class GameAdmin(admin.ModelAdmin):
    model = Game
    list_display = ['title', ]


class PackageAdmin(admin.ModelAdmin):
    model = Package
    list_display = ['get_game', 'version', ]

    def get_game(self, obj):
        return obj.game.title


admin.site.register(Category, CategoryAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Package, PackageAdmin)
