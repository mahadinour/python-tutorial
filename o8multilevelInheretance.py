class dad:
    basketball = 1
class son(dad):
    dance = 1
    def is_dance(self):
        return f"son    ===       is_dance-> {self.dance}"


class grandson(son):
    dance = 6
    def is_dance(self):
        return f"grandson is_dance -> {self.dance} basketball -> {self.basketball}"


if __name__ == '__main__':
    darry = dad()
    larry = son()
    harry = grandson()
    print(harry.basketball)
    print(harry.is_dance())