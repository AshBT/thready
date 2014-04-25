import thready

def test_threaded():
    import thready
    results = set()
    def f(i):
        results.add(i)
    thready.threaded(range(10), f)
    assert results == set(range(10))
