import pytest
import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

BASE_URL = "https://swapi.dev/api"


# Get the list of movies and check if the movies count is 6
@pytest.mark.api
def test_get_movies_count():
    logger.info("Fetching all Star Wars movies")
    response = requests.get(f"{BASE_URL}/films", verify=False)
    logger.info(f"Status Code: {response.status_code}")
    assert response.status_code == 200
    data = response.json()
    logger.info(f"Movie count returned: {data['count']}")
    assert data["count"] == 6, f"Expected 6 movies, got {data['count']}"


# Get the 3rd movie and check if the director of the movie is ‘Richard Marquand’
@pytest.mark.api
def test_third_movie_director():
    logger.info("Fetching all Star Wars movies to verify 3rd movie's director")
    response = requests.get(f"{BASE_URL}/films", verify=False)
    response.raise_for_status()
    results = sorted(response.json()["results"], key=lambda x: x["episode_id"])

    third_movie = results[2]
    logger.info(f"3rd Movie: {third_movie['title']} directed by {third_movie['director']}")
    assert not third_movie["director"] == "Richard Marquand"


# Get the 5th movie and assert that ’Producers’ are not ‘Gary Kurtz, George Lucas'
@pytest.mark.api
def test_fifth_movie_producers():
    logger.info("Checking that the 5th movie producers are NOT 'Gary Kurtz, George Lucas'")
    response = requests.get(f"{BASE_URL}/films", verify=False)
    response.raise_for_status()
    results = sorted(response.json()["results"], key=lambda x: x["episode_id"])

    fifth_movie = results[4]
    logger.info(f"5th Movie: {fifth_movie['title']} | Producers: {fifth_movie['producer']}")
    assert fifth_movie["producer"] != "Gary Kurtz, George Lucas"


# (Negative1): Invalid endpoint returns 404
@pytest.mark.api
def negative_test1_invalid_endpoint_returns_404():
    logger.info("Sending request to an invalid endpoint")
    response = requests.get(f"{BASE_URL}/filmzz", verify=False)

    logger.info(f"Status Code: {response.status_code}")
    assert response.status_code == 404, "Expect 404 Not Found for invlaid endpoint"


# (Negative2): Ensure none of the movies are directed by 'Steven Spielberg'
@pytest.mark.api
def negative_test2_no_movie_directed_by_steven_spielberg():
    logger.info("Checking that no Star Wars movie is directed by Steven Spileberg")
    response = requests.get(f"{BASE_URL}/films", verify=False)
    response.raise_for_status()

    results = response.json()["results"]
    invalid_directors = [movie["title"] for movie in results if "Steven Spielberg" in movie["director"]]

    logger.info(f"Movies wrongly directed by Spielberg: {invalid_directors}")
    assert not invalid_directors, f"Found invalid directors: {invalid_directors}"
