import data
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle_bottom_left_to_top_right(self):
        rect = hw2.create_rectangle(data.Point(2, 2), data.Point(10, 10))
        self.assertEqual(rect, data.Rectangle(data.Point(2, 10), data.Point(10, 2)))

    def test_create_rectangle_top_right_to_bottom_left(self):
        rect = hw2.create_rectangle(data.Point(10, 10), data.Point(2, 2))
        self.assertEqual(rect, data.Rectangle(data.Point(2, 10), data.Point(10, 2)))

    def test_create_rectangle_top_left_to_bottom_right(self):
        rect = hw2.create_rectangle(data.Point(2, 10), data.Point(10, 2))
        self.assertEqual(rect, data.Rectangle(data.Point(2, 10), data.Point(10, 2)))

    def test_create_rectangle_bottom_right_to_top_left(self):
        rect = hw2.create_rectangle(data.Point(10, 2), data.Point(2, 10))
        self.assertEqual(rect, data.Rectangle(data.Point(2, 10), data.Point(10, 2)))

    def test_create_rectangle_shared_x(self):
        rect = hw2.create_rectangle(data.Point(5, 2), data.Point(5, 10))
        self.assertEqual(rect, data.Rectangle(data.Point(5, 10), data.Point(5, 2)))

    def test_create_rectangle_shared_y(self):
        rect = hw2.create_rectangle(data.Point(2, 7), data.Point(10, 7))
        self.assertEqual(rect, data.Rectangle(data.Point(2, 7), data.Point(10, 7)))

    # Part 2
    def test_shorter_duration_than_more_seconds_on_shorter(self):
        d1 = data.Duration(2, 50)
        d2 = data.Duration(3, 10)
        self.assertTrue(hw2.shorter_duration_than(d1, d2))
        self.assertFalse(hw2.shorter_duration_than(d2, d1))

    def test_shorter_duration_than_equal(self):
        d1 = data.Duration(3, 10)
        d2 = data.Duration(3, 10)
        self.assertFalse(hw2.shorter_duration_than(d1, d2))

    def test_shorter_duration_than_diff_only_in_seconds(self):
        d1 = data.Duration(4, 15)
        d2 = data.Duration(4, 16)
        self.assertTrue(hw2.shorter_duration_than(d1, d2))
        self.assertFalse(hw2.shorter_duration_than(d2, d1))

    # Part 3
    def test_songs_shorter_than_mixed(self):
        s1 = data.Song("Artist A", "Short Song", data.Duration(2, 45))
        s2 = data.Song("Artist B", "Exact Limit Song", data.Duration(3, 30))
        s3 = data.Song("Artist C", "Long Song", data.Duration(4, 10))
        s4 = data.Song("Artist D", "Another Short Song", data.Duration(3, 29))
        songs = [s1, s2, s3, s4]

        result = hw2.songs_shorter_than(songs, data.Duration(3, 30))
        self.assertEqual(result, [s1, s4])

    def test_songs_shorter_than_empty(self):
        self.assertEqual(hw2.songs_shorter_than([], data.Duration(3, 0)), [])

    # Part 4
    def test_running_time_standard_and_repeats(self):
        library = [
            data.Song("Decemberists", "June Hymn", data.Duration(4, 30)),
            data.Song("Broken Bells", "October", data.Duration(3, 40)),
            data.Song("Kansas", "Dust in the Wind", data.Duration(3, 29)),
            data.Song("Local Natives", "Airplanes", data.Duration(3, 58)),
        ]
        playlist = [0, 2, 1, 3, 0]
        self.assertEqual(hw2.running_time(library, playlist), data.Duration(20, 7))

    def test_running_time_out_of_range_indices(self):
        library = [
            data.Song("Decemberists", "June Hymn", data.Duration(4, 30)),
            data.Song("Broken Bells", "October", data.Duration(3, 40)),
        ]
        playlist = [-1, 0, 2, 99, -5, 1]
        self.assertEqual(hw2.running_time(library, playlist), data.Duration(8, 10))

    def test_running_time_empty_playlist(self):
        library = [data.Song("Decemberists", "June Hymn", data.Duration(4, 30))]
        self.assertEqual(hw2.running_time(library, []), data.Duration(0, 0))

    # Part 5
    def test_validate_route_valid_both_directions(self):
        city_links = [
            ["san luis obispo", "santa margarita"],
            ["san luis obispo", "pismo beach"],
            ["atascadero", "santa margarita"],
            ["atascadero", "creston"],
        ]
        route = ["pismo beach", "san luis obispo", "santa margarita", "atascadero", "creston"]
        self.assertTrue(hw2.validate_route(city_links, route))

    def test_validate_route_invalid_skipped_link(self):
        city_links = [
            ["san luis obispo", "santa margarita"],
            ["atascadero", "santa margarita"],
        ]
        route = ["san luis obispo", "atascadero"]
        self.assertFalse(hw2.validate_route(city_links, route))

    def test_validate_route_empty_and_single_city(self):
        city_links = [["san luis obispo", "santa margarita"]]
        self.assertTrue(hw2.validate_route(city_links, []))
        self.assertTrue(hw2.validate_route(city_links, ["san luis obispo"]))

    # Part 6
    def test_longest_repetition_unique_max(self):
        self.assertEqual(hw2.longest_repetition([1, 1, 2, 2, 1, 1, 1, 3]), 4)

    def test_longest_repetition_tied_runs(self):
        self.assertEqual(hw2.longest_repetition([5, 5, 2, 2, 8, 8]), 0)

    def test_longest_repetition_empty(self):
        self.assertIsNone(hw2.longest_repetition([]))

    def test_longest_repetition_single_element(self):
        self.assertEqual(hw2.longest_repetition([42]), 0)

    def test_longest_repetition_no_adjacent_duplicates(self):
        self.assertEqual(hw2.longest_repetition([1, 2, 3, 4, 5]), 0)





if __name__ == '__main__':
    unittest.main()
