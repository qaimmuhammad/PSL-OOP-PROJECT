📥 PSL Season Simulation System
A Python-based Object-Oriented Management System designed to simulate the Pakistan Super League (PSL). This project demonstrates Encapsulation, Inheritance, Composition, and Association by managing franchises, players, coaching staff, and match simulations.

📂 Project Structure
psl_project/
│
├── data/                    # Text files containing tournament data
│   ├── coaching_staff.txt   # Staff details (ID|Name|Nationality|Role...)
│   ├── players.txt          # Player stats (ID|Name|Nationality|Age...)
│   ├── teams.txt            # Franchise details (ID|Name|City|Owner...)
│   └── venues.txt           # Stadium details (ID|Name|City|Country...)
│
├── franchise.py             # Franchise class (Manages squads and stats)
├── player.py                # Player class (Stats and profiles)
├── coaching_staff.py        # CoachingStaff class
├── venue.py                 # Venue class (Stadium info and hosting count)
├── match.py                 # Match class (Randomized simulation logic)
├── psl.py                   # PSL class (The "Brain": scheduling & points table)
└── main.py                  # Entry point (Menu-driven interface)
🚀 Key Features
Automated Data Loading: Parses pipe-delimited (|) text files into Python objects using @classmethods.

Match Simulation: Uses random logic to generate scores and wickets, ensuring dynamic results every time.

Points Table Logic: Automatically calculates points (2 for win, 0 for loss) and updates Net Run Rate (NRR).

Dynamic Sorting: The points table is sorted primarily by Points and secondarily by NRR.

Object Association: Matches link physical Venue objects with Franchise objects, updating their internal states after every game.

🛠️ How to Run
Ensure you have Python 3.10+ installed.

Clone or download this repository.

Open your terminal/command prompt in the psl_project directory.

Run the following command:  python main.py

📝 Data Format Requirements
All data files in the data/ folder must follow the pipe-delimited format:

Teams: ID|Name|City|Owner|Titles

Players: ID|Name|Nationality|Age|Role|Batting|Bowling|Runs|Wickets|Matches|Salary

Venues: ID|Name|City|Country|Capacity|PitchType|Floodlights|HostedCount

🎓 Academic Criteria Fulfilled
Encapsulation: Used @property getters and setters with validation logic.

Composition: The Franchise class "owns" a list of Player and CoachingStaff objects.

Association: The Match class references Franchise and Venue without owning them.

File I/O: Comprehensive loading of external data into a live system. 