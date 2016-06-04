
class RequestVoteMessage:

    """
    Invoked by candidates to gather votes

    candidate_id: candidate requesting vote
    term: candidate's term
    last_log_index: index of candidate's last log entry
    last_log_term: term of candidate's last log entry
    """

    def __init__(self, candidate_id, term, last_log_index, last_log_term):
        self.candidate_id = candidate_id
        self.term = term
        self.last_log_index = last_log_index
        self.last_log_term = last_log_term


class AppendEntriesMessage:

    """
    Invoked by leader to replicate log entries and discover inconsistencies; also used as heartbeat

    term: leader's term
    leader_id: so follower can redirect clients
    prev_log_index: index of log entry immediately preceding new ones
    prev_log_term: term of prev_log_index entry
    entries: log entries to store (empty for heartbeat)
    commit_index: last entry known to be committed

    """

    def __init__(self, term, leader_id, prev_log_index, prev_log_term, entries, commit_index):
        self.term = term
        self.leader_id = leader_id
        self.prev_log_index = prev_log_index
        self.prev_log_term = prev_log_term
        self.entries = entries
        self.commit_index = commit_index


    def is_heartbeat(self):
        if not self.entries:
            return True
        else:
            return False