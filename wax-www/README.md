# Wax Machine WebApp

To run this, you need [Node.js](https://nodejs.org/en/download/current/). 
After installing node, `cd` to this directory and run:

```bash
npm i
```

Now you can run the app with this command:

```bash
npm run dev -- --open
```

## Inner pages

Inner pages of the app are in the `src/routes` directory. Each "page" makes a specific
call to the Wax Machine Server and loads the next page.
