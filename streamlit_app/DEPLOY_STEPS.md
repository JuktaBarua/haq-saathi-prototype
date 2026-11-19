# Put the Haq Saathi prototype online (Streamlit Community Cloud, free)

This takes about 10 minutes. You will get a public link like `https://haq-saathi.streamlit.app` that the professor can open in any browser. Nobody needs to sign in to view it.

You need a GitHub account (free). Sign in with your own details; nobody else should do this for you.

## A. Put the files on GitHub

1. Go to https://github.com and sign in, or create an account.
2. Click **+** (top right), then **New repository**.
3. Name it `haq-saathi-prototype`. Choose **Public**. Click **Create repository**.
4. On the next page, click the link **uploading an existing file**.
5. Open this `streamlit_app` folder in Finder. Select everything inside it and drag it onto the GitHub page:
   - `app.py`
   - `requirements.txt`
   - `hotspots.json`
   - `prototype.html`
   - the `screens` folder
6. Optional: the theme lives in a hidden folder called `.streamlit`. To include it, press **Cmd + Shift + .** in Finder to show hidden files, then drag it in too. The app works without it.
7. Click **Commit changes**.

## B. Turn it into a website

1. Go to https://share.streamlit.io and click **Continue with GitHub**. Allow access when GitHub asks.
2. Click **Create app**, then **Deploy a public app from GitHub**.
3. Fill in:
   - Repository: `your-username/haq-saathi-prototype`
   - Branch: `main`
   - Main file path: `app.py`
   - App URL: type something short, such as `haq-saathi`
4. Click **Deploy**. Wait 1–3 minutes while it installs.
5. When the app appears, copy the address bar link. That is the link for the professor.

## C. Check before you share

- Open the link in a private or incognito window. If it loads without asking you to sign in, the professor can open it too.
- Free apps go to sleep after a few days without visits. A sleeping app shows a button saying it's asleep. Clicking it wakes the app in under a minute. Open it yourself the day before you send it.

## What the professor will see

- **Tap the phone**: the full clickable prototype. Tap the buttons on the screen, just like an app.
- **Guided walkthrough**: one screen at a time, with Sunita's story, what each screen does, and the UX law behind it. Buttons move through the flow.

## To change something later

Edit the file on GitHub (pencil icon) and commit. The app updates by itself within a minute.
