teams = [
    {"name": "Auburn", "odds": 0.1359, "pickrate": 0.113},
    {"name": "ALST/SFPA", "odds": 0.0016, "pickrate": 0.001},
    {"name": "Louisville", "odds": 0.0073, "pickrate": 0.003},
    {"name": "Creighton", "odds": 0.0035, "pickrate": 0.002},
    {"name": "Michigan", "odds": 0.0043, "pickrate": 0.011},
    {"name": "UC San Diego", "odds": 0.0009, "pickrate": 0.001},
    {"name": "Texas A&M", "odds": 0.0081, "pickrate": 0.005},
    {"name": "Yale", "odds": 0.0008, "pickrate": 0.001},
    {"name": "Ole Miss", "odds": 0.0054, "pickrate": 0.002},
    {"name": "SDSU/UNC", "odds": 0.0037, "pickrate": 0.004},
    {"name": "Iowa State", "odds": 0.0263, "pickrate": 0.009},
    {"name": "Lipscomb", "odds": 0.0008, "pickrate": 0.0005},
    {"name": "Marquette", "odds": 0.0051, "pickrate": 0.002},
    {"name": "New Mexico", "odds": 0.0008, "pickrate": 0.001},
    {"name": "Michigan St", "odds": 0.0263, "pickrate": 0.045},
    {"name": "Bryant", "odds": 0.0008, "pickrate": 0.0005},
    {"name": "Florida", "odds": 0.163, "pickrate": 0.198},
    {"name": "Norfolk St", "odds": 0.0008, "pickrate": 0.002},
    {"name": "UConn", "odds": 0.0062, "pickrate": 0.008},
    {"name": "Oklahoma", "odds": 0.001, "pickrate": 0.001},
    {"name": "Memphis", "odds": 0.001, "pickrate": 0.003},
    {"name": "Colorado St", "odds": 0.0012, "pickrate": 0.001},
    {"name": "Maryland", "odds": 0.0115, "pickrate": 0.007},
    {"name": "Grand Canyon", "odds": 0.0008, "pickrate": 0.001},
    {"name": "Missouri", "odds": 0.0101, "pickrate": 0.003},
    {"name": "Drake", "odds": 0.0008, "pickrate": 0.001},
    {"name": "Texas Tech", "odds": 0.0326, "pickrate": 0.011},
    {"name": "UNC Wilmington", "odds": 0.0008, "pickrate": 0.0005},
    {"name": "Kansas", "odds": 0.0101, "pickrate": 0.005},
    {"name": "Arkansas", "odds": 0.0008, "pickrate": 0.002},
    {"name": "St John's", "odds": 0.053, "pickrate": 0.053},
    {"name": "Omaha", "odds": 0.0008, "pickrate": 0.001},
    {"name": "Duke", "odds": 0.1988, "pickrate": 0.258},
    {"name": "AMER/MSM", "odds": 0.0016, "pickrate": 0.001},
    {"name": "Mississippi St", "odds": 0.0035, "pickrate": 0.001},
    {"name": "Baylor", "odds": 0.0035, "pickrate": 0.001},
    {"name": "Oregon", "odds": 0.0043, "pickrate": 0.004},
    {"name": "Liberty", "odds": 0.0008, "pickrate": 0.001},
    {"name": "Arizona", "odds": 0.0215, "pickrate": 0.007},
    {"name": "Akron", "odds": 0.0008, "pickrate": 0.001},
    {"name": "BYU", "odds": 0.0081, "pickrate": 0.004},
    {"name": "VCU", "odds": 0.0039, "pickrate": 0.001},
    {"name": "Wisconsin", "odds": 0.0134, "pickrate": 0.011},
    {"name": "Montana", "odds": 0.0008, "pickrate": 0.0005},
    {"name": "Saint Mary's", "odds": 0.0062, "pickrate": 0.001},
    {"name": "Vanderbilt", "odds": 0.0008, "pickrate": 0.001},
    {"name": "Alabama", "odds": 0.0408, "pickrate": 0.038},
    {"name": "Robert Morris", "odds": 0.0008, "pickrate": 0.0005},
    {"name": "Houston", "odds": 0.1019, "pickrate": 0.084},
    {"name": "SIUE", "odds": 0.0008, "pickrate": 0.001},
    {"name": "Gonzaga", "odds": 0.0185, "pickrate": 0.005},
    {"name": "Georgia", "odds": 0.0008, "pickrate": 0.002},
    {"name": "Clemson", "odds": 0.0081, "pickrate": 0.006},
    {"name": "McNeese", "odds": 0.0008, "pickrate": 0.001},
    {"name": "Purdue", "odds": 0.0095, "pickrate": 0.006},
    {"name": "High Point", "odds": 0.0008, "pickrate": 0.0005},
    {"name": "Illinois", "odds": 0.0146, "pickrate": 0.003},
    {"name": "TEX/XAV", "odds": 0.0016, "pickrate": 0.001},
    {"name": "Kentucky", "odds": 0.0146, "pickrate": 0.018},
    {"name": "Troy", "odds": 0.0008, "pickrate": 0.0005},
    {"name": "UCLA", "odds": 0.0058, "pickrate": 0.002},
    {"name": "Utah State", "odds": 0.0008, "pickrate": 0.001},
    {"name": "Tennessee", "odds": 0.0371, "pickrate": 0.043},
    {"name": "Wofford", "odds": 0.0008, "pickrate": 0.001},
]

best_by_half = {}
best_by_quarter = {}
for i,team in enumerate(teams):
    quarter = i//16
    team["quarter"] = quarter
    best_by_quarter.setdefault(quarter, team)
    if team["odds"] > best_by_quarter[quarter]["odds"]:
        best_by_quarter[quarter] = team

    half = i//32
    team["half"] = half
    best_by_half.setdefault(half, team)
    if team["odds"] > best_by_half[half]["odds"]:
        best_by_half[half] = team
        

def calculate_adjusted_pickrates(pool_size, known_picks):
    for pick in known_picks:
        if pick not in [t["name"] for t in teams]:
            print(f"Unknown pick {pick}")
            raise
    
    for t in teams:
        pick_cnt = len([pick for pick in known_picks if pick == t["name"]])
        t["pickrate"] = (t["pickrate"] * (pool_size - len(known_picks)) + pick_cnt) / pool_size

def evaluate_picks(pool_size):
    #champ -> prob(champ) * prob(win pool | champ and pick == champ)
    champ_missed_value = {}

    #champ -> prob(champ) * prob(win pool | champ and pick != champ)
    champ_picked_value = {}

    #best runnerup pick for any given champ
    champ_to_runnerup_pick = {}

    #iterate through each champ -- what are the chances of winning if you didn't get pick them?
    for i,champ in enumerate(teams):
        champ_odds = champ["odds"]
        champ_pr = champ["pickrate"]
        if champ_pr > 1/pool_size:
            champ_missed_value[champ["name"]] = 0
        elif champ_pr + (1 - champ_pr)*2/3 < 1/pool_size:
            champ_missed_value[champ["name"]] = champ_odds
        else:
            champ_missed_value[champ["name"]] = champ_odds * (1/pool_size - champ_pr) / ((1-champ_pr) * 2/3)

        #runnerup -> prob(champ) * prob(runnerup) * prob(win pool | champ and pick == champ and runnerup and pick != runnerup)
        runnerup_missed_value = {}

        #runnerup -> prob(champ) * prob(runnerup) * prob(win pool | champ and pick == champ and runnerup and pick == runnerup)
        runnerup_picked_value = {}

        #now iterate through each runnerup -- what are the chances of winning if you got the champ right but didn't get the runnerup right?
        for j,runnerup in enumerate(teams):
            if i//32 == j//32: continue #same side of the bracket

            #TODO: better estimate of runnerup odds than just doubling winner odds
            runnerup_odds = min(runnerup["odds"] * 2, 1)
            runnerup_pr = min(runnerup["pickrate"] * 2, 1)

            total_odds = champ_odds * runnerup_odds
            total_pr = champ_pr * runnerup_pr

            if total_pr > 1/pool_size:
                runnerup_missed_value[runnerup["name"]] = 0
            elif total_pr + (champ_pr - total_pr)*2/3 < 1/pool_size:
                runnerup_missed_value[runnerup["name"]] = total_odds
            else:
                runnerup_missed_value[runnerup["name"]] = total_odds * (1/pool_size - total_pr) / ((champ_pr - total_pr) * 2/3)

            if total_pr * 2/3 > 1/pool_size:
                runnerup_picked_value[runnerup["name"]] = total_odds * (1/pool_size) / (total_pr * 2/3)
            else:
                runnerup_picked_value[runnerup["name"]] = total_odds

        runnerup_total_missed_value = sum([runnerup_missed_value[x] for x in runnerup_missed_value])

        pick_value_runnerup = {}
        for j,runnerup in enumerate(teams):
            if i//32 == j//32: continue #same side of the bracket
            pick_value_runnerup[runnerup["name"]] = runnerup_picked_value[runnerup["name"]] + runnerup_total_missed_value - runnerup_missed_value[runnerup["name"]]

        best_pick = sorted(pick_value_runnerup.items(), key = lambda x: x[1], reverse=True)[0][0]

        champ_to_runnerup_pick[champ["name"]] = best_pick
        champ_picked_value[champ["name"]] = pick_value_runnerup[best_pick]

        
    pick_value_champ = {}
    champ_total_missed_value = sum([champ_missed_value[x] for x in champ_missed_value])
    for champ in teams:
        pick_value_champ[champ["name"]] = champ_picked_value[champ["name"]] + champ_total_missed_value - champ_missed_value[champ["name"]]

    print(sorted([(x[0],champ_to_runnerup_pick[x[0]],x[1]) for x in pick_value_champ.items()],key=lambda x: x[2],reverse=True))

def get_best_winner_pick(pool_size):
    winner_wrong_value = {}
    winner_right_value = {}
    winner_picks = {}
    for winner in teams:
        name = winner["name"]
        winner_odds = winner["odds"]
        winner_pr = winner["pickrate"]

        if winner_pr > 1/pool_size:
            winner_wrong_value[name] = 0
        elif winner_pr + (1 - winner_pr) * 2/3 > 1/pool_size:
            frac = (1/pool_size - winner_pr) / ((1-winner_pr)*2/3)
            winner_wrong_value[name] = frac * winner_odds
        else:
            winner_wrong_value[name] = winner_odds

    total_wrong_value = 0
    for winner in teams:
        total_wrong_value += winner_wrong_value[winner["name"]]

    winner_info = {}
    for winner in teams:
        name = winner["name"]
        winner_odds = winner["odds"]
        winner_pr = winner["pickrate"]

        short_circuit = True
        if 2/3 * winner_pr < 1/pool_size and short_circuit:
            runnerup, semi1, semi2 = get_chalk_final_four(winner)
            winner_info[name] = {
                "winner": name,
                "runnerup": runnerup["name"],
                "semi1": semi1["name"],
                "semi2": semi2["name"],
                "value": winner_odds + total_wrong_value - winner_wrong_value[name]
            }
        else:
            runnerup_picks = get_best_runnerup_pick(winner, pool_size)

            winner_info[name] = {
                "winner": name,
                "runnerup": runnerup_picks["runnerup"],
                "semi1": runnerup_picks["semi1"],
                "semi2": runnerup_picks["semi2"],
                "value": runnerup_picks["value"] + total_wrong_value - winner_wrong_value[name]
            }

    all_options = []
    for pick in winner_info:
        all_options.append(winner_info[pick])
    
    all_options.sort(key = lambda x: x["value"], reverse=True)
    
    return all_options[0]
    
def get_best_runnerup_pick(winner, pool_size):
    remaining = [t for t in teams if t["half"] != winner["half"]]

    winner_odds = winner["odds"]
    winner_pr = winner["pickrate"]

    #calculate odds if runnerup is wrong
    runnerup_wrong_value = {}
    runnerup_right_value = {}
    runnerup_picks = {}
    for runnerup in remaining:
        name = runnerup["name"]

        runnerup_odds = min(2*runnerup["odds"],1)
        runnerup_pr = min(2*runnerup["pickrate"],1)

        total_odds = winner_odds * runnerup_odds
        runnerup_right_pr = winner_pr * runnerup_pr
        runnerup_wrong_pr = winner_pr * (1-runnerup_pr)

        if runnerup_right_pr > 1/pool_size:
            runnerup_wrong_value[name] = 0
        else:
            if runnerup_wrong_pr == 0:
                frac = 1
            else:
                frac = min(1,(1/pool_size - runnerup_right_pr) / (runnerup_wrong_pr * 2/3))
                
            #adjust cap to 0.99 instead of 1 to account
            #for the 1% chance something can go wrong
            #this keeps the algorithm from spitting out completely
            #random picks once it thinks it has the win locked up
            frac = min(0.99, frac)
            
            runnerup_wrong_value[name] = frac * total_odds

    total_wrong_value = 0
    for runnerup in remaining:
        total_wrong_value += runnerup_wrong_value[runnerup["name"]]

    runnerup_info = {}
    for runnerup in remaining:
        name = runnerup["name"]
        total_odds = winner_odds * runnerup_odds
        total_pr = winner_pr * runnerup_pr

        short_circuit = False
        if 2/3 * total_pr < 1/pool_size and short_circuit:
            _, semi1, semi2 = get_chalk_final_four(winner, runnerup)
            runnerup_info[name] = {
                "winner": winner["name"],
                "runnerup": name,
                "semi1": semi1["name"],
                "semi2": semi2["name"],
                "value": total_odds + total_wrong_value - runnerup_wrong_value[name],
            }
        else:
            final_four_picks = get_best_final_four_picks(winner, runnerup, pool_size)

            runnerup_info[name] = {
                "winner": winner["name"],
                "runnerup": name,
                "semi1": final_four_picks["semi1"],
                "semi2": final_four_picks["semi2"],
                "value": final_four_picks["value"] + total_wrong_value - runnerup_wrong_value[name],
            }

    all_options = sorted(runnerup_info.values(),key=lambda x: x["value"], reverse=True)
    return all_options[0]
    
def get_best_runnerup_pick_shallow(winner, pool_size):
    remaining = [t for t in teams if t["half"] != winner["half"]]

    champ_odds = winner["odds"]
    champ_pr = winner["pickrate"]

    #let prob(total) = prob(winner) * prob(runnerup)
    #runnerup -> prob(total) * prob(win pool | total, picked correct runnerup)
    runnerup_right_value = {}
    #runnerup -> prob(total) * prob(win pool | total, picked wrong runnerup)
    runnerup_wrong_value = {}
    
    for runnerup in remaining:
        runnerup_odds = min(runnerup["odds"] * 2, 1)
        runnerup_pr = min(runnerup["pickrate"] * 2, 1)

        total_odds = champ_odds * runnerup_odds
        runnerup_right_pr = champ_pr * runnerup_pr
        runnerup_wrong_pr = champ_pr * (1-runnerup_pr)

        if runnerup_right_pr * 2/3 > 1/pool_size:
            frac = (1/pool_size) / (runnerup_right_pr * 2/3)
            runnerup_right_value[runnerup["name"]] = frac * total_odds
            runnerup_wrong_value[runnerup["name"]] = 0
        elif runnerup_right_pr > 1/pool_size:
            runnerup_right_value[runnerup["name"]] = total_odds
            runnerup_wrong_value[runnerup["name"]] = 0
        elif runnerup_right_pr + (runnerup_wrong_pr * 2/3) > 1/pool_size:
            frac = (1/pool_size - runnerup_right_pr) / (runnerup_wrong_pr * 2/3)
            runnerup_right_value[runnerup["name"]] = total_odds 
            runnerup_wrong_value[runnerup["name"]] = frac * total_odds
        else:
            runnerup_right_value[runnerup["name"]] = total_odds
            runnerup_wrong_value[runnerup["name"]] = total_odds

    total_wrong_value = 0
    for runnerup in remaining:
        total_wrong_value += runnerup_wrong_value[runnerup["name"]]

    all_options = []
    for runnerup in remaining:
        name = runnerup["name"]
        all_options.append({
            "runnerup": name,
            "semi1": "",
            "semi2": "",
            "value": runnerup_right_value[name] + total_wrong_value - runnerup_wrong_value[name]
        })

    all_options.sort(key=lambda x: x["value"], reverse=True)
    return all_options[0]

def get_chalk_runnerup(winner):
    for half in best_by_half:
        if half == winner["half"]: continue
        return best_by_half[half]

def get_chalk_final_four(winner, runnerup=None):
    if runnerup is None:
        for half in best_by_half:
            if half == winner["half"]: continue
            runnerup = best_by_half[half]
            
    yield runnerup
    
    for quarter in best_by_quarter:
        if quarter in [winner["quarter"], runnerup["quarter"]]: continue
        yield best_by_quarter[quarter]

def get_best_final_four_picks(winner, runnerup, pool_size):
    #given correct picks for the winner and runnerup, find the best final four picks for the other quadrants

    #let prob(total) = prob(winner) * prob(runnerup) * prob(semi1) * prob(semi2)
    #semi1, semi2 -> prob(total) * prob(win pool | total, missed both semis)
    semi_none_right_value = {}
    #semi1, semi2 -> prob(total) * prob(win pool | total, one semi correct)
    semi_one_right_value = {}
    #semi1, semi2 -> prob(total) * prob(win pool | total, both semis correct)
    semi_both_right_value = {}

    remaining = [t for t in teams if t["quarter"] != winner["quarter"] and t["quarter"] != runnerup["quarter"]]
    all_pairs = [(team1, team2) for i,team1 in enumerate(remaining) for j,team2 in enumerate(remaining) if i < j and team1["quarter"] != team2["quarter"]]

    champ_odds = winner["odds"]
    champ_pr = winner["pickrate"]

    runnerup_odds = min(runnerup["odds"] * 2, 1)
    runnerup_pr = min(runnerup["pickrate"] * 2, 1)

    for semi1, semi2 in all_pairs:
        #TODO: more realistic probabilities
        semi1_odds = min(semi1["odds"] * 4, 1)
        semi1_pr = min(semi1["pickrate"] * 4, 1)
        semi2_odds = min(semi2["odds"] * 4, 1)
        semi2_pr = min(semi2["pickrate"] * 4, 1)

        #each final four pick is worth 80 points
        #which is kinda like the standard deviation of early round scores
        #ie someone who did well in the early rounds could beat someone
        #with an extra final four team:
        total_odds = champ_odds * runnerup_odds * semi1_odds * semi2_odds
        both_right_pr = champ_pr * runnerup_pr * semi1_pr * semi2_pr
        one_right_pr = champ_pr * runnerup_pr * (semi1_pr * (1-semi2_pr) + (1-semi1_pr) * semi2_pr)
        none_right_pr = champ_pr * runnerup_pr * (1-semi1_pr) * (1-semi2_pr)

        #Estimating this with four categories
        #no. 1: both correct, lucky in early picks
        cat1_pr = 0.5 * both_right_pr
        #no. 2: both correct, unlucky OR one correct and lucky
        cat2_pr = 0.5 * both_right_pr + 0.5 * one_right_pr
        #no. 3: one correct, unlucky OR none correct and lucky
        cat3_pr = 0.5 * one_right_pr + 0.5 * none_right_pr
        #no. 4: none correct, unlucky
        cat4_pr = 0.5 * none_right_pr

        s1 = semi1["name"]
        s2 = semi2["name"]
        
        if cat1_pr * 2/3 > 1/pool_size:
            frac = (1/pool_size) / (cat1_pr * 2/3)
            semi_both_right_value[(s1,s2)] = 0.5 * frac * total_odds
            semi_one_right_value[(s1,s2)] = 0
            semi_none_right_value[(s1,s2)] = 0
        elif cat1_pr > 1/pool_size:
            semi_both_right_value[(s1,s2)] = 0.5 * total_odds
            semi_one_right_value[(s1,s2)] = 0
            semi_none_right_value[(s1,s2)] = 0
        elif cat1_pr + (cat2_pr * 2/3) > 1/pool_size:
            frac = (1/pool_size - cat1_pr) / (cat2_pr * 2/3)
            semi_both_right_value[(s1,s2)] = 0.5 * (1+frac) * total_odds
            semi_one_right_value[(s1,s2)] = 0.5 * frac * total_odds
            semi_none_right_value[(s1,s2)] = 0
        elif cat1_pr + cat2_pr > 1/pool_size:
            semi_both_right_value[(s1,s2)] = total_odds
            semi_one_right_value[(s1,s2)] = 0.5 * total_odds
            semi_none_right_value[(s1,s2)] = 0
        elif cat1_pr + cat2_pr + (cat3_pr * 2/3) > 1/pool_size:
            frac = (1/pool_size - cat1_pr - cat2_pr) / (cat3_pr * 2/3)
            semi_both_right_value[(s1,s2)] = total_odds
            semi_one_right_value[(s1,s2)] = 0.5 * (1+frac) * total_odds
            semi_none_right_value[(s1,s2)] = 0.5 * frac * total_odds
        elif cat1_pr + cat2_pr + cat3_pr > 1/pool_size:
            semi_both_right_value[(s1,s2)] = total_odds
            semi_one_right_value[(s1,s2)] = total_odds
            semi_none_right_value[(s1,s2)] = 0.5 * total_odds
        else:
            if cat4_pr == 0:
                frac = 1
            else:
                frac = min(1,(1/pool_size - cat1_pr - cat2_pr - cat3_pr) / (cat4_pr * 2/3))
                
            #adjust cap to 0.99 instead of 1 to account
            #for the 1% chance something can go wrong
            #this keeps the algorithm from spitting out completely
            #random picks once it thinks it has the win locked up
            frac = min(0.99, frac)
            
            semi_both_right_value[(s1,s2)] = total_odds
            semi_one_right_value[(s1,s2)] = total_odds
            semi_none_right_value[(s1,s2)] = 0.5 * (1 + frac) * total_odds

    ptv = get_picks_to_value(all_pairs, semi_both_right_value, semi_one_right_value, semi_none_right_value)

    all_options = []
    for pick1, pick2 in all_pairs:
        all_options.append({
            "semi1": pick1["name"],
            "semi2": pick2["name"],
            "value": ptv[(pick1["name"],pick2["name"])],
        })

    all_options.sort(key=lambda x: x["value"], reverse=True)
        
    return all_options[0]
    
def get_picks_to_value_old(all_pairs, semi_both_right_value, semi_one_right_value, semi_none_right_value):
    #slow but straightforward version of this function
    picks_to_value = {}
    for pick1, pick2 in all_pairs:
        p1 = pick1["name"]
        p2 = pick2["name"]
        value = 0
        for semi1, semi2 in all_pairs:
            s1 = semi1["name"]
            s2 = semi2["name"]
            cnt = 1 * (pick1 == semi1) + 1 * (pick2 == semi2)
            if cnt == 2:
                value += semi_both_right_value[(s1,s2)]
            elif cnt == 1:
                value += semi_one_right_value[(s1,s2)]
            elif cnt == 0:
                value += semi_none_right_value[(s1,s2)]
            else:
                raise
                
        picks_to_value[(p1,p2)] = value
    return picks_to_value

def get_picks_to_value(all_pairs, semi_both_right_value, semi_one_right_value, semi_none_right_value):
    semi_none_right_total = 0
    semi_none_right_by_team = {}
    semi_one_right_by_team = {}
    for semi1, semi2 in all_pairs:
        s1 = semi1["name"]
        s2 = semi2["name"]
        semi_none_right_by_team.setdefault(s1,0)
        semi_none_right_by_team.setdefault(s2,0)
        semi_none_right_by_team[s1] += semi_none_right_value[(s1,s2)]
        semi_none_right_by_team[s2] += semi_none_right_value[(s1,s2)]
        semi_none_right_total += semi_none_right_value[(s1,s2)]

        semi_one_right_by_team.setdefault(s1,0)
        semi_one_right_by_team.setdefault(s2,0)
        semi_one_right_by_team[s1] += semi_one_right_value[(s1,s2)]
        semi_one_right_by_team[s2] += semi_one_right_value[(s1,s2)]

        
    picks_to_value = {}
    for pick1, pick2 in all_pairs:
        p1 = pick1["name"]
        p2 = pick2["name"]
        value = 0
        value += semi_none_right_total
        value -= semi_none_right_by_team[p1]
        value -= semi_none_right_by_team[p2]
        value += semi_none_right_value[(p1,p2)]

        value += semi_one_right_by_team[p1]
        value += semi_one_right_by_team[p2]
        value -= 2*semi_one_right_value[(p1,p2)]

        value += semi_both_right_value[(p1,p2)]

        picks_to_value[(p1,p2)] = value
    return picks_to_value

if __name__ == "__main__":
    N = 10

    known_picks = [] #["Texas Tech", "Texas Tech", "Iowa State"]
    calculate_adjusted_pickrates(N, known_picks)

    winner_pick = get_best_winner_pick(N)

    i = 2
    while i < 1e9:
        print(i, get_best_winner_pick(i))
        if i <= 100:
            i += 1
        else:
            i = round(1.03 * i)
    
    #previous version
    # evaluate_picks(N)
