from page_object.SearchPage import SearchPage

class Test_SearchEvent():

    def test_search_event(self, init_app):
        search = SearchPage(init_app)
        assert search.search_event(), "Evento não encontrado"
        
        
    def test_no_result_found_event(self, init_app):
        search = SearchPage(init_app)

        assert search.not_found_event(), "Evento encontrado"
