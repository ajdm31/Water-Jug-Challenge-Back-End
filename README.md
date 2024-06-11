
# Water-Jug-Challenge-Back-End

This API solves the classic Water Jug Riddle. Given two jugs with capacities X and Y, it finds the steps to measure exactly Z gallons, using the Breadth First Search Algorithm.


## Installation

To run this project locally, follow these steps:

1. Clone the repository:
```bash
  git clone https://github.com/ajdm31/Water-Jug-Challenge-Back-End.git
```
2. cd into repository:
```bash
  cd water-jug-challenge-back-end
```

3. **MACOS/Linux** Create a virtual environment and install dependencies:
```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
```

3. **Windows** Create a virtual environment and install dependencies:
```bash
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
```

4. Run migrations and start the server:
```bash
    python manage.py migrate
    python manage.py runserver
```

5. Run test file "tests.py":
Stop server and then:
```bash
    python manage.py test
```

    