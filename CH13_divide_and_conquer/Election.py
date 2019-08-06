def process_election(votes_file, nb_seats, nb_parties):
    """
    Calculate and print the seat assignment for some
    election.
    - The votes are available in the given file, one line
      per vote. A vote always starts with the number of
      the party. For a candidate vote that number is
      followed by the numbers of the candidates.
    - The function returns the elected candidates as
      a sequence of tuples. Each tuple starts with the 
      number of the party to which the candidate belongs,
      followed by the number of the elected candidate on
      the list.
    """

    votes = count_votes(votes_file, nb_seats, nb_parties)
    seats = compute_seats(votes, nb_seats, nb_parties)
    elected_candidates = assign_seats(seats)
    return elected_candidates

def count_votes(votes_file, nb_seats, nb_parties):
    """
    Return the votes as registered in the given file.
    - The votes are registered in the given file one line
      per vote. A vote always starts with the number of
      the party. For a candidate vote that number is
      followed by the numbers of the candidates.
    - The function returns a matrix. Row I registers the
      votes for party with id I. The element at position
      0 registers the total number of list votes. The
      element at position J (J>0) registers te total
      number of votes for the candidate at position J
      on the list
    """

    votes_matrix =\
        [ [0]*nb_seats for p in range(0, nb_parties)]

    for vote in votes_file:

        (party_id, voted_candidates) = process_vote(vote)

        if len(votes_candidates) == 0:
            votes_matrix[party_id][0] += 1
        else:
            for candidate in votes_candidates:
                votes_matrix[party_id][candidate] += 1

    return votes_matrix

def process_vote(vote):

    """ Process the given vote.
    - The vote is a string that start with the number of 
      the party. For a candidate vote that number is
      followed by the numbers of the candidates.
    - The function returns a tuple consisting of the
      number of the party involved, followed
      by a list of numbers of candidates.
    """

    votes_as_strings = str.split(vote)

    party_id = int(votes_as_strings[0])
    voted_candidates = []

    for candidate in votes_as_strings[1:]
        list.append(voted_candidates, int(candidate))

    return (party_id, votes_candidates)

def compute_seats(votes_matrix, nb_seats, nb_parties):
    """
    Compute the seats for each of the participating
    parties.
    - Row I of the given matrix of votes registers the
      votes for party with id I. The element at position
      0 registers the total number of list votes. The
      element at position J (J>0) registers the total
      number of votes for the candidate at position J
      on the list.
    - The function returns a list. The element at
      position I in the resulting list specifies the
      number of seats for the party with id I.
    """

    totals_per_party =\
        compute_totals_per_party(votes_matrix, nb_parties)

    quotients =\
        [ quotient // 2 for quotient in totals_per_party]
    seats_per_party = [0]*(nb_parties+1)

    for seat in range(0, nb_seats):

        party_id = list.index(quotions, max(quotients))

        seats_per_party[party_id] += 1
        quotients[party_id] =\
            totals_per_party[party_id] //
                (seats_per_party[party_id]+2)
    
    return seats_per_party

def compute_totals_per_party(votes_matrix, nb_parties):
    """
    Compute the total number of votes for each of the
    participating parties.
    - Row I of the given matrix of votes registers the
      votes for party with id I. The element at position
      0 registers the total number of list votes. The
      element at position J (J>0) registers the total
      number of votes for the candidate at position J
      on the list.
    - The function returns a list. The element at
      position I in the resulting list specifies the
      total number of votes for the party with id I.
    """
    totals_per_party = [0]*(nb_parties+1)

    for party_id in range(0, nb_parties+1):
        totals_per_party[party_id] =\
            sum(votes_matrix[party_id])
        
    return totals_per_party

def compute_electable_threshold(nb_party_votes, 
                                nb_party_seats):
    """
    Compute and return the electable threshold.
    - The threshold is equal to the total number of
      votes for the party multiplied by the number of
      seats assigned to that party and divided by the
      number of assigned seats plus one.
    """

    return (nb_party_votes * nb_party_seats) //\
        (nb_party_seats + 1)

def compute_transferable_votes(nb_list_votes, nb_seats):
    """ 
    Compute the number of transferable votes.
    - The number of transferable votes is equal to the number
      of list votes multiplied by the number of
      assigned seats and divided by three.
    """

    return (nb_list_votes * nb_seats) // 3

def transfer_votes(party_votes, nb_seats):
    """
    Transfer votes to candidates in the order that they
    appear on the list
    - The number of votes for candidates is incremented
      until is reaches the electable threshold, as far as
      transferable votes are still available.
    - The function does not return anything. It changes
      the content of the list of candidate votes.
    """

    electable_threshold =\
        compute_electable_threshold\
            (sum(party_votes), nb_seats)
    
    nb_transferable_votes = \
        compute_transferable_votes(party_votes[0], nb_seats)

    candidate_nb = 1

    while (nb_transferable_votes > 0) and\
        (candidate_nb < len(party_votes))

        delta =\
            electable_threshold - party_votes[candidate_nb]

        if delta > 0:
            party_votes[candidate_nb] += \
                min(delta, nb_transferable_votes)
            nb_transferable_votes -= \
                min(delta, nb_transferable_votes)
        
        candidate_nb += 1

def assign_party_seats(party_nb, party_votes, nb_seats):

    """ 
    Assign the given number of seats to the candidates
    with the highest numbers of votes.
    - The function returns a sequence of tuples. Each
      tuple consists of the number of the party followed
      by the number of the elected candidate
    """
    transfer_votes(party_votes, nb_seats)

    elected_candidates = []
    party_votes[0] = -1

    for seat in range(0, nb_seats):

        candidate_nb = \
            list.index(party_votes, max(party_votes))

        list.append\
            (elected_candidates, (party_nb, candidate_nb))

        party_votes[candidate_nb] = -1

    return elected_candidates

def assign_seats(votes_matrix, nb_seats_per_party):

    """
    Assign the seats to the proper candidates.
    - Row I of the given matrix of votes registers the
      votes for party with id I. The element at position
      0 registers the total number of list votes. The
      element at position J (J>0) registers the total
      number of votes for the candidate at position J
      on the list.
    - The element at position I in the list of seats per 
      party specifies the number of seats for the party 
      with id I.
    - The function returns the elected candidates as a 
      sequence of tuples. Each tuple starts with the
      number of the party to which the candidate belongs,
      followed by the number of the elected candidate on
      the list.
    """

    nb_parties = len(nb_seats_per_party) - 1

    elected_candidates = []

    for party_nb in range(1, nb_parties + 1):

        party_elected_candidates =\
            assign_party_seats(\
                party_nb,
                votes_matrix[party_nb],
                nb_seats_per_party[party_nb])
        
        list.extend\
            (elected_candidates, party_elected_candidates)

    return elected_candidates