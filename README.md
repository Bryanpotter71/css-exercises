# CSS Exercises

These exercises consist of a series of CSS-related tasks intended to complement the HTML and CSS content on The Odin Project (TOP). They should only be completed when instructed during the course of the curriculum.

When doing these exercises, please use all documentation and resources you need to accomplish them. You are _not_ intended to have any of this stuff memorized at this point. Check the docs, use Google, and do what you need to do (besides checking the solutions) to get them done.

## Contributing

If you have suggestions to improve an exercise, ideas for a new exercise, or notice an issue with an exercise, please feel free to open an issue after thoroughly reading our [contributing guide](https://github.com/TheOdinProject/.github/blob/main/CONTRIBUTING.md).

## How To Use These Exercises

1. Fork and clone this repository. To learn how to fork a repository, see the GitHub documentation on how to [fork a repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo).
    * Copies of repositories on your machine are called clones. If you need help cloning to your local environment, you can learn how from the GitHub documentation on [cloning a repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository).
2. Go to an exercise directory and open the HTML file in a web browser. You can open the file directly or use something like VSCode's Live Server extension.
3. For each exercise, read the README thoroughly before starting any work.
    * Each README has a "Self Check" list. Use this to ensure you haven't missed any important details in your implementation.
4. Make your edits in the `index.html` and/or the `style.css` files in order to make the output in your browser look like the Desired Outcome image(s).
    * Depending on the instructions of the exercise, you may only need to make edits in one of these files.
5. Once you successfully finish an exercise, check TOP's solution to compare it with yours.
   * You should not be checking the solution for an exercise until you finish it!
   * Keep in mind that TOP's solution is not the only solution. If your solution differs wildly from TOP's solution (and still passes the self-check criteria), feel free to ask about it in the chatroom.
6. Do not submit your solutions to this repo, as any PRs that do so will be closed without merging.

## Some Hints
- The official solutions put all changes at the _end_ of the CSS file, which may duplicate some selectors (e.g. there might be a `body {}` in the given CSS and another `body {}` in the solution). When you are working on an exercise, it is best practice to add your CSS to existing selectors instead of duplicating them at the end of the file. We're sacrificing this best practice in our official solutions to make it extra clear to you what things we changed to solve the exercise.
- Unless listed in the self-check section, do not worry about getting the exact pixel value for things like margin, padding and font size. These exercises are intended to test your knowledge of CSS, not your ability to guess that a screenshot is using `font: sans-serif bold 16px` or that the margin is _exactly_ `42px`.
- You may need to add some elements to your HTML to get things into the right spot. (For the first few exercises, we make it explicit when this needs to happen.)
- You may need to add more selectors to your CSS file. The first few exercises have almost everything already done for you, but as you progress, you'll find that you need to add more and more selectors to get the correct result.

## Extra Tool: Color Converter

A small Python script named `color_converter.py` has been added to help convert colors between hexadecimal and RGB formats or generate random colors. You can run it with the following commands:

```bash
# Convert a hex value to RGB
python3 color_converter.py --hex "#ff0000"

# Convert an RGB value to hex
python3 color_converter.py --rgb "255,0,0"

# Generate a random color
python3 color_converter.py --random
```

The script prints the result directly to the terminal.

### Running on iPhone

To run `color_converter.py` on an iPhone, install a Python
interpreter app such as **Pythonista** or **Pyto** from the App Store.
Copy this repository (or just the script) into the app and execute the
same commands shown above in the in-app terminal.

### Running in Replit

If you want to try the script in Replit:

1. Open the Replit app (or go to <https://replit.com>) and create a new
   **Python** repl.
2. Upload `color_converter.py` or import this repository from GitHub.
3. Use the built-in Shell tab to run any of the example commands shown
   above, such as:

   ```bash
   python3 color_converter.py --random
   ```

The output will appear in the console just like on a local machine.

### Starting a New Repository

If you want to keep the script in your own GitHub repository named
**Maiden Voyage**, follow these steps:

1. Sign in to GitHub and create a new repository called `Maiden-Voyage`.
2. Clone the empty repository or create a new folder in Replit and run:

   ```bash
   git init
   git add color_converter.py README.md
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin <your repository URL>
   git push -u origin main
   ```

This gives you a fresh repo with just the sample program and README so it
won't be tied to any private Odin Project repositories.


