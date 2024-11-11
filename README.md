# Scribe
Continuation of WebscrapeDnd

Description: Developed a dynamic Dungeons & Dragons (D&D) character and combat simulation tool in Python to streamline character creation, battle simulation, and data analysis, enhancing efficiency and strategy insights for players.

Key Features:

Automated Character Data Extraction: Leveraged BeautifulSoup for web scraping to access and pull JSON-based character data directly from the MythWeavers website. Programmatically logs into user accounts and extracts character attributes, reducing manual data entry and setup time.

Character and Creature Configuration: Built modular creature.py files to define and store character and creature templates. Parameters are automatically populated based on scraped data, resulting in ready-to-play, level-accurate player characters and customized enemy creatures.

Automated Enemy Creation: Created a monster data-scraping function that locates and retrieves information from relevant web pages, building battle-ready enemy profiles with skills and stats. This enables rapid creation of new opponents for character testing and battle simulations.

Comprehensive Combat Simulation and Logging: Engineered a combat engine that allows player characters and enemies to interact in repeated battle simulations, using skills, spells, and gear dynamically. The program tracks and logs all battle outcomes, providing valuable data on strategy effectiveness and character performance over multiple scenarios.

Inventory and Spell Management: Integrated comprehensive files for gear and spells, allowing all creatures to equip items, learn or change spells, and manage rest cycles. This enhances simulation depth, providing realistic character progression and recovery mechanics.

Technical Skills Used:

Python for all programming, data management, and combat logic
Web scraping with BeautifulSoup for automated data retrieval
JSON handling for character and creature attribute storage
Modular programming for organized character and creature classes
Simulation and logging for real-time data insights and performance tracking
Impact: Scribe automates a previously time-intensive process, allowing D&D players to efficiently create, customize, and test character and enemy builds, improving strategic planning and gameplay experiences. This project showcases robust data-handling, automation, and object-oriented programming skills, as well as the ability to leverage Python for web scraping and JSON integration.
