import os
from psl import PSL

# ── Helper ──────────────────────────────────────────────────
def print_banner():
    print('=' * 55)
    print('   PSL SEASON 10 MANAGEMENT SYSTEM | Python OOP')
    print('=' * 55)

# ── Main Menu ────────────────────────────────────────────────
def main():
    # Initialize the League
    league = PSL('Season 10', 2026)
    
    # 1. LOAD TEAMS FIRST (This is the most important fix!)
    league.load_franchises('data/teams.txt')
    
    # 2. Load the rest of the data
    league.load_venues('data/venues.txt')
    league.load_players('data/players.txt')
    league.load_coaching_staff('data/coaching_staff.txt')
    
    # 3. Create the Match Schedule
    league.generate_schedule()
    
    print_banner()
    
    while True:
        print('\n 1. View All Franchises & Squads')
        print(' 2. View All Venues')
        print(' 3. Run Full Season Simulation')
        print(' 4. Display Points Table')
        print(' 5. Show Tournament Leaders (Runs/Wickets)')
        print(' 0. Exit')
        
        choice = input('\n Enter choice: ').strip()
        
        if choice == '1':
            # Ensure this method name matches your psl.py
            for franchise in league.franchises:
                franchise.display_franchise_info()
                
        elif choice == '2':
            for venue in league.venues:
                venue.display_info()
                
        elif choice == '3':
            league.run_season()
            
        elif choice == '4':
            league.display_points_table()
            
        elif choice == '5':
            # Note: Ensure you have find_top_scorer implemented in psl.py
            scorer = league.find_top_scorer()
            bowler = league.find_top_wicket_taker()
            print(f'\nTop Scorer: {scorer if scorer else "N/A"}')
            print(f'Top Wicket-Taker: {bowler if bowler else "N/A"}')
            
        elif choice == '0':
            print('\nExiting... Goodbye! Pakistan Zindabad!')
            break
        else:
            print('\n[!] Invalid choice. Please enter a number from 0-5.')

if __name__ == '__main__':
    main()