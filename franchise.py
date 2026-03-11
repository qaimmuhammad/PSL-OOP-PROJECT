class Franchise:
    def __init__(self):
        # Identity (Section 4.3 Step 1)
        self._franchise_id = ''
        self._team_name = ''
        self._city = ''
        self._owner = ''
        
        # Statistics (Must be private with underscores)
        self._titles_won = 0
        self._matches_played = 0
        self._matches_won = 0
        self._matches_lost = 0
        self._net_run_rate = 0.0
        self._points = 0
        
        # Composition (Section 4.3 Step 2)
        self._squad = [] # List for Player objects
        self._staff = [] # List for CoachingStaff objects

    # --- @property Getters (REQUIRED for ALL attributes) ---
    @property
    def franchise_id(self): return self._franchise_id
    @property
    def team_name(self): return self._team_name
    @property
    def city(self): return self._city
    @property
    def owner(self): return self._owner
    @property
    def titles_won(self): return self._titles_won
    @property
    def matches_played(self): return self._matches_played
    @property
    def matches_won(self): return self._matches_won
    @property
    def matches_lost(self): return self._matches_lost
    @property
    def points(self): return self._points
    @property
    def net_run_rate(self): return self._net_run_rate
    @property
    def squad(self): return self._squad
    @property
    def staff(self): return self._staff

    # --- @setters with Validation (REQUIRED for Mutables) ---
    @titles_won.setter
    def titles_won(self, value):
        if int(value) < 0: raise ValueError("Titles cannot be negative")
        self._titles_won = int(value)

    @net_run_rate.setter
    def net_run_rate(self, value):
        self._net_run_rate = float(value)

    # --- Logic Methods (Section 4.3 Step 3) ---
    @property
    def win_percentage(self):
        """Calculates win rate, handling division by zero."""
        if self._matches_played == 0:
            return 0.0
        return (self._matches_won / self._matches_played) * 100

    def update_stats(self, won, nrr_change):
        """Standard method to update standings after a Match."""
        self._matches_played += 1
        if won:
            self._matches_won += 1
            self._points += 2
        else:
            self._matches_lost += 1
        self._net_run_rate += float(nrr_change)

    def add_player(self, player):
        """Requirement: Must use append() on the _squad list."""
        self._squad.append(player)

    def add_staff(self, staff_member):
        self._staff.append(staff_member)

    # --- File I/O Methods ---
    @classmethod
    def from_data(cls, fid, name, city, owner, titles):
        f = cls()
        f._franchise_id = fid
        f._team_name = name
        f._city = city
        f._owner = owner
        f.titles_won = titles # Uses setter for validation
        return f

    @classmethod
    def load_from_line(cls, line):
        parts = line.strip().split('|')
        return cls.from_data(*parts)

    def display_franchise_info(self):
        """Formatted Output using f-strings."""
        print(f"\n{'='*40}")
        print(f" FRANCHISE: {self._team_name.upper()}")
        print(f"{'='*40}")
        print(f"Owner: {self._owner} | City: {self._city}")
        print(f"Stats: P:{self._matches_played} W:{self._matches_won} L:{self._matches_lost}")
        print(f"Table: Points:{self._points} | NRR:{self._net_run_rate:+.3f}")
        print(f"Win%:  {self.win_percentage:.2f}%")
        print(f"{'='*40}\n")

    def __str__(self):
        """Required __str__ dunder method."""
        return f"{self._team_name} ({self._city})"
