# third_world_search_engine

**An open-source news discovery API focused on regional journalism, independent publishers, and transparent search relevance.**

## Project Overview

third_world_search_engine is a Python and Flask-based search engine prototype that retrieves information from supported news websites, analyzes keywords, ranks results, and stores search information in MySQL.

I plan to evolve the project into an open-source news discovery service focused on regional journalism and independent publishers whose reporting can be difficult to discover through conventional search tools.

The platform will provide developers with configurable news sources, transparent relevance scoring, regional filtering, and a documented search API.

Rather than relying on opaque ranking mechanisms, the project will emphasize understandable, deterministic information retrieval techniques.

## Target Users

- Developers building news discovery applications
- Researchers exploring regional journalism and media coverage
- Independent publishers interested in content discoverability
- Open-source contributors working on search and information retrieval systems

## Tech Stack

- **Language:** Python 3
- **API Framework:** Flask
- **Database:** MySQL
- **ORM:** Flask-SQLAlchemy
- **Migrations:** Flask-Migrate
- **Web Extraction:** Requests, Beautiful Soup
- **Search:** Keyword analysis and relevance scoring

## Existing Implementation

The original prototype includes:

- Keyword-based news search endpoints
- Source-specific article extraction
- Text analysis and relevance scoring
- Search result ranking
- Database models and migrations
- Search result persistence

The original integrations included CNN, BBC, and The New York Times.

Support for regional and independent publications is part of the planned development rather than existing functionality.

## API

The original application exposes:

**POST /api/news**

Example request:

`{"keywords": ["technology", "education"]}`

The API accepts a list of keywords and processes them through the existing search pipeline.

## Project Structure

- `deltai_api/` — Flask application, models, and search components
- `migrations/` — Database migrations
- `db_config.py` — Database configuration
- `deltai_api.py` — Application entry point
- `requirements.txt` — Python dependencies

## Local Development

1. Clone the repository.
2. Create a virtual environment using `python3 -m venv .venv`.
3. Activate it using `source .venv/bin/activate`.
4. Install dependencies using `pip install -r requirements.txt`.
5. Configure a local MySQL database.
6. Set the required database environment variables.
7. Set `FLASK_APP=deltai_api.py`.
8. Run `flask db upgrade` and `flask run`.

Compatibility with modern Python versions and external news sources requires validation.

## Planned Development Roadmap

### Phase 1 — Backend Modernization

- [ ] Upgrade Python and Flask dependencies.
- [ ] Refactor ingestion, ranking, persistence, and API components.
- [ ] Add consistent request validation and error handling.
- [ ] Introduce unit and integration tests.
- [ ] Create a reproducible local development environment.

### Phase 2 — News Source Integration

- [ ] Add configurable RSS and Atom feed adapters.
- [ ] Introduce publisher metadata and source attribution.
- [ ] Implement language and regional classification.
- [ ] Normalize article metadata into a consistent format.
- [ ] Add duplicate detection and canonical URL handling.

### Phase 3 — Search and Ranking

- [ ] Improve keyword relevance scoring.
- [ ] Introduce freshness and source-diversity ranking factors.
- [ ] Implement regional and language filters.
- [ ] Add explainable relevance scoring.
- [ ] Introduce pagination and configurable result limits.

### Phase 4 — Developer Experience

- [ ] Publish OpenAPI documentation.
- [ ] Introduce configurable indexing and caching.
- [ ] Build a CLI for indexing approved feeds and running searches.
- [ ] Add structured logging and operational metrics.
- [ ] Create synthetic fixtures for deterministic search tests.

## Current Status and Future Direction

third_world_search_engine is an independently developed search API prototype that I plan to expand and maintain as an open-source news discovery platform.

The main objective is to make regional and independent journalism easier to discover through transparent and configurable search technology.

My initial development focus will be modernizing the search pipeline, adding support for configurable news sources, improving ranking quality, and exposing a stable API for integration into other applications.

As the project evolves, I intend to expand regional filtering, source attribution, indexing capabilities, and developer tooling.

The existing implementation provides a foundation for ingestion, ranking, and persistence, while the planned work involves substantial backend development, search architecture, API design, and automated testing.

The project will use synthetic testing fixtures and appropriately authorized public content or metadata, respecting publisher access policies and content rights.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
