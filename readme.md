# kaogurai's api

```
git clone https://github.com/kaogurai/api
cd api
python3.8 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mv config.yaml.example config.yaml
hypercorn server:app
```
