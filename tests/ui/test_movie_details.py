import pytest
import logging
from pages.homepage import HomePage
from pages.movie_detail_page import MovieDetailPage


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)


# Test 1: Sort movies by Title
@pytest.mark.ui
def test_sort_movies_by_title(open_homepage, driver):
    logger.info("Starting test: Sort movies by Title")
    driver = open_homepage
    home_page = HomePage(driver)

    logger.info("Clicking on 'Title' column to sort movies")
    home_page.click_sort_by_title()

    titles = home_page.get_all_movie_titles()
    logger.info(f"Movie titles after sorting: {titles}")

    assert "The Phantom Menace" in titles[-1], "Expected last movie to be 'The Phantom Menace'"


# Test 2: View 'The Empire Strikes Back' → Species list should include 'Wookie'
@pytest.mark.ui
def test_species_for_empire_strikes_back(open_homepage, driver):
    logger.info("Starting test: Species for 'The Empire Strikes Back'")
    driver = open_homepage
    home_page = HomePage(driver)

    logger.info("Clicking on 'The Empire Strikes Back'")
    home_page.click_empire_strikes_back()

    detail = MovieDetailPage(driver)
    species = detail.get_species()
    logger.info(f"Species list: {species}")

    assert "Wookie" in species, "'Wookie' should be in the species list for Empire Strikes Back"


# Test 3: View 'The Phantom Menace' → Planets list should NOT include 'Camino'
@pytest.mark.ui
def test_camino_not_in_phantom_menace(open_homepage, driver):
    logger.info("Starting test: Planets for 'The Phantom Menace'")
    driver = open_homepage
    home_page = HomePage(driver)

    logger.info("Clicking on 'The Phantom Menace'")
    home_page.click_phantom_menace()

    detail = MovieDetailPage(driver)
    planets = detail.get_planets()
    logger.info(f"Planets list: {planets}")

    assert "Camino" not in planets, "'Camino' should not be in the planets list for The Phantom Menace"


# (Negative): Try selecting a non-existent movie (e.g., 'Star Trek')
@pytest.mark.ui
def negative_test_non_exist_movie_click(open_homepage, driver):
    logger.info("Starting test: Non-exist Movie Click")
    driver = open_homepage
    home_page = HomePage(driver)

    try:
        logger.info("Trying to click on 'Star Trek' (should not exist)")
        home_page.click_movie_by_title("Star Trek")
        logger.error("Test failed — Unexpectedly found and clicked 'Star Trek'")
        assert False, "Should not be able to click a non-existent movie like 'Star Trek'"
    except Exception as e:
        logger.info(f"Caught expected exception: {str(e)} — PASS")
        assert True

