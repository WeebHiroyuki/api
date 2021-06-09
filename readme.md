# kaogurai's api

```
git clone https://github.com/kaogurai/api
cd api
python3.8 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mv config.yml.example config.yml
hypercorn server:app
```
