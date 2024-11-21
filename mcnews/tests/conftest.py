import pytest
from mcnews.searchapi import SearchApiClient, VERSION

COLLECTION_MEDIACLOUD = "mc_search-*"

port_map = {
	"prod": 8000,
	"staging": 8200,
	"dev": 8100
}

env_options = tuple(port_map.keys())


def pytest_addoption(parser):
	parser.addoption(
		"--env",
		action="store",
		default="prod",
		help=f"Toggles which news-search-api environment to test against: {env_options}",
		choices=env_options
		)


@pytest.fixture(scope="class")
def api_client(request):
	environment = request.config.getoption("--env")
	port = port_map[environment]
	request.cls._api = SearchApiClient(COLLECTION_MEDIACLOUD)
	request.cls._api.API_BASE_URL = f"http://localhost:{port}/{VERSION}/"