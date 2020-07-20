from Steps import StepsForTest

my_steps = StepsForTest()


class Testing:

    def test_go_to_google(self):
        my_steps.go_to_google()

    def test_search_In_GoogLe(self):
        my_steps.search_In_GoogLe('სამი გოჭი')

    def test_check_title_contains(self):
        my_steps.check_title_contains()

    def test_clear_button(self):
        button = my_steps.check_clear_button()
        assert button.is_enabled() and button.is_displayed()

    def test_count_results(self):
        my_steps.count_results()

    def test_check_all_title_contains(self):
        result = my_steps.check_all_title_contain()
        assert result == True

    def test_go_to_photos_page(self):
        my_steps.go_to_Photos_page()

    def test_search_by_photo_button(self):
        button = my_steps.check_Search_By_Photo_button_exist()
        assert button.is_enabled() and button.is_displayed()

    def test_open_picture_from_youtube(self):
        my_steps.open_picture_from_youtube()

    def test_close_button(self):
        button = my_steps.check_photo_close_button()
        assert button.is_enabled() and button.is_displayed()

    def test_image_exist(self):
        my_steps.check_image_exist()

    def test_youtube_button(self):
        button = my_steps.youtube_watch_button_exist()
        assert button.is_enabled() and button.is_displayed()

    def test_share_button(self):
        button = my_steps.check_share_button_exist()
        assert button.is_enabled()

    def test_more_options_button(self):
        button = my_steps.check_more_options_button()
        assert button.is_enabled()

    def test_get_help_button(self):
        button = my_steps.check_get_help_button()
        assert button.is_enabled()

    def test_feedback_button(self):
        button = my_steps.check_feedback_button()
        assert button.is_enabled()

    def test_title_of_photo(self):
        title = my_steps.title_of_photo()
        assert title == True

    def test_youtube_watch_button(self):
        button = my_steps.youtube_watch_button_exist()
        assert button.is_enabled() and button.is_displayed()

    def test_youtube_watch_time(self):
        text = my_steps.youtube_watch_time()
        text_must_be = 'Watch (7:15)'
        assert text == text_must_be

    def test_author_text(self):
        author = my_steps.check_author()
        author_must_be = 'Uploaded by: GioKidsClub, Apr 5, 2019'
        assert author == author_must_be

    def test_views_and_likes(self):
        views_and_likes = my_steps.views_and_likes()
        views_and_likes_must_be = '377K Views · 1.11K Likes'
        assert views_and_likes == views_and_likes_must_be

    def test_related_images(self):
        result = my_steps.related_images()
        assert result == True

    def test_clear_input(self):
        my_steps.clear_input()

    def test_input_search(self):
        text = 'ხუთკუნჭულა'
        result = my_steps.input_search(text)
        assert result == text

    def test_count_photos(self):
        my_steps.count_photos()

    def test_title_contains(self):
        my_steps.count_contain_title()

    def test_driver_close(self):
        my_steps.driver_close()
