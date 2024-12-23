# https://raw.githubusercontent.com/yes1am/douban-movie-calendar/refs/heads/master/douban-movie-calendar-2024.json
def get_today_movie_info():
    import requests
    from datetime import datetime
    import json

    # Fetch data from URL
    url = "https://raw.githubusercontent.com/yes1am/douban-movie-calendar/refs/heads/master/douban-movie-calendar-2024.json"
    try:
        response = requests.get(url)
        movies = response.json()
    except:
        return None

    # Get today's date in the format used in comments (YYYY-MM-DD)
    today = datetime.now().strftime("%Y-%m-%d")
    
    # First try to find exact match for today
    for movie in movies:
        if today in movie.get('comment', ''):
            return movie
    
    # If no exact match, find nearest date
    nearest_movie = None
    smallest_diff = float('inf')
    
    for movie in movies:
        comment = movie.get('comment', '')
        # Extract date from comment (assumes format YYYY-MM-DD at start of comment)
        try:
            movie_date = datetime.strptime(comment[:10], "%Y-%m-%d")
            diff = abs((datetime.now() - movie_date).days)
            if diff < smallest_diff:
                smallest_diff = diff
                nearest_movie = movie
        except:
            continue
    
    return nearest_movie

if __name__ == "__main__":
    print(get_today_movie_info())
