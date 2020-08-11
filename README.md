# WT-Social-Test
...a repo of tests on <https://wt.social/> using pytest and selenium.

#### Setup
- Clone this repo
- Run `pip3 install -r requirements.txt`
- Edit data/login_creds.sample.py w/ your credentials and rename it to data/login_creds.py

#### Run the tests
How I run this a specific test: `pytest -v test_posts.py --browser=firefox`

Or you can run all the test: `pytest -v --browser=firefox`

I had trouble with selenium using chrome (default browser) so I added the `--browser=firefox`. But this was just my machine, feel free to leave that out.

Also, add the flag `--headed` to watch selenium run the test. Or `--headless` to turn that off.