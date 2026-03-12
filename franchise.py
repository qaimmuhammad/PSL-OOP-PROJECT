class Franchise:
    def __init__(self):
        # Identity
        self._franchise_id = ''
        self._team_name = ''
        self._city = ''
        self._owner = ''

        # Statistics
        self._titles_won = 0
        self._matches_played = 0
        self._matches_won = 0
        self._matches_lost = 0
        self._net_run_rate = 0.0
        self._points = 0

        # Composition: Franchise OWNS these lists
        self._squad = []  # List of Player objects
        self._staff = []  # List of CoachingStaff objects

    # --- @property Getters ---
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

    # --- @setters with Validation ---
    @titles_won.setter
    def titles_won(self, value):
        if int(value) < 0:
            raise ValueError("Titles cannot be negative")
        self._titles_won = int(value)

    @net_run_rate.setter
    def net_run_rate(self, value):
        self._net_run_rate = float(value)

    # --- Logic Methods ---
    @property
    def win_percentage(self):
        """Calculates win rate, handling division by zero."""
        if self._matches_played == 0:
            return 0.0
        return (self._matches_won / self._matches_played) * 100

    def update_stats(self, won, nrr_change):
        """Updates standings after a Match."""
        self._matches_played += 1
        if won:
            self._matches_won += 1
            self._points += 2
        else:
            self._matches_lost += 1
        self._net_run_rate += float(nrr_change)

    def add_player(self, player):
        """Appends a Player to the squad list."""
        self._squad.append(player)

    def add_staff(self, staff_member):
        """Appends a CoachingStaff member to the staff list."""
        self._staff.append(staff_member)

    def remove_player(self, player_id):
        """Removes a player by ID using list comprehension."""
        before = len(self._squad)
        self._squad = [p for p in self._squad if p.player_id != player_id]
        if len(self._squad) == before:
            print(f'Player {player_id} not found.')

    def find_player(self, name):
        """Returns a Player by name, or None if not found."""
        for p in self._squad:
            if p.full_name.lower() == name.lower():
                return p
        return None

    # --- File I/O Methods ---
    @classmethod  # BUG FIX: was indented with 3 spaces instead of 4
    def from_data(cls, fid, name, city, owner, titles):
        """Creates a Franchise instance from raw data."""
        f = cls()
        f._franchise_id = fid
        f._team_name = name
        f._city = city
        f._owner = owner
        f._titles_won = int(titles)
        return f

    @classmethod
    def load_from_line(cls, line):
        """Parses a pipe-delimited line from teams.txt.
        Format: ID|Name|City|Stadium|Owner|Titles|..."""
        if line.startswith('#') or not line.strip():
            return None
        parts = line.strip().split('|')
        # parts[0]=ID, [1]=Name, [2]=City, [3]=Stadium, [4]=Owner, [5]=Titles
        return cls.from_data(parts[0], parts[1], parts[2], parts[4], parts[5])

    def display_franchise_info(self):
        """Formatted output using f-strings."""
        print(f"\n{'='*40}")
        print(f" FRANCHISE: {self._team_name.upper()}")
        print(f"{'='*40}")
        print(f"Owner: {self._owner} | City: {self._city}")
        print(f"Titles Won: {self._titles_won}")
        print(f"Stats: P:{self._matches_played} W:{self._matches_won} L:{self._matches_lost}")
        print(f"Table: Points:{self._points} | NRR:{self._net_run_rate:+.3f}")
        print(f"Win%:  {self.win_percentage:.2f}%")
        print(f"Squad size: {len(self._squad)} players")
        print(f"{'='*40}\n")

    def display_squad(self):
        """Prints all players in the squad."""
        print(f"\n--- {self._team_name} Squad ---")
        for p in self._squad:
            print(f"  {p}")

    def display_staff(self):
        """Prints all coaching staff."""
        print(f"\n--- {self._team_name} Coaching Staff ---")
        for s in self._staff:
            print(f"  {s}")

    # --- Dunder Methods ---
    def __str__(self):
        """Required __str__ dunder method."""
        return f"{self._team_name} ({self._city})"

    def __len__(self):
        """Returns squad size with len(franchise)."""
        return len(self._squad)

    def __bool__(self):
        """Franchise object is always truthy, even with an empty squad."""
        return True

    def __contains__(self, player):
        """Allows: player in franchise."""
        return player in self._squad

    def __lt__(self, other):
        """Allows sorting franchises by points."""
        return self._points < other._points