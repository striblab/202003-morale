# svelte app

This is a project template for [Svelte](https://svelte.dev) apps. It lives at https://github.com/striblab/svelte3-template-webpack and is a fork of https://github.com/sveltejs/template-webpack.

To create a new project based on this template using [degit](https://github.com/Rich-Harris/degit):

```bash
npx degit striblab/svelte3-template-webpack svelte-app
cd svelte-app
```

*Note that you will need to have [Node.js](https://nodejs.org) installed.*

## Publishing

This project pulls JSON from a Google Form/Google Sheet on the teamjpg account. There is setup to do after cloning this repository.

### Setup

1. cd into this directory and run this command `touch .env`. You'll need this in order to run the publishing shell script
1. Ask Thomas for a copy of the Google credentials JSON as well as the .env variables.
1. Put the Google credentials JSON file into this file path `./src/data/`.
1. Make sure that the Google credentials, .zip file with static assets and json are not being tracked by Git.

### Publishing new content

Note: You will need your .aws/credentials file in order to publish.

1. From the repository directory, run `chmod 0755 publish.sh`. This changes the file permissions so that your computer knows that the shell script is an executable file. If you've already done this, skip this step.
1. Go to the Google Drive folder that holds all the media assets and download it as a .zip file. Rename it `files.zip` and drag and drop it into the `./src/data/` directory. **Note: If the .zip file is not named `files.zip` the script will not run.**
1. From the repository directory, run `./publish.sh`. This script deletes the original `files/` directory, unzips the zip file, uploads its content to S3, scrapes the JSON out of the Google Sheet and deletes the zip file. 


## Get started

Install the dependencies...

```bash
cd svelte-app
npm install
```

...then start webpack:

```bash
npm run dev
```

Navigate to [localhost:8080](http://localhost:8080). You should see your app running. Edit a component file in `src`, save it, and the page should reload with your changes.


## Deploying to the web

```bash
npm run deploy
```

Or, some other suggestions from Rich Harris:

### With [now](https://zeit.co/now)

Install `now` if you haven't already:

```bash
npm install -g now
```

Then, from within your project folder:

```bash
now
```

As an alternative, use the [Now desktop client](https://zeit.co/download) and simply drag the unzipped project folder to the taskbar icon.

### With [surge](https://surge.sh/)

Install `surge` if you haven't already:

```bash
npm install -g surge
```

Then, from within your project folder:

```bash
npm run build
surge public
```
