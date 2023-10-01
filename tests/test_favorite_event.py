from page_object.FavoritePage import FavoritePage
from page_object.MenuPage import MenuPage
from page_object.SearchPage import SearchPage

class Test_FavoriteEvent():

    def test_favorite_event(self, after_favorite_event):
        search = SearchPage(after_favorite_event)
        search.search_event()

        favorite = FavoritePage(search.driver)
        favorite.favorite_event()

        search = SearchPage(favorite.driver)
        search.go_back()

        menu = MenuPage(search.driver)
        menu.access_favorites()

        favorite = FavoritePage(menu.driver)
        assert favorite.verify_favorites(), "Evento não favoritado"

    
    def test_remove_favorite_event(self, before_favorite_event):
        menu = MenuPage(before_favorite_event)
        menu.access_favorites()

        favorite = FavoritePage(menu.driver)
        favorite.remove_favorite()
        assert favorite.verify_empty_favorites_list(), "Existe eventos favoritados"




