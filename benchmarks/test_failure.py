def test_must_fail(resource_tracker, request):
    """FIXME: DEBUG ONLY. REMOVE BEFORE MERGE."""
    with resource_tracker.track(log=request):
        raise ValueError("ooops")
