

class Commit:
    def __init__(self, code):
        self.code = code


class Repository:
    def __init__(self, code=""):
        self.code = code

    def save_state(self):
        return Commit(self.code)

    def restore_state(self, commit):
        self.code = commit.code


class Git:
    def __init__(self):
        self._save_states = []

    def commit(self, repo):
        self._save_states.append(repo.save_state())

    def revert(self, repo):
        if len(self._save_states) > 1:
            last_state = self._save_states[-2]
            repo.restore_state(last_state)
            self._save_states.remove(last_state)


repo = Repository("Initial code")
git = Git()
git.commit(repo)

print(repo.code)

repo.code = "Code after first change"
git.commit(repo)
print(repo.code)

repo.code = "Code after second change"
git.commit(repo)
print(repo.code)

git.revert(repo)
print(repo.code)


