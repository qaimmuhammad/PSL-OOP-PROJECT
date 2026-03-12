class CoachingStaff:
    def __init__(self):
        # Step 1: Attributes with leading underscores
        self._staff_id = ''
        self._full_name = ''
        self._nationality = ''
        self._role = '' 
        self._experience_years = 0
        self._qualifications = ''
        self._franchise_team = ''
        self._salary = 0.0

    # --- @property Getters (Fulfills Checklist Requirement) ---
    @property
    def staff_id(self): return self._staff_id
    @property
    def full_name(self): return self._full_name
    @property
    def nationality(self): return self._nationality
    @property
    def role(self): return self._role
    @property
    def experience_years(self): return self._experience_years
    @property
    def qualifications(self): return self._qualifications
    @property
    def franchise_team(self): return self._franchise_team
    @property
    def salary(self): return self._salary

    # --- @setters with Validation ---
    @salary.setter
    def salary(self, value):
        if float(value) < 0: 
            raise ValueError('Salary cannot be negative')
        self._salary = float(value)

    @experience_years.setter
    def experience_years(self, value):
        if int(value) < 0:
            raise ValueError("Experience years cannot be negative.") 
        self._experience_years = int(value)
    
    # --- Methods ---
    def display(self):
        """Prints a formatted staff profile card."""
        print(f"\n{'='*35}")
        print(f" COACHING STAFF: {self._full_name}")
        print(f"{'='*35}")
        print(f"ID: {self._staff_id} | Role: {self._role}")
        print(f"Experience: {self._experience_years} Years")
        print(f"Qualifications: {self._qualifications}")
        print(f"Franchise: {self._franchise_team}")
        print(f"Salary: PKR {self._salary:,.2f}")
        print(f"{'='*35}\n")
    
    @classmethod
    def from_data(cls, sid, name, nat, role, exp, qual, team, salary):
        staff = cls()
        staff._staff_id = sid
        staff._full_name = name
        staff._nationality = nat
        staff._role = role 
        staff.experience_years = int(exp)  # Added int() cast
        staff._qualifications = qual
        staff._franchise_team = team
        staff.salary = float(salary)       # Added float() cast
        return staff
    
    @classmethod
    def load_from_line(cls, line):
        """Parses pipe-delimited line."""
        parts = line.strip().split('|')
        return cls.from_data(*parts)
    
    def __str__(self):
        """Fulfills the dunder method requirement."""
        return f"{self._full_name} ({self._role})"