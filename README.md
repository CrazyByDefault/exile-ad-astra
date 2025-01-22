# Exile Ad Astra

Collection of all the crap I've managed to put together for the layout extraction process for PoE2's Campaign Codex project.

## To get started -

```bash
pip install -r requirements.txt
```

1. Navigate to `main.py` and take a look at what's going on.
2. Download and dump your test images in `images/test` folder. You can also dump multiple nested folders here if you wish, all of them will be processed individually and dumped with the same folder structure into the `out/` folder.
3. Realize I've not gotten much done at all.
4. Contribute so that we can actually get somewhere.


## To contribute

- Have a patch? Fork this repo, make changes, PR back!
- Have suggestions/discussions? Start an issue or reach out on Discord! A Discord Invite URL is hidden in a comment at the bottom of `utils/__init__.py`, since I don't want bots scraping it :/
- Unsure of where you can contribute? Read ahead -
  
Here's the latest status update from me personally on this project, which might help you get started on one of the open problem statements -

---

Just a quick update with where I am with this (and a request for help :Sadge: ) -

- **Layout Extraction:** I have greatly improved the contour detection so as to get it to work with very noisy images such as those with bright gameplay under the map as well, such as https://discord.com/channels/1327009865008152576/1327020941078958141/1327686901502578748 and https://discord.com/channels/1327009865008152576/1327021248747671602/1327687419172225167 
  - I'm aiming for at least 85%+ accuracy, 15% of images not being processed correctly (at our current dataset size) can afford some manual intervention, not a huge deal IMO.
  - It is not yet perfect tho, but it is very very close to acceptable, and should produce acceptable results with a mazesolver. 
- **OCR**: I have basic OCR working, but I will need help creating a database for every zone in the game, mapped to every text-label that needs to be scanned for campaign completion. This is needed for the next step, where a MazeSolver will be tasked with going through the extracted layouts in order to learn how to cover the most Points of Interest, as efficiently as possible.
  - For eg: Infested Barrens has the following Points of Interest (at league start) - `The Azak Bog`, `Matlan Waterways`, `Jungle Ruins (starting point)`, and `Chimeral Wetlands`.
  - I would greatly appreciate if someone is magically sitting on a mapping of these for all zones, or spend the time to define all of these somewhere in a Sheet, so that I may simply use these. I'll get around to writing these down myself if no one does eventually, but yeah it's a ToDo as of now.
- **Mazesolver**: Made almost no progress here, except for some basic research. We can either -
  - Write our own MazeSolver with DFS/BFS/[model-free RL](https://en.wikipedia.org/wiki/Model-free_(reinforcement_learning)), or 
  - Will need a way to convert the extracted layouts (which we have in vector form) into an equivalent grid-maze, so we can use existing grid-maze solving algorithms such as [this](https://github.com/YeyoM/mazeSolver). Maybe more digging here will produce something better, least sure about my approach to this one.
- **Solution Heatmap**: Depending on how we solve the above, we will then need to put those results in a form that would benefit traversal in a league-start scenario. In my mind, I am thinking of this as a heatmap for a given zone and starting point.
  - For eg: *If you enter Infested Barrens at the top*, we will want to come up with a heatmap for where the most common spots for Matlan Waterways, Azak Bog, and Chimeral Wetlands are. 

I hope the above crap is coherent and not just a giant wall of text lol.

On a personal note, I have had a very hectic last few days, thanks to unanticipated travel for work over the weekend, and have been basically unable to play the game (except for hideout warrior-ing) or work on this project. I am starting to find more time again soon, and hope to make progress whenever I can.

AT THE SAME TIME, I think it is not great for progress as a whole to be blocked on me, or for others to refrain from tackling this problem under the assumption that I am actively working on it. Please help in any way you want to/are able to, and if you are unsure of what to look into, pick one of the above tasks I've outlined and start hacking away at something that might work, or even just start a discussion on how we can approach the problem, or tell me where I'm approaching this wrong and how we can better solve this problem.

---

Awesome, thanks for checking this project out! Hope we can see this to some form of completion before the next Acts are added to PoE2!