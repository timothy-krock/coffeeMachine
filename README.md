# I Automated a Coffee Machine!

I had been looking for a new talking point to tack a Raspberry Pi on for a while, when I ran into a store that had knock-off Keurigs on sale for pretty cheap. This was the perfect thing to attach a Pi to, because automated coffee, who doesn't want that?

This was also a prime opportunity to learn to do some home-[IOT](https://en.wikipedia.org/wiki/Internet_of_things). There's no permanent internet at the Krock house right now, so there's no option for a traditional server. Instead, I had to do one of the jankier things I've put my name on. I discovered [myjson](http://myjson.com/), and used it to create the most primitive of APIs. On one end, it's controlled by a webpage that looks like somebody hired a five year old to build a webpage, just barebones bootstrap and js. When the coffee button is pushed, the JSON stored is changed to indicate that coffee should be made. (The webpage also shows last connection, and the machine's IP address, so I can SSH to it instead of hooking my coffee machine up to a keyboard mouse and monitor.)

On the other side is the coffee machine itself. I mentioned before that this was the perfect thing to stick a Pi into, but I can't express how easy it was to pull off. The machine I got was one of those single-cup things that makes coffee at the push of a button. Most buttons, I though, are just a connection of two wires, and I figured I out to be able to solder a relay in to the same points as the button such that I could short it, (simulate pressing the button) by way of the Pi, and probably finish this in like three hours. 

I was wrong. I got it destroyed, figured out, reassembled, and making coffee in less than half that. It's the first time [Hofstadter's Law](https://en.wikipedia.org/wiki/Hofstadter%27s_law) had ever not applied in one of my projects. Soldering was tricky because I'm bad at it, but it went up without a hitch. 

The programming connecting the pi to the MYJSON api took me a little longer than expected, but most of that was fidgeting with the rc.local file so that the API watcher starts when the pi boots. 

Going forward, I hope to enable a "queue coffee at X time" function, and I have a Pi sound card that I'd like to turn into a voice command parser, but that's a way down the road. 

Thanks for reading, this was a reasonable quick and super fun project, and now I can push a button on my phone and have coffee!
