from main import check_document_existance, get_doc_owner_name, get_all_doc_owners_names, add_new_shelf, delete_doc, get_doc_shelf, show_all_docs_info, add_new_doc
import pytest

class TestAccountant:

    def test_get_all_doc_owners_names(self):
        expected = {'Василий Гупкин', 'Геннадий Покемонов', 'Аристарх Павлов'}
        assert get_all_doc_owners_names() == expected

    def test_show_all_docs_info(self):
        expected = '\npassport 2207 876234 Василий Гупкин\ninvoice 11-2 Геннадий Покемонов\ninsurance 10006 Аристарх Павлов\n'
        assert show_all_docs_info() == expected

    @pytest.mark.parametrize("test_input,expected", (['11-2', "Геннадий Покемонов"], ['10006', "Аристарх Павлов"], ['2207 876234', "Василий Гупкин"], [11-2, None]))
    def test_get_doc_owner_name(self, test_input, expected):
        assert get_doc_owner_name(test_input) == expected


    @pytest.mark.parametrize("test_input,expected", (['11-2', True], ['10006', True], ['2207 876234', True], [11-2, False]))
    def test_check_document_existance(self, test_input, expected):
        assert check_document_existance(test_input) is expected

    @pytest.mark.parametrize("test_input,expected", (['10006', '2'], ['11-2', '1'], ['2207 876234', '1'], [11-2, None]))
    def test_get_doc_shelf(self, test_input, expected):
        assert get_doc_shelf(test_input) == expected

    def test_add_new_doc(self):
        assert add_new_doc('10008', 'insurance', 'Антон Чегур', '3') == '3'
        assert add_new_doc('10008', 'insurance', 'Антон Чегур', 3) != '3'

    @pytest.mark.parametrize("test_input,expected", (['2', False], ['5', True]))
    def test_add_new_shelf(self, test_input, expected):
        assert add_new_shelf(test_input) is expected

    @pytest.mark.parametrize("test_input, expected", (['10006', ('10006', True)], ['11-2', ('11-2', True)], [11-2, None]))
    def test_delete_doc(self, test_input, expected):
        assert delete_doc(test_input) == expected
