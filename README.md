# Our idea

## What we did to do what we did:
We replaced every pixel of the canvas to match a canvas which we imagined.

## How we did?
* A script replace.py which creates new copies of pixel_update.json to replace 5 new pixels
* a bash script to run this python script for the entirety of the pixels on the canvas
* a cron job to do this every night when we can replace pixels in peace using gh pr create
* the cron job -- 
* a canvas.png where our -- to be replaced with -- image is located

