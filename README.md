
# Star Wars Automation Testing Project

This project is built to automate the testing of Star Wars movie app using **Selenium with Python**, **Pytest**, and **GitHub Actions**. The application uses the public [SWAPI API](https://swapi.dev).

---

## Project Features

1. UI Functional Test Coverage  
2. API Functional Test Coverage  
3. Page Object Model (POM) Structure  
4. Modular and Reusable Test Design  
5. GitHub Actions CI Integration

---

## Folder Structure

```
starwars_tests/
├── pages/                   # Page Object Models
│   ├── home_page.py
│   └── movie_detail_page.py
├── tests/
│   ├── ui/                  # UI Test Cases
│   │   ├── test_sort_movies.py
│   │   └── test_planet_details.py		
│   │   └── test_species_details.py
│   └── api/                 # API Test Cases
│       └── test_movies_list.py
├── conftest.py              # Pytest Fixtures
├── requirements.txt
└── .github/
    └── workflows/
        └── pytest.yml       # GitHub Actions CI Pipeline
```

---

## Automated Test Scenarios

###  UI Scenarios (Selenium)
- Sort movies by `Title`, assert last movie is `The Phantom Menace`
- Click `The Empire Strikes Back`, assert `Wookie` in species list
- Open `The Phantom Menace`, assert `Camino` is **not** in planets list

### API Scenarios (SWAPI)
- Assert total number of movies is 6
- Assert 3rd movie director is `Richard Marquand`
- Assert 5th movie **producers** are **not** `Gary Kurtz, George Lucas`

---

## ▶How to Run Tests Locally

### 1. Clone the Repo & Install Dependencies
```bash
git clone https://github.com/your-username/starwars-automation.git
cd starwars-automation
pip install -r requirements.txt
```

### 2. Start the App Locally
```bash
cd star-wars
npm install
npm run dev
```

Ensure the app runs at `http://localhost:3000`.

### 3. Run Tests
```bash
pytest -v
```

Run only UI or API:
```bash
pytest -v -m ui
pytest -v -m api
```

---

## Tech Stack

| Tool              | Purpose                       |
|------------------|-------------------------------|
| Python + Pytest  | Test Framework                |
| Selenium         | UI Automation                 |
| Requests         | API Testing                   |
| GitHub Actions   | CI/CD                          |
| Page Object Model| Test Architecture Pattern     |

---

## GitHub Actions CI

Tests run automatically via GitHub Actions on each push.

**Workflow file:** `.github/workflows/pytest.yml`

You can trigger the workflow by:
- Pushing code to `main` or `test` branch
- Opening a pull request

---

## Author

**Nutan Kumar**  
Senior QA Automation Engineer  


---

## Notes

- Base URL: `http://localhost:3000`
- Star Wars API: [https://swapi.dev](https://swapi.dev)
- This project is created as part of a QA Technical Assessment.
