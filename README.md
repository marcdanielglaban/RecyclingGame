## Overview

The game presents items to be sorted into different bins based on their categories (Paper, Metal, Plastic, Glass). The player scores points for correctly sorting items within a time limit, and the game provides a final accuracy score and grade at the end.

Classes:

• Trash: Represents individual items with a name and category.

• Bin: Represents bins for different categories and can accept items.

• RecyclingGame: The main class managing the game. It initializes the game interface, handles user input, updates the score, and calculates accuracy and grade.

Game Logic:

• The game has a list of items (Trash) and bins (Bin).

• Users start the game by selecting a difficulty level and clicking the "Start Game" button.

• Bins are displayed as buttons, and the player clicks a bin to sort the current item.

• The game tracks the score, time remaining, and displays results at the end.

User Interface:

•The Tkinter library is used for the GUI.

•Bins are represented as buttons.

•Labels display the current item, score, and time remaining.

•A separate window shows the final results and bin contents.

Scoring and Results:

•The player gains points for correct sorting and loses points for incorrect sorting.

•The game calculates accuracy and assigns a grade based on the player's performance.

•Results are displayed in a messagebox.

Sustainable Development Goal (SDG) Alignment:


• SDG 12: Responsible Consumption and Production:

The game promotes responsible consumption by encouraging players to correctly sort items into recycling bins.
It raises awareness about waste management and the importance of recycling different materials.

• SDG 13: Climate Action:

Proper waste management, including recycling, contributes to reducing the environmental impact and mitigating climate change.

• SDG 15: Life on Land:

Recycling and proper waste management contribute to protecting terrestrial ecosystems by reducing pollution and preserving natural resources.

## Technologies Used

• Python: The primary programming language.

• Tkinter : Used to create the graphical user interface of the recycling game.

• Random Module: Used for shuffling the list of trash items, adding an element of randomness to the game.

• Messagebox Module (part of Tkinter): Utilized for displaying information windows, such as game results and bin contents.

## Screenshots of the Program



## Individual Assessment
Main Programmer - Glaban, Marc Daniel - 100%
