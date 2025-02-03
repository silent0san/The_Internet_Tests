from pages.drag_and_drop_page import DragAndDropPage
from pages.home_page import HomePage


def test_drag_and_drop(driver):
    home_page = HomePage(driver)
    drag_and_drop_page = DragAndDropPage(driver)
    home_page.click_page("Drag and Drop")

    source_element_header_before = drag_and_drop_page.get_source_element_header()
    drag_and_drop_page.drag_elements()

    source_element_header_after = drag_and_drop_page.get_source_element_header()

    #  Verify by checking headers, if source element has been moved to position of target element
    assert source_element_header_after != source_element_header_before


def test_drag_and_drop_back(driver):
    drag_and_drop_page = DragAndDropPage(driver)

    drag_and_drop_page.drag_elements()

    source_element_header_after = drag_and_drop_page.get_source_element_header()

    #  Verify by checking headers, if source element has been moved to position of target element
    assert source_element_header_after == "A"
