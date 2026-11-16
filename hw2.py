import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 1
def create_rectangle(p1: data.Point, p2: data.Point) -> data.Rectangle:
    min_x = min(p1.x, p2.x)
    max_x = max(p1.x, p2.x)
    min_y = min(p1.y, p2.y)
    max_y = max(p1.y, p2.y)

    top_left = data.Point(min_x, max_y)
    bottom_right = data.Point(max_x, min_y)

    return data.Rectangle(top_left, bottom_right)

# Part 2
def shorter_duration_than(d1: data.Duration, d2: data.Duration) -> bool:
    if d1.minutes < d2.minutes:
        return True
    elif d1.minutes == d2.minutes:
        return d1.seconds < d2.seconds
    else:
        return False

# Part 3
def songs_shorter_than(songs: list[data.Song], max_duration: data.Duration) -> list[data.Song]:
    return [song for song in songs
            if shorter_duration_than(song.duration, max_duration)]

# Part 4
def running_time(library: list[data.Song], playlist: list[int]) -> data.Duration:
    total_minutes = 0
    total_seconds = 0

    for index in playlist:
        if 0 <= index < len(library):
            song = library[index]
            total_minutes += song.duration.minutes
            total_seconds += song.duration.seconds

    total_minutes += total_seconds // 60
    total_seconds = total_seconds % 60

    return data.Duration(total_minutes, total_seconds)

# Part 5
def validate_route(city_links: list[list[str]], route: list[str]) -> bool:
  if len(route) < 2:
    return True


  valid_links = {frozenset(link) for link in city_links}

  for i in range(len(route) - 1):
    pair = frozenset([route[i], route[i + 1]])
    if pair not in valid_links:
      return False

  return True


# Part 6
def longest_repetition(nums: list[int]) -> Optional[int]:
    if not nums:
        return None

    best_start = 0
    best_len = 1
    current_start = 0
    current_len = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            current_len += 1
        else:
            current_start = i
            current_len = 1

        if current_len > best_len:
            best_len = current_len
            best_start = current_start

    return best_start
