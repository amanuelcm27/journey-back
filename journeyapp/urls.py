from django.urls import path ,re_path
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    path("api/hello_world",views.JsonResponse),
    path("add_game/",views.add_game),
    path("all_games/",views.all_games),
    path("game_detail/<int:game_id>/",views.game_detail),
    path("search_games/",views.search_game),
    path("remove/<int:game_id>/",views.remove_game),
    path("add_wishlist/",views.add_wishlist),
    path("show_wishlist/",views.show_wishlist),
    path("remove_wishlist/<int:wish_id>/",views.remove_wishlist),
    path("mark_favourite/<int:game_id>/",views.markFavourite),
    path("filter/<str:method>/<str:genreOption>/",views.filter_games),
    path("all_genres/",views.all_genres),
    path("add_opinion/<int:game_id>/",views.add_opinion)
]
