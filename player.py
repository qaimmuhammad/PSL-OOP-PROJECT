class Player:
    def __init__(self):
        # Identity
        self._player_id = '' # e.g. 'PSL-LQ-001'
        self._full_name = ''
        self._nationality = ''
        self._age = 0
        # Role
        self._role = '' # 'Batsman'|'Bowler'|'All-Rounder'|'Wicket-Keeper'   
        self._batting_style = '' # 'Right-Handed' | 'Left-Handed'
        self._bowling_style = '' # 'Right-Arm Fast' | 'N/A' etc.
        # Career Statistics
        self._total_runs = 0
        self._total_wickets = 0
        self._matches_played = 0
        self._batting_avg = 0.0
        self._bowling_avg = 0.0
        self._salary = 0.0 # in PKR
        self._is_captain = False
    # Getters and Setters
    @classmethod
    def from_data(cls, player_id, full_name, nationality,
    age, role, bat_style, bowl_style,
    runs, wickets, matches, salary):

        p = cls()
        p._player_id = player_id
        p._full_name = full_name
        p._nationality = nationality
        p._age = int(age)
        p._role = role
        p._batting_style = bat_style
        p._bowling_style = bowl_style
        p._total_runs = int(runs)
        p._total_wickets = int(wickets)
        p._matches_played = int(matches)
        p._salary = float(salary)
        p.compute_averages()
        return p
    @property
    def player_id(self):
        return self._player_id
    @property
    def full_name(self):
        return self._full_name  
    @property
    def nationality(self):
        return self._nationality
    @property
    def age(self):
        return self._age
    @property
    def role(self):
        return self._role
    @property
    def batting_style(self):        
        return self._batting_style
    @property   
    def bowling_style(self):
        return self._bowling_style
    @property
    def total_runs(self):
        return self._total_runs
    @property
    def total_wickets(self):
        return self._total_wickets
    @property
    def matches_played(self):
        return self._matches_played
    @property
    def batting_avg(self):
        return self._batting_avg    
    @property
    def bowling_avg(self):
        return self._bowling_avg
    @property
    def salary(self):
        return self._salary
    @total_runs.setter
    def total_runs(self, value):
        if value < 0: raise ValueError('Runs cannot be negative') 
        self._total_runs = value
        self.compute_averages()

    @total_wickets.setter
    def total_wickets(self, value):
            if value < 0: raise ValueError('Wickets cannot be negative')
            self._total_wickets = value
            self.compute_averages()

    @salary.setter
    def salary(self, value):
        if value < 0: raise ValueError('Salary cannot be negative')
        self._salary = float(value)
    def compute_averages(self):
        """Calculates batting and bowling averages, handling division by zero."""
        # Batting Avg = Total Runs / Matches (Simplified logic)
        self._batting_avg = self._total_runs / self._matches_played if self._matches_played > 0 else 0.0
        
        # Bowling Avg = Total Runs Conceded / Wickets (Using matches as proxy for demo)
        self._bowling_avg = self._total_wickets / self._matches_played if self._matches_played > 0 else 0.0
    
    def display(self):
        """Prints a formatted player profile card."""
        border = "=" * 30
        print(f"\n{border}")
        print(f" PLAYER PROFILE: {self._full_name} ({self._player_id})")
        print(f"{border}")
        print(f"Role:      {self._role}")
        print(f"Stats:     {self._total_runs} Runs | {self._total_wickets} Wickets")
        print(f"Averages:  Batting: {self._batting_avg:.2f} | Bowling: {self._bowling_avg:.2f}")
        print(f"Salary:    PKR {self._salary:,.2f}")
        print(f"{border}\n")
    @classmethod
    def load_from_line(cls, line):
            """Parses one | -delimited line from a file."""
            data = line.strip().split('|')
            # Expecting order: id|name|nat|age|role|bat|bowl|runs|wickets|matches|salary
            return cls.from_data(*data)
    @classmethod
    def from_data(cls, player_id, full_name, nationality, age, role, bat_style, bowl_style, runs, wickets, matches, salary):
        p = cls()
        p._player_id = player_id
        p._full_name = full_name
        p._nationality = nationality
        p._age = int(age)
        p._role = role
        p._batting_style = bat_style
        p._bowling_style = bowl_style
        p._total_runs = int(runs)
        p._total_wickets = int(wickets)
        p._matches_played = int(matches)
        p._salary = float(salary)
        p.compute_averages()
        return p
    
# Example Usage:
raw_line = "PSL-LQ-001|Shaheen Afridi|PK|23|Bowler|Left|Left-Arm Fast|150|95|50|5000000"
player = Player.load_from_line(raw_line)
player.display()