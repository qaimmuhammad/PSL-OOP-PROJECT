import random

class Match:
    def __init__(self, match_id, team_a, team_b, venue, match_date, match_type):
        # Step 1: Attributes with leading underscores
        self._match_id = match_id
        self._team_a = team_a # Franchise object
        self._team_b = team_b # Franchise object
        self._venue = venue   # Venue object
        self._match_date = match_date
        self._match_type = match_type # 'Group Stage'|'Qualifier'|'Final'
        
        # Results
        self._score_a = 0
        self._score_b = 0
        self._wickets_a = 0
        self._wickets_b = 0
        self._result = 'Scheduled'
        self._is_completed = False

    # --- @property Getters (Required for ALL attributes) ---
    @property
    def match_id(self): return self._match_id
    @property
    def team_a(self): return self._team_a
    @property
    def team_b(self): return self._team_b
    @property
    def venue(self): return self._venue
    @property
    def result(self): return self._result
    @property
    def is_completed(self): return self._is_completed

    # --- Simulation Logic (Section 4.5 Step 3) ---
    def simulate_match(self):
        """Simulates match and updates Franchise standings."""
        if self._is_completed:
            return

        # Simulate Scores
        self._score_a = random.randint(120, 220)
        self._score_b = random.randint(120, 220)
        self._wickets_a = random.randint(0, 10)
        self._wickets_b = random.randint(0, 10)

        # Determine Winner and Update Stats (Crucial for Points Table)
        # NRR change is simplified: (ScoreDiff / 20)
        nrr_diff = abs(self._score_a - self._score_b) / 20

        if self._score_a > self._score_b:
            self._result = f"{self._team_a.team_name} won by {self._score_a - self._score_b} runs"
            self._team_a.update_stats(won=True, nrr_change=nrr_diff)
            self._team_b.update_stats(won=False, nrr_change=-nrr_diff)
        elif self._score_b > self._score_a:
            self._result = f"{self._team_b.team_name} won by {self._score_b - self._score_a} runs"
            self._team_a.update_stats(won=False, nrr_change=-nrr_diff)
            self._team_b.update_stats(won=True, nrr_change=nrr_diff)
        else:
            self._result = "Match Tied"
            # In a tie, both usually get 1 point (update_stats would need adjustment)
            self._team_a.update_stats(won=False, nrr_change=0)
            self._team_b.update_stats(won=False, nrr_change=0)

        # Update Venue
        self._venue.increment_matches_hosted()
        self._is_completed = True

    def display_scorecard(self):
        """Formatted scorecard output."""
        if not self._is_completed:
            print(f"Match {self._match_id} is yet to be played.")
            return

        border = "-" * 40
        print(f"\n{border}")
        print(f" MATCH SCORECARD: {self._match_id}")
        print(f" {self._venue.stadium_name}, {self._venue.city}")
        print(border)
        print(f"{self._team_a.team_name:15} {self._score_a}/{self._wickets_a}")
        print(f"{self._team_b.team_name:15} {self._score_b}/{self._wickets_b}")
        print(border)
        print(f" RESULT: {self._result}")
        print(f"{border}\n")

    def __str__(self):
        """Required __str__ dunder method."""
        return f"Match {self._match_id}: {self._team_a.team_name} vs {self._team_b.team_name}"