from player import Player
from coaching_staff import CoachingStaff
from franchise import Franchise
from venue import Venue
from match import Match


class PSL:
    def __init__(self, season, year):
        self._season = season
        self._year = year
        self._franchises = []  # Aggregation: PSL manages Franchise objects
        self._venues = []      # Aggregation: PSL manages Venue objects
        self._schedule = []    # List of Match objects

    # --- @property Getters ---
    @property
    def season(self): return self._season

    @property
    def year(self): return self._year

    @property
    def franchises(self): return self._franchises

    @property
    def venues(self): return self._venues

    @property
    def schedule(self): return self._schedule

    # --- Data Loading Methods ---
    def load_franchises(self, file_path):
        """Reads teams.txt and creates Franchise objects."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    franchise_obj = Franchise.load_from_line(line)
                    if franchise_obj:  # None returned for comment/blank lines
                        self._franchises.append(franchise_obj)
        except FileNotFoundError:
            print(f'Error: {file_path} not found. Place it in the data/ folder.')

    def load_venues(self, file_path):
        """Reads venues.txt and creates Venue objects."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    # BUG FIX: skip comment lines and blank lines
                    if not line or line.startswith('#'):
                        continue
                    self._venues.append(Venue.load_from_line(line))
        except FileNotFoundError:
            print(f'Error: {file_path} not found. Place it in the data/ folder.')

    def load_players(self, file_path):
        """Reads players.txt and assigns each Player to the correct Franchise."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    # BUG FIX: skip comment lines and blank lines
                    if not line or line.startswith('#'):
                        continue
                    player = Player.load_from_line(line)
                    parts = line.split('|')
                    # Player ID format: PSL-LQ-001 → team code is parts[0].split('-')[1]
                    team_code = parts[0].split('-')[1]  # e.g. 'LQ'
                    for fran in self._franchises:
                        if team_code == fran.franchise_id:
                            fran.add_player(player)
                            break
        except FileNotFoundError:
            print(f'Error: {file_path} not found. Place it in the data/ folder.')

    def load_coaching_staff(self, file_path):
        """Reads coaching_staff.txt and assigns each staff member to correct Franchise."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    # BUG FIX: skip comment lines and blank lines
                    if not line or line.startswith('#'):
                        continue
                    staff_member = CoachingStaff.load_from_line(line)
                    parts = line.split('|')
                    # Staff ID format: CS-LQ-001 → team code is parts[0].split('-')[1]
                    team_code = parts[0].split('-')[1]  # e.g. 'LQ'
                    for fran in self._franchises:
                        if team_code == fran.franchise_id:
                            fran.add_staff(staff_member)
                            break
        except FileNotFoundError:
            print(f'Error: {file_path} not found. Place it in the data/ folder.')

    # --- Tournament Logic ---
    def generate_schedule(self):
        """Creates a round-robin Group Stage schedule."""
        match_count = 1
        for i in range(len(self._franchises)):
            for j in range(i + 1, len(self._franchises)):
                # Rotate through available venues
                venue = self._venues[(match_count - 1) % len(self._venues)]
                new_match = Match(
                    f"M-{match_count:02}",
                    self._franchises[i],
                    self._franchises[j],
                    venue,
                    "2026-03-15",
                    "Group Stage"
                )
                self._schedule.append(new_match)
                match_count += 1

    def run_season(self):
        """Simulates all scheduled matches and prints results."""
        print(f"\n--- Starting PSL {self._season} ({self._year}) ---\n")
        for match in self._schedule:
            match.simulate_match()
            match.display_scorecard()
        print("--- All matches completed! ---\n")

    def display_points_table(self):
        """Prints franchises sorted by Points (primary) and NRR (secondary)."""
        sorted_teams = sorted(
            self._franchises,
            key=lambda x: (x.points, x.net_run_rate),
            reverse=True
        )
        print(f"\n{'='*52}")
        print(f"| {'PSL POINTS TABLE':^48} |")
        print(f"{'='*52}")
        print(f"| {'Pos':<4} {'Team':<20} {'P':<3} {'W':<3} {'L':<3} {'NRR':<9} {'Pts':<4}|")
        print(f"|{'-'*50}|")
        for i, t in enumerate(sorted_teams, start=1):
            print(f"| {i:<4} {t.team_name:<20} {t.matches_played:<3} "
                  f"{t.matches_won:<3} {t.matches_lost:<3} "
                  f"{t.net_run_rate:>+8.3f}  {t.points:<4}|")
        print(f"{'='*52}\n")

    def display_all_franchises(self):
        """Displays all franchise info cards."""
        for franchise in self._franchises:
            franchise.display_franchise_info()
            franchise.display_squad()

    def display_all_venues(self):
        """Displays all venue info."""
        for venue in self._venues:
            venue.display_info()

    # BUG FIX: These two methods were completely missing
    def find_top_scorer(self):
        """Searches all squads and returns the Player with the most runs."""
        top = None
        for fran in self._franchises:
            for player in fran.squad:
                if top is None or player.total_runs > top.total_runs:
                    top = player
        return top

    def find_top_wicket_taker(self):
        """Searches all squads and returns the Player with the most wickets."""
        top = None
        for fran in self._franchises:
            for player in fran.squad:
                if top is None or player.total_wickets > top.total_wickets:
                    top = player
        return top

    # --- Dunder Methods ---
    def __str__(self):
        """Readable string representation."""
        return f"Pakistan Super League — {self._season} ({self._year})"