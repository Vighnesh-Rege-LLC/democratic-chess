# Democratic Chess

Chess with the monarchy abolished: Presidents, Oligarchs, Media, Lawyers, Lobbyists, Bureaucrats and Citizens who don't always cooperate. Opens with the satirical intro reel (skippable).

Static single page (`public/index.html`), no build step at deploy time. Deployed as a Cloudflare Worker with static assets by Workers Builds from this repo (`wrangler.jsonc`), served at https://chess.apps.vighneshrege.com.

`public/index.html` is generated: edit `src/game.html` (the game) or `src/intro-reel.html` (the reel), then run `python3 src/build.py` and commit the result.
