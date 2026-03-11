from player import Player
from coaching_staff import CoachingStaff
from franchise import Franchise
from venue import Venue
from match import Match

class PSL:
    def __init__(self, season, year):
        self._season = season
        self._year = year
        self._franchises = []
        self._venues = []
        self._schedule = []

    @property
    def season(self): return self._season

    # --- Step 2: Methods (Data Loading) ---
    # FIXED: Changed 'data/teams.txt' to file_path
    def load_franchises(self, file_path):
        with open(file_path, 'r') as f: 
            for line in f:
                if line.strip():
                    self._franchises.append(Franchise.load_from_line(line))

    def load_venues(self, file_path):
        with open(file_path, 'r') as f:
            for line in f:
                if line.strip():
                    self._venues.append(Venue.load_from_line(line))

    def load_players(self, file_path):
        with open(file_path, 'r') as f:
            for line in f:
                if not line.strip(): continue
                player = Player.load_from_line(line)
                
                # Logic to link player to franchise based on ID
                parts = line.strip().split('|')
                team_code = parts[0].split('-')[1] # Extracts 'LQ'
                for fran in self._franchises:
                    if team_code in fran.franchise_id:
                        fran.add_player(player)

    def load_coaching_staff(self, file_path):
        with open(file_path, 'r') as f:
            for line in f:
                if not line.strip(): continue
                staff_member = CoachingStaff.load_from_line(line)
                
                parts = line.strip().split('|')
                team_code = parts[0].split('-')[1] # Extracts 'LQ'
                for fran in self._franchises:
                    if team_code in fran.franchise_id:
                        fran.add_staff(staff_member)

    # --- Step 2: Tournament Logic ---
    def generate_schedule(self):
        match_count = 1
        for i in range(len(self._franchises)):
            for j in range(i + 1, len(self._franchises)):
                # Rotate through venues
                venue = self._venues[(match_count - 1) % len(self._venues)]
                new_match = Match(f"M-{match_count:02}", self._franchises[i], 
                                  self._franchises[j], venue, "2026-03-15", "Group Stage")
                self._schedule.append(new_match)
                match_count += 1

    def run_season(self):
        print(f"\n--- Starting PSL {self._season} ({self._year}) ---")
        for match in self._schedule:
            match.simulate_match()
            print(f"Match {match.match_id}: {match.result}")

    def display_points_table(self):
        # Sort by Points (Primary) and NRR (Secondary)
        sorted_teams = sorted(self._franchises, 
                              key=lambda x: (x.points, x.net_run_rate), 
                              reverse=True)
        
        print(f"\n{'='*48}")
        print(f"| {'PSL POINTS TABLE':^44} |")
        print(f"{'='*48}")
        print(f"| {'Team':<18} | {'P':<2} | {'Pts':<3} | {'NRR':<8} |")
        print(f"|{'-'*46}|")
        for t in sorted_teams:
            print(f"| {t.team_name:<18} | {t.matches_played:<2} | {t.points:<3} | {t.net_run_rate:>+8.3f} |")
        print(f"{'='*48}\n")

    def __str__(self):
        return f"Pakistan Super League - {self._season} ({self._year})"
