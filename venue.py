class Venue:
    def __init__(self):
        # Step 1: Private attributes with leading underscores
        self._venue_id = ''
        self._stadium_name = ''
        self._city = ''
        self._country = ''
        self._capacity = 0
        self._pitch_type = '' # 'Batting Friendly'|'Bowling Friendly'|'Balanced'
        self._has_floodlights = False
        self._matches_hosted = 0

    # --- @property Getters (Required for ALL attributes) ---
    @property
    def venue_id(self): return self._venue_id
    @property
    def stadium_name(self): return self._stadium_name  
    @property
    def city(self): return self._city   
    @property
    def country(self): return self._country
    @property
    def capacity(self): return self._capacity
    @property   
    def pitch_type(self): return self._pitch_type
    @property
    def has_floodlights(self): return self._has_floodlights
    @property
    def matches_hosted(self): return self._matches_hosted

    # --- @setters with Validation (Required by Checklist) ---
    @capacity.setter
    def capacity(self, value):
        if int(value) < 0:
            raise ValueError("Capacity cannot be negative.")
        self._capacity = int(value)

    @matches_hosted.setter
    def matches_hosted(self, value):
        if int(value) < 0:
            raise ValueError("Matches hosted cannot be negative.")
        self._matches_hosted = int(value)

    # --- Methods ---
    def increment_matches_hosted(self):
        """Standard method required for Match logic."""
        self._matches_hosted += 1

    def display_info(self):
        """Formatted display using f-strings."""
        print(f"\nVENUE: {self._stadium_name}")
        print(f"Location: {self._city}, {self._country}")
        print(f"Capacity: {self._capacity:,} | Pitch: {self._pitch_type}")
        print(f"Floodlights: {'Yes' if self._has_floodlights else 'No'}")
        print(f"Matches Hosted: {self._matches_hosted}")

    @classmethod
    def from_data(cls, v_id, name, city, country, cap, p_type, flood, hosted):
        v = cls()
        v._venue_id = v_id
        v._stadium_name = name
        v._city = city
        v._country = country
        v.capacity = cap      # Uses setter for validation
        v._pitch_type = p_type
        v._has_floodlights = flood
        v.matches_hosted = hosted # Uses setter for validation
        return v

    @classmethod
    def load_from_line(cls, line):
        """Parses pipe-delimited line: ID|Name|City|Country|Cap|Pitch|Flood|Hosted"""
        parts = line.strip().split('|') # Changed to | for consistency
        if len(parts) != 8:
            raise ValueError(f"Expected 8 fields, got {len(parts)}")
            
        v_id, name, city, country, cap_str, p_type, flood_str, host_str = parts
        
        # Type Conversion
        flood = flood_str.lower() == 'true'
        return cls.from_data(v_id, name, city, country, int(cap_str), p_type, flood, int(host_str))

    def __str__(self):
        """Required __str__ dunder method."""
        return f"{self._stadium_name} ({self._city})"