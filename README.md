# Discord-Simulator
simulates a discord server with markov chains


requirements: just use `install-deps.bat`, python 3.5.3 (im sure later versions work i just use 3.5.3 because tensorflow only works on that version)

multiple bots are allowed for different channels, i have a server that simulates one of my other servers and the bot posts different things in different channels through probably 10 cmd.exe windows

to acquire a Data, first you need to use the [Discord History Tracker](https://dht.chylex.com/). I recommend turning off embeds when using it. Once you have captured a good amount (1000-3000) you should see a file named `dht.txt`. Go to the viewer (located on the DHT page) and put in the file. At the top click settings and turn off both checkboxes so that it can load faster AND it will enable the bot to use \* , \`, \`\`\`, :emoji: etc. Click on the messages per page dropdown and click "all."

![settings](https://cdn.discordapp.com/attachments/419149275142946829/419158271614779393/unknown.png)

Then get the Chrome extension [Scraper](https://chrome.google.com/webstore/detail/mbigbapnjcgaffohmbkdlecaccepngjd). Once you have it right click on a message's body (as long as its the text portion) and click "scrape similar..." (or if you cant, just open scraper and set the location to `//div[2]/div/div/p`.) Then you can click copy to clipboard and paste it into Notepad. 

![yöted](https://cdn.discordapp.com/attachments/419149275142946829/419159447915593728/unknown.png)

Copy it back from notepad and go to [remove diacritics](http://utils.paranoiaworks.org/diacriticsremover/). This is to help with removing unsupported characters. Paste *that* into Notepad and go to find and replace. Replace all of the characters ` []()"'{} ` with nothing (some may be supported, just in case). Save the file into the main directory of the bot. Set the encoding to ANSI (IMPORTANT, OTHER ENCODINGS ALLOW ILLEGAL CHARACTERS).

Getting the usernames: If the server is small you can type them by hand. If it is large then you can go back to the scraping but instead of doing the body you scrape the username. Save those to a file and set the encoding to ANSI (IMPORTANT, OTHER ENCODINGS ALLOW ILLEGAL CHARACTERS).

Edit the `main.py` script. Change the text file to your message file, the un or users or usernames i dont remember file to your users file, and the big weird number with your channel's id (right click a channel and click copy id or find it in the last part of the url). Change the token to your bot's token and you're good.

The bot will start becoming sentient.
